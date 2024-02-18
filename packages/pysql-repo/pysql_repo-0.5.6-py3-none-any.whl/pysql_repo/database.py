# MODULES
from typing import Any, Generator, List
from pathlib import Path
from logging import Logger

# SQLALCHEMY
from sqlalchemy import text, MetaData, create_engine
from sqlalchemy.orm import DeclarativeMeta, Session, sessionmaker
from sqlalchemy.inspection import inspect

# CONTEXTLIB
from contextlib import contextmanager

# UTILS
from pysql_repo._database import (
    Database as _Database,
    DataBaseConfigTypedDict as _DataBaseConfigTypedDict,
)


class DataBase(_Database):
    def __init__(
        self,
        databases_config: _DataBaseConfigTypedDict,
        logger: Logger,
        base: DeclarativeMeta,
        metadata_views: List[MetaData] | None = None,
    ) -> None:
        super().__init__(databases_config, logger, base, metadata_views)

        self._engine = create_engine(
            self._database_config.get("connection_string"),
            echo=False,
            connect_args=self._database_config.get("connect_args") or {},
        )

        self._session_factory = sessionmaker(
            bind=self._engine,
            autoflush=False,
            expire_on_commit=False,
        )

        if self._database_config.get("create_on_start"):
            self.create_database()

    def create_database(self) -> None:
        insp = inspect(self._engine)
        current_view_names = [item.lower() for item in insp.get_view_names()]

        with self.session_factory() as session:
            for view in self.views:
                if view.key.lower() in current_view_names:
                    session.execute(text(f"DROP VIEW {view}"))

        self._base.metadata.create_all(self._engine)

    @contextmanager
    def session_factory(self) -> Generator[Session, Any, None]:
        session = self._session_factory()
        try:
            yield session
        except Exception as ex:
            self._logger.error("Session rollback because of exception", exc_info=ex)
            session.rollback()
            raise
        finally:
            session.close()

    def init_tables_from_json_files(
        self,
        directory: Path,
        table_names: list[str],
        timezone="CET",
    ):
        ordered_tables = self._get_ordered_tables(table_names=table_names)

        with self.session_factory() as session:
            for table in ordered_tables:
                path = directory / f"{(table_name := table.name.upper())}.json"

                raw_data = self._get_pre_process_data_for_initialization(
                    path=path,
                    timezone=timezone,
                )

                if raw_data is None:
                    continue

                session.execute(table.delete())
                session.execute(table.insert().values(raw_data))

                self._logger.info(
                    f"Successfully initialized {table_name=} from the file at {str(path)}."
                )

                session.commit()

        return ordered_tables
