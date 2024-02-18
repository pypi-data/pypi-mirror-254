# SQLALCHEMY
from typing import Any, Dict, List, Union
from sqlalchemy.orm import Session

# _CONSTANTS
from pysql_repo._constants.constants import _PARAM_SESSION


def check_values(as_list: bool = False):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            values_attr: Union[Dict[str, Any], List[Dict[str, Any]]] = kwargs.get(
                "values", None
            )

            if as_list:
                if (
                    values_attr is None
                    or not isinstance(values_attr, list)
                    or not all(
                        isinstance(item, dict) and isinstance(key, str)
                        for item in values_attr
                        for key in item.keys()
                    )
                ):
                    raise TypeError(
                        "values expected to be a list of non-empty dictionary with string keys"
                    )
            else:
                if (
                    values_attr is None
                    or not isinstance(values_attr, dict)
                    or not all(isinstance(key, str) for key in values_attr.keys())
                ):
                    raise TypeError(
                        "values expected to be a non-empty dictionary with string keys"
                    )

            return func(self, *args, **kwargs)

        return wrapper

    return decorator


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


from pysql_repo._repository import Repository
from pysql_repo._service import Service
