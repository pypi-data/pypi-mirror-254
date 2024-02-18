# SQLALCHEMY
from sqlalchemy.orm import Session

# _CONSTANTS
from pysql_repo.constants.constants import _PARAM_SESSION


def with_session(
    param_session: str = _PARAM_SESSION,
):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not isinstance(self, (Repository, Service)):
                raise TypeError(
                    f"{self.__class__.__name__} must be instance of {Repository.__name__} or {Service.__name__}"
                )

            session = kwargs.get(param_session)

            if session is None:
                with self.session_manager() as session:
                    kwargs[param_session] = session
                    return func(self, *args, **kwargs)
            elif not isinstance(session, Session):
                raise TypeError(
                    f"{param_session} must be instance of {Session.__name__}"
                )

            return func(self, *args, **kwargs)

        return wrapper

    return decorator


from pysql_repo.repository import Repository
from pysql_repo.service import Service
