import click

import lumipy.provider as lp


def main(target, domain):

    if target is None or target == 'pyprovider':
        lp.setup(domain)
    else:
        raise ValueError(f'Invalid setup type: {target}. Currently supports: \'pyprovider\' (default).')


@click.command()
@click.argument('target', required=False, metavar='TARGET')
@click.option('--domain', help='The domain to run setup in. Defaults to whatever the active domain is in config, or creds available in the env vars.')
def setup(target, domain):
    """Set up provider infrastructure and certificates.

        This will download the associated binaries and pem files then organise things for you, so they're ready to run.

        TARGET: what to set up. This currently only supports pyproviders (the default if not specified).

        Example:

            $ lumipy setup --domain=my-domain

    """
    main(target, domain)
