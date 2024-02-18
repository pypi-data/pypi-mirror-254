import re
import shutil
import socket
import subprocess as sp
import os
from signal import SIGINT
from threading import Thread
from typing import Union
from pathlib import Path

from lumipy.provider.common import get_dll_path, get_latest_local_semver, get_certs_path
from lumipy.provider.setup import setup_dlls, setup_certs, setup
from ..common import red_print, emph_print
from lumipy import config


class Factory:
    """This class encapsulates a process that manages the python provider factory dotnet application

    """

    def __init__(
            self,
            host: str,
            port: int,
            user: Union[str, None],
            domain: Union[str, None],
            whitelist_me: bool,
            _fbn_run: bool,
            _sdk_version: str = None,
            _skip_checks: bool = False,
            _dev_dll_path: Union[str, None] = None
    ):
        """Constructor of the Factory class

        Args:
            host (str): the host that the target api server is running at
            port (int): the port that the target api server is exposed at
            user (str): the user to route with. Can be a user ID, global or None. In the none case a browser window will
             be opened for you to log in with.
            domain (str): which finbourne domain to run in such as fbn-ci (internal), fbn-qa (internal) or fbn-prd.
            _fbn_run (bool): finbourne-internal option for an alternative rabbitMQ authentication when running in K8s.
            _sdk_version (str): version number of sdk to use when developing against version other than the default.

        """

        if re.match('^[\w._-]+$', host) is None:
            raise ValueError(f"Invalid value for host: {host}")

        if not isinstance(port, int):
            raise ValueError(f"Port number must be an integer. Was {type(port).__name__} ({port})")

        if _sdk_version is None:
            _sdk_version = get_latest_local_semver()

        self.domain = config.domain if domain is None else domain
        if self.domain is None:
            raise ValueError(
                f'Please set the domain by:\n'
                '  ProviderManager(p, domain="your domain")\n'
                'or adding it to lumipy config\n'
                '  import lumipy as lm\n'
                '  lm.config.add("your domain", "your token")'
            )
        if domain is not None and re.match('^[\w_-]+$', domain) is None:
            raise ValueError(f"Invalid value for domain: {domain}")

        if len(list(get_certs_path(self.domain).glob('*'))) == 0 and not _skip_checks:
            emph_print('Setting up PyProvider certs.')
            setup_certs(**config.creds(self.domain))

        if _sdk_version is None and not _skip_checks:
            emph_print('Setting up PyProvider dlls.')
            setup_dlls(**config.creds(self.domain))
            _sdk_version = get_latest_local_semver()
            if _sdk_version is None:
                raise ValueError('No valid dlls after dll setup. An unexpected problem has occurred.')

        if _dev_dll_path is not None:
            self.base_path = Path(_dev_dll_path)
        elif _sdk_version is not None:
            self.base_path = get_dll_path(_sdk_version) / 'tools' / 'net6.0' / 'any'
        elif _skip_checks:
            self.base_path = Path('/some/test/path')
        else:
            raise ValueError('Could not find base path for dlls')

        self.dll_path = self.base_path / 'Finbourne.Honeycomb.Host.dll'
        self.cmd = f'dotnet {self.dll_path} --quiet '

        self.cmd += f'--authClientDomain={domain} '

        if user is not None and user != 'global':
            self.cmd += f'--localRoutingUserId "{user}" '

        elif user is not None and user == 'global':
            self.cmd += f'--routeAs:Global '

        self.cmd += f'--config "PythonProvider:BaseUrl=>http://{host}:{port}/api/v1/" '

        if whitelist_me and user == 'global':
            if os.name == 'nt':
                my_machine_name = os.environ['COMPUTERNAME']
            else:
                my_machine_name = socket.gethostname().split('.')[0]

            red_print(f'🚨 Warning: machine name "{my_machine_name}" is whitelisted. Providers are running globally 🚨')
            self.cmd += f'"DataProvider:RoutingTypeGlobalMachineWhitelist=>{my_machine_name}" '

        if _fbn_run:
            self.cmd += '"Metrics:Enabled=>true" '
            self.cmd += '"NameServiceClient:RabbitConfigFile=>honeycomb-rabbit-config-plain.json" '
            self.cmd += '"NameServiceClient:RabbitUserPassword->/usr/app/secrets/service-main" '

        self.starting = True
        self.process = None
        self.print_thread = Thread(target=self.__print_process_output)
        self.errored = False

    def start(self):
        """Start the factory process. This will block the program while the setup is running.

        """
        emph_print(f'Starting python provider factory in {self.domain}')

        def throw_setup_error(msg):
            cmd = 'python -m lumipy.setup --token=<your token> --api_url=https://<your domain>.lusid.com/honeycomb'
            kws = setup.__doc__.split('Keyword Args:')[-1].replace(' '*8, ' '*4)
            raise ValueError(
                f'{msg}. Have you run the provider setup?\n  Try:\n    {cmd}\n\n'
                'You can also run the setup function under lumipy.provider for other types of authentication. '
                f'It takes the following keyword arguments:\n{kws.rstrip()}\n\n'
                'If none are provided it will look for authentication values in your environment variables in the '
                'same way as Finbourne\'s other python SDKs.'
            )

        if not self.dll_path.exists():
            throw_setup_error('Provider factory dll is missing')

        dom_path = get_certs_path(self.domain)
        certs = list(dom_path.glob('*.pem'))

        if len(certs) != 2:
            throw_setup_error('Certificate .pem files are missing')

        for dll_cert in self.base_path.glob('*.pem'):
            dll_cert.unlink()

        for cert in certs:
            shutil.copy2(cert, self.base_path / cert.parts[-1])

        print(self.cmd, end='\n\n')

        self.process = sp.Popen(self.cmd.split(), shell=False, stdout=sp.PIPE, stderr=sp.PIPE)

        self.print_thread.start()

        while self.starting:
            pass

        self.errored = self.process.poll() is not None

        if self.errored:
            self.print_thread.join()

    def stop(self):
        """Stop the factory process and shut down the providers. This will block the program while the termination is
        completing.

        """
        if self.process.poll() is not None:
            # no-op
            return

        emph_print('\nStopping python provider factory')

        if os.name == 'nt':
            self.process.terminate()
        else:
            self.process.send_signal(SIGINT)

        while self.process.poll() is None:
            pass

        self.print_thread.join()

    def __print_process_output(self):

        # Set a loop running in another thread that periodically polls the process
        # When there's a new line of output print it
        # If the process is in exit state, set block=False so the stop method stops blocking

        bad_lines = 0
        while self.process.poll() is None:

            output = self.process.stdout.readline().decode('utf-8', errors="replace").rstrip()

            if output:
                print(output)

            if 'RemoteCancellation: ResubscribeAsync failed with' in output:
                bad_lines += 1
            else:
                # reset count in case it's a blip
                bad_lines = 0

            if bad_lines > 50:
                self.errored = True
                break

            if 'Running! Hit Ctrl+C to shut down services' in output:
                self.starting = False
