from pathlib import Path
from typing import Optional

from numerous.cli.auth import get_refresh_token
from numerous.cli.job import start_local_job
from numerous.cli.repository import NumerousRepository
from numerous.cli.utils import print_load_warnings


def create_local_execution_from_repository(
    path: Optional[Path] = None,
) -> tuple[NumerousRepository, str, str]:
    path = path or Path.cwd()
    repo, load_warnings = NumerousRepository(path).load()
    print_load_warnings(load_warnings)

    if repo.remote is None or repo.scenario is None:
        raise RuntimeError(
            "Repository not configured correctly, try checking out a scenario or re-initializing."
        )

    execution_id = start_local_job(repo)
    refresh_token = get_refresh_token(repo, execution_id)

    return repo, execution_id, refresh_token
