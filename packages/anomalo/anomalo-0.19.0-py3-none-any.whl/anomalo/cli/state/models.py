from __future__ import annotations

import os
from collections import defaultdict
from dataclasses import dataclass, field
from difflib import unified_diff
from textwrap import indent
from typing import Any, TypeVar

import yaml
from dataclasses_json import (
    DataClassJsonMixin,
    config,
)
from dataclasses_json.core import Json


SM = TypeVar("SM", bound="StateModel")


always_exclude = lambda _: True


class StateModel(DataClassJsonMixin):
    pass


@dataclass
class Table(StateModel):
    config: dict[str, Any] = field(
        default_factory=dict, metadata=config(field_name="configuration")
    )
    checks: dict[str, Check] = field(default_factory=dict)


@dataclass
class Check(StateModel):
    check_type: str = field(metadata=config(field_name="check"))
    params: dict[str, Any] = field(default_factory=dict)


@dataclass
class State(StateModel):
    tables: dict[str, Table] = field(
        default_factory=lambda: defaultdict(Table),
        metadata=config(field_name="AnomaloTables"),
    )

    @classmethod
    def _remove_unused_table_properties(cls, kvs: dict[str, Json]) -> dict[str, Json]:
        # Remove empty tables and unused configuration / checks properties from tables
        if isinstance(kvs, dict) and "AnomaloTables" in kvs:
            kvs["AnomaloTables"] = {
                table_ref: {
                    table_data_key: table_data_value
                    for table_data_key, table_data_value in table_data.items()
                    if table_data_value
                }
                for table_ref, table_data in kvs["AnomaloTables"].items()
                if table_data and any(table_data.values())
            }
        return kvs

    @classmethod
    def from_dict(cls, kvs: Json, *args: Any, **kwargs: Any) -> State:
        new_state = super().from_dict(
            cls._remove_unused_table_properties(kvs), *args, **kwargs
        )
        # dataclasses_json can't construct a defaultdict using type() since defaultdict
        # requires an argument. Instead, replace the parsed dict with a defaultdict.
        new_state.tables = defaultdict(Table, new_state.tables.items())
        return new_state

    def to_dict(self, *args: Any, **kwargs: Any) -> dict[str, Json]:
        return self._remove_unused_table_properties(super().to_dict(*args, **kwargs))


@dataclass
class Action:
    prev: dict[str, Any] | StateModel | None = None
    new: dict[str, Any] | StateModel | None = None

    def __str__(self) -> str:
        raise NotImplementedError

    def diff(self) -> str | None:
        if self.prev == self.new:
            return None

        def _repr(obj: dict[str, Any] | StateModel) -> str:
            flat = obj.to_dict() if isinstance(obj, StateModel) else obj
            return indent(yaml.safe_dump(flat), prefix="    ") if flat else ""

        diff = unified_diff(
            _repr(self.prev).splitlines(), _repr(self.new).splitlines(), lineterm=""
        )
        # Skip +++, --- header lines in resulting generator
        next(diff)
        next(diff)
        return indent(os.linesep.join(diff), prefix="  |  ")

    @property
    def verb(self) -> str:
        if self.new:
            return "Modify" if self.prev else "Create"
        if self.prev:
            return "Destroy"
        return "N/A"


@dataclass
class TableConfigAction(Action):
    prev: dict[str, Any] | None = None
    new: dict[str, Any] | None = None
    table_ref: str | None = None

    def __str__(self) -> str:
        return f"{self.verb} {self.table_ref} configuration"


@dataclass
class CheckAction(Action):
    prev: Check | None = None
    new: Check | None = None
    table_ref: str | None = None
    check_ref: str | None = None

    def __str__(self) -> str:
        return f"{self.verb} {self.check_ref} on {self.table_ref}"
