import logging
import time

from sqlalchemy import Engine, event
from pysql_repo.database import DataBase
from pysql_repo.decorators import with_session
from pysql_repo.repository import Repository
from pysql_repo.service import Service
from pysql_repo.constants.enum import Operators, LoadingTechnique


logging.basicConfig()
_logger = logging.getLogger("pysql_repo")
_logger.setLevel(logging.INFO)


@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    conn.info.setdefault("query_start_time", []).append(time.perf_counter())
    _logger.debug("Start Query: %s, {%s}", statement, parameters)


@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    total = time.perf_counter() - conn.info["query_start_time"].pop(-1)
    _logger.debug("Query completed in %fs", total)
