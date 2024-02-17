import click

from ..utils import CONTEXT_SETTINGS
from .notebook import monitor_sync, start_notebook, start_standalone_sync, stop_notebook


@click.group(name="notebook", context_settings=CONTEXT_SETTINGS)
def notebook():
    """Commands for managing JupyterLab sessions on dedicated VMs in the cloud.

    The Python packages you have installed locally are automatically installed.
    (See https://docs.coiled.io/user_guide/package_sync.html for details.)

    Your local filesystem can also be synced using the `--sync` flag.

    This creates an easy "make my laptop bigger" command, since you'll have
    the same files and environment, just on a bigger machine in the cloud.
    """
    pass


notebook.add_command(start_notebook, "start")
notebook.add_command(stop_notebook, "stop")
notebook.add_command(monitor_sync, "monitor")
notebook.add_command(start_standalone_sync, "start-sync")
