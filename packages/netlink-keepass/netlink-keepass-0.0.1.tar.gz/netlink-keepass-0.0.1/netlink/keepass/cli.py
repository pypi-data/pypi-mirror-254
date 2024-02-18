import pathlib
import click
from netlink.keepass import reader


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "-k",
    "--keyfile",
    type=click.Path(
        exists=True,
        dir_okay=False,
        path_type=pathlib.Path,
    ),
    help="'KeePass Key File'",
)
@click.option(
    "-t",
    "--token",
    type=click.Path(
        exists=True,
        dir_okay=False,
        path_type=pathlib.Path,
    ),
    help="Fernet token file",
)
@click.option("-p", "--port", type=int, default=8666, help="Port (default: 8666)")
@click.option(
    "-x",
    "--shutdown",
    default="_shutdown",
    help="Pseudo directory to shutdown server (default: '_shutdown')",
)
@click.argument(
    "filename",
    type=click.Path(
        exists=True,
        dir_okay=False,
        path_type=pathlib.Path,
    ),
)
@click.argument("secret")
def reader_cli(filename, secret, keyfile, token, port, shutdown):
    """
    Start REST server to read KeePass Database FILENAME using SECRET.

    \b
    SECRET is either the 'KeePass Master Password'
           or Fernet key, if Fernet token file is provided.

    Port will be opened for localhost only.
    """
    reader(filename=filename, secret=secret, keyfile=keyfile, token=token, port=port, shutdown=shutdown)
