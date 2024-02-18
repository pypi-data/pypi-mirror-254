import importlib.metadata

from ..utils import bold, green


def command_version():
    version = importlib.metadata.version("numerous.sdk")
    print(green(f"{bold('numerous.sdk')} command line tool v{bold(version)}"))
