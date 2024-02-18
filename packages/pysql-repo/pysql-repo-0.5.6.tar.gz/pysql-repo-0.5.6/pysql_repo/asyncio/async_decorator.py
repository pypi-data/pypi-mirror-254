# SQLALCHEMY
from sqlalchemy.ext.asyncio import AsyncSession

# _CONSTANTS
from pysql_repo.constants.constants import _PARAM_SESSION


def with_async_session(
    param_session: str = _PARAM_SESSION,
):
    def decorator(func):
        async def wrapper(self, *args, **kwargs):
            if not isinstance(self, (AsyncRepository, AsyncService)):
                raise TypeError(
                    f"{self.__class__.__name__} must be instance of {AsyncRepository.__name__} or {AsyncService.__name__}"
                )

            session = kwargs.get(param_session)

            if session is None:
                async with self.session_manager() as session:
                    kwargs[param_session] = session
                    return await func(self, *args, **kwargs)
            elif not isinstance(session, AsyncSession):
                raise TypeError(
                    f"{param_session} must be instance of {AsyncSession.__name__}"
                )

            return await func(self, *args, **kwargs)

        return wrapper

    return decorator


from pysql_repo.asyncio.async_repository import AsyncRepository
from pysql_repo.asyncio.async_service import AsyncService
