# MODULES
from typing import TypeVar, Generic
from logging import Logger

# MODELS
from pysql_repo.repository import Repository


_T = TypeVar("_T", bound=Repository)


class Service(Generic[_T]):
    def __init__(
        self,
        repository: _T,
        logger: Logger,
    ) -> None:
        self._repository = repository
        self._logger = logger

    def session_manager(self):
        return self._repository.session_manager()
