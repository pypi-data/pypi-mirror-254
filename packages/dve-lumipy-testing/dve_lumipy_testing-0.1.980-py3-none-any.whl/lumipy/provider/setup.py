import os
import re
import shutil
import subprocess
from pathlib import Path
from zipfile import ZipFile
from shutil import rmtree, which, copy2
from subprocess import run, CalledProcessError

from lusid_drive import ApiException, Configuration, ApiClient, FilesApi

from lumipy import get_client
from time import sleep

from lumipy.provider.common import get_dll_path, min_version, max_version, get_certs_path
from lumipy.common import emph

import semver

drive_path = '/LUSID-support-document-share/Luminesce/'
semverRegex = r'(\d+\.\d+\.\d+)'


def find_dotnet_sdks():
    instruction = "Please install .NET 6.0."

    if which('dotnet') is None:
        raise ValueError(f".NET runtime not found. {instruction}]")

    try:
        result = subprocess.run(["dotnet", "--list-sdks"], capture_output=True, text=True, check=True)
    except CalledProcessError:
        raise ValueError(f"Error when trying to list .NET SDKs. {instruction}")

    semvers = re.findall(semverRegex, result.stdout)
    if len(semvers) == 0:
        raise ValueError(f"No .NET SDKs were found. {instruction}")


def get_latest_valid_version(client):
    # noinspection SqlResolve
    # noinspection SqlNoDataSourceInspection
    df = client.run(
        '''
        SELECT
           [Id], [Name]
        FROM
           [Drive.File]
        WHERE
           ([RootPath] = '/LUSID-support-document-share/Luminesce/Providers/')
           and ([Name] LIKE 'finbourne.luminesce.pythonproviders%.zip')
        ''',
        quiet=True
    )
    df['SemVer'] = df.Name.str.extract(semverRegex)
    df['SemVer'] = df.SemVer.apply(semver.Version.parse)
    df = df.sort_values('SemVer', ascending=False)
    df = df[df.SemVer.between(min_version, max_version)]

    if len(df) == 0:
        raise ValueError(
            f'No pyprovider binaries available in Drive with version between {min_version} and {max_version} '
            'Please contact support as the binaries may not have been added to your domain.'
        )

    return str(df.iloc[0].SemVer)


# noinspection SqlResolve,SqlNoDataSourceInspection
def download_files(lm_client, files, path, pattern):
    sql = f"SELECT [Id], [Name] FROM [Drive.File] WHERE [RootPath] = '{path}' and [Name] like '{pattern}'"

    wait = 30
    df = lm_client.run(sql, quiet=True)
    locations = []
    for _, r in df.iterrows():
        _print(f'Downloading {path}/{r["Name"]}.', 4)

        count = 0
        while True:
            try:
                locations.append(Path(files.download_file(r['Id'])))
                break
            except ApiException as ae:
                if count > 3:
                    raise ae
                count += 1
                _print(f'Couldn\'t get file (reason: {ae.reason}). Waiting {wait}s before retry.')
                sleep(wait)

    return locations


def _print(s, n=0):
    indent = ' ' * n
    print(indent + s)


def setup_certs(domain=None, **kwargs):

    lm_client = get_client(domain, **kwargs)
    cfg = Configuration(host=f'https://{lm_client.get_domain()}.lusid.com/drive')
    cfg.access_token = lm_client.get_token()
    files = FilesApi(ApiClient(cfg))

    c_str = emph(f'[{lm_client.get_domain()}]')
    _print(f'Getting pem files for {c_str}.', 2)
    pem_paths = download_files(lm_client, files, drive_path + 'Certificates', '%.pem')
    if len(pem_paths) != 2:
        raise ValueError(
            f"Couldn't get {drive_path}/Certificates/*.pem. "
            f"Please contact support as the certs may not have been added to your domain."
        )

    certs_path = get_certs_path(lm_client.get_domain())
    if certs_path.exists():
        shutil.rmtree(certs_path)
    certs_path.mkdir(parents=True, exist_ok=True)

    for pem_path in pem_paths:
        pem_name = pem_path.parts[-1].strip(';')
        _print(f'Copying {pem_name}.', 4)
        target = certs_path / pem_name
        copy2(pem_path, target)

    _print('Checking pem files.', 4)
    pems = list(certs_path.glob('*.pem'))
    if len(pems) != 2:
        raise ValueError(f"Couldn't find pem files at {certs_path}.")

    _print('Successfully added pem files.', 4)


def setup_dlls(domain=None, **kwargs):

    find_dotnet_sdks()

    lm_client = get_client(domain, **kwargs)
    cfg = Configuration(host=f'https://{lm_client.get_domain()}.lusid.com/drive')
    cfg.access_token = lm_client.get_token()
    files = FilesApi(ApiClient(cfg))

    _print(f'Getting PyProvider dlls.', 2)
    c_str = emph(f'[{lm_client.get_domain()}]')
    _print(f'Finding the latest valid version in {c_str}', 4)
    sdk_ver = get_latest_valid_version(lm_client)
    _print(f'Version = {sdk_ver}', 6)
    sdk_version = kwargs.pop('sdk_version', sdk_ver)
    bin_path = get_dll_path(sdk_version)

    if bin_path.exists():
        rmtree(bin_path)
    else:
        bin_path.mkdir(parents=True)

    zip_name = f'finbourne.luminesce.pythonproviders.{sdk_version}.zip'

    _print('Getting the provider factory dlls zip.', 4)
    zip_path = download_files(lm_client, files, drive_path + 'Providers', zip_name)
    if len(zip_path) != 1:
        raise ValueError(f"Couldn't get {drive_path}/{zip_name}. Please contact support as the binaries may not have been added to your domain.")

    _print('Unzipping the provider factory dlls.', 4)
    with ZipFile(zip_path[0], 'r') as zf:
        zf.extractall(bin_path)

    _print('Cleaning up zip file.', 4)
    os.remove(zip_path[0])


def setup(domain=None, **kwargs):
    """Run the lumipy python providers setup given your user credentials for a domain.

    Keyword Args:
        token (str): Bearer token used to authenticate.
        api_secrets_filename (str): Name of secrets file (including full path)
        api_url (str): luminesce API url
        app_name (str): Application name (optional)
        certificate_filename (str): Name of the certificate file (.pem, .cer or .crt)
        proxy_url (str): The url of the proxy to use including the port e.g. http://myproxy.com:8888
        proxy_username (str): The username for the proxy to use
        proxy_password (str): The password for the proxy to use
        correlation_id (str): Correlation id for all calls made from the returned finbournesdkclient API instances

    """

    _print('Setting up python providers. 🛠')
    show_hint = kwargs.pop('show_hint', True)

    setup_certs(domain, **kwargs)
    setup_dlls(domain, **kwargs)

    _print("\nAll set! You can now build and run python Luminesce providers.")

    if show_hint:
        _print(f"\nTry running the following command in a terminal:")
        cmd = 'lumipy run demo '
        _print(cmd + '\n', 2)
        _print('This will open a browser window for you to log in. '
               'Once startup has finished only you will be able to query it.\n')
        _print('To run these demo providers so others in your domain can use them:')
        cmd = 'lumipy run demo --user=global --whitelist-me'
        _print(cmd + '\n', 2)
        _print('In this case it will not open a browser window.')
