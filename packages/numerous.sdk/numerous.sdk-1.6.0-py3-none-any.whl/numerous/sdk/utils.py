from typing import Any, NoReturn


class DataFrameStub:
    def __call__(self, *args, **kwargs) -> NoReturn:
        raise LibraryNotInstalledError("pandas")

    def __getattr__(self, attr) -> NoReturn:  # noqa: F841
        raise LibraryNotInstalledError("pandas")


class PandasStub:
    def __getattr__(self, attr: str) -> Any:  # noqa: F841
        if attr == "DataFrame":
            return DataFrameStub()
        raise LibraryNotInstalledError("pandas")


class LibraryNotInstalledError(Exception):
    def __init__(self, library_name):
        self.library_name = library_name
        self.message = (
            f"{library_name} is not installed. "
            f"Please install it using 'pip install {library_name}'."
        )
