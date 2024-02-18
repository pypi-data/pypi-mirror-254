# MODULES
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    Sequence,
)

# CONTEXTLIB
from contextlib import AbstractContextManager

# SQLALCHEMY
from sqlalchemy import ColumnExpressionArgument, Select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, InstrumentedAttribute

# DECORATORS
from pysql_repo._decorators import check_values as _check_values, with_session

# UTILS
from pysql_repo._utils import (
    _FilterType,
    RelationshipOption,
    build_delete_stmt,
    build_insert_stmt,
    build_select_stmt,
    build_update_stmt,
    select_distinct,
    apply_pagination,
)


_T = TypeVar("_T", bound=declarative_base())


class Repository:
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
    ) -> None:
        self._session_factory = session_factory

    def session_manager(self):
        return self._session_factory()

    def _build_query_paginate(
        self,
        session: Session,
        stmt: Select[Tuple[_T]],
        model: Type[_T],
        page: int,
        per_page: int,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        group_by: Optional[ColumnExpressionArgument] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[Union[List[str], str]] = None,
        limit: int = None,
    ) -> Tuple[Select[Tuple[_T]], str]:
        stmt = build_select_stmt(
            stmt=stmt,
            model=model,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            group_by=group_by,
            order_by=order_by,
            direction=direction,
            limit=limit,
        )

        return apply_pagination(
            session=session,
            stmt=stmt,
            page=page,
            per_page=per_page,
        )

    @with_session()
    def _select(
        self,
        model: Type[_T],
        distinct: Optional[ColumnExpressionArgument] = None,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        session: Optional[Session] = None,
    ) -> Optional[_T]:
        stmt = select_distinct(
            model=model,
            expr=distinct,
        )

        return self._select_stmt(
            stmt=stmt,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            session=session,
        )

    @with_session()
    def _select_stmt(
        self,
        stmt: Select[Tuple[_T]],
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        group_by: Optional[ColumnExpressionArgument] = None,
        session: Optional[Session] = None,
    ) -> Optional[_T]:
        stmt = build_select_stmt(
            stmt=stmt,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            group_by=group_by,
        )

        return session.execute(stmt).unique().scalar_one_or_none()

    @with_session()
    def _select_all(
        self,
        model: Type[_T],
        distinct: Optional[List[ColumnExpressionArgument]] = None,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
        session: Optional[Session] = None,
    ) -> Sequence[_T]:
        stmt = select_distinct(
            model=model,
            expr=distinct,
        )

        return self._select_all_stmt(
            stmt=stmt,
            model=model,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            order_by=order_by,
            direction=direction,
            limit=limit,
            session=session,
        )

    @with_session()
    def _select_all_stmt(
        self,
        stmt: Select[Tuple[_T]],
        model: Type[_T],
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        group_by: Optional[ColumnExpressionArgument] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[Union[List[str], str]] = None,
        limit: int = None,
        session: Optional[Session] = None,
    ) -> Sequence[_T]:
        stmt = build_select_stmt(
            stmt=stmt,
            model=model,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            group_by=group_by,
            order_by=order_by,
            direction=direction,
            limit=limit,
        )

        return session.execute(stmt).unique().scalars().all()

    @with_session()
    def _select_paginate(
        self,
        model: Type[_T],
        page: int,
        per_page: int,
        distinct: Optional[ColumnExpressionArgument] = None,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
        session: Optional[Session] = None,
    ) -> Tuple[Sequence[_T], str]:
        stmt = select_distinct(
            model=model,
            expr=distinct,
        )

        return self._select_paginate_stmt(
            stmt=stmt,
            model=model,
            page=page,
            per_page=per_page,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            order_by=order_by,
            direction=direction,
            limit=limit,
            session=session,
        )

    @with_session()
    def _select_paginate_stmt(
        self,
        stmt: Select[Tuple[_T]],
        model: Type[_T],
        page: int,
        per_page: int,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        group_by: Optional[ColumnExpressionArgument] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
        session: Optional[Session] = None,
    ) -> Tuple[Sequence[_T], str]:
        stmt, pagination = self._build_query_paginate(
            session=session,
            stmt=stmt,
            model=model,
            page=page,
            per_page=per_page,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            group_by=group_by,
            order_by=order_by,
            direction=direction,
            limit=limit,
        )

        return session.execute(stmt).unique().scalars().all(), pagination

    @_check_values(as_list=False)
    @with_session()
    def _update_all(
        self,
        model: Type[_T],
        values: Dict[str, Any],
        filters: Optional[_FilterType] = None,
        flush: bool = False,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> Sequence[_T]:
        if (
            values is None
            or not isinstance(values, dict)
            or len(values) == 0
            or any([not isinstance(item, str) for item in values.keys()])
        ):
            raise TypeError("values expected to be Dict[str, Any]")

        stmt = build_update_stmt(
            model=model,
            values=values,
            filters=filters,
        )

        sequence = session.execute(stmt).unique().scalars().all()

        if flush:
            session.flush()
        if commit:
            session.commit()

        [session.refresh(item) for item in sequence]

        return sequence

    @_check_values(as_list=False)
    @with_session()
    def _update(
        self,
        model: Type[_T],
        values: Dict[str, Any],
        filters: Optional[_FilterType] = None,
        flush: bool = False,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> Optional[_T]:
        stmt = build_update_stmt(
            model=model,
            values=values,
            filters=filters,
        )

        item = session.execute(stmt).unique().scalar_one_or_none()

        if item is None:
            return None

        if flush:
            session.flush()
        if commit:
            session.commit()

        session.refresh(item)

        return item

    @_check_values(as_list=True)
    @with_session()
    def _add_all(
        self,
        model: Type[_T],
        values: List[Dict[str, Any]],
        flush: bool = False,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> Sequence[_T]:
        stmt = build_insert_stmt(model=model)

        sequence = session.execute(stmt, values).unique().scalars().all()

        if flush:
            session.flush()
        if commit:
            session.commit()

        if flush or commit:
            [session.refresh(item) for item in sequence]

        return sequence

    @_check_values(as_list=False)
    @with_session()
    def _add(
        self,
        model: Type[_T],
        values: Dict[str, Any],
        flush: bool = False,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> Optional[_T]:
        stmt = build_insert_stmt(model=model)

        item = session.execute(stmt, values).unique().scalar_one()

        if flush:
            session.flush()
        if commit:
            session.commit()

        if flush or commit:
            session.refresh(item)

        return item

    @with_session()
    def _delete_all(
        self,
        model: Type[_T],
        filters: Optional[_FilterType] = None,
        flush: bool = True,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> bool:
        stmt = build_delete_stmt(
            model=model,
            filters=filters,
        )

        sequence = session.execute(stmt).unique().scalars().all()

        if len(sequence) == 0:
            return False

        if flush:
            session.flush()
        if commit:
            session.commit()

        return True

    @with_session()
    def _delete(
        self,
        model: Type[_T],
        filters: Optional[_FilterType] = None,
        flush: bool = True,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> bool:
        stmt = build_delete_stmt(
            model=model,
            filters=filters,
        )

        item = session.execute(stmt).unique().scalar_one_or_none()

        if item is None:
            return False

        if flush:
            session.flush()
        if commit:
            session.commit()

        return True
