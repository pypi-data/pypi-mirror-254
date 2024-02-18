from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from contextlib import suppress
from functools import cached_property, lru_cache
from time import sleep

from ...client import Client
from .errors import CheckNotFound, InvalidTableRef, TableNotFound
from .models import Action, Check, CheckAction, State, TableConfigAction


def retry_requests(f):
    try_times = 3

    def wrapper(*args, **kwargs):
        for i in range(try_times):
            try:
                return f(*args, **kwargs)
            except RuntimeError:
                if i >= try_times - 1:
                    # Last retry, re-raise exception
                    raise
                amount = 2 * (i + 1)
                sleep(amount)

    return wrapper


class APIDriver:
    def __init__(self, client: Client):
        self.client = client
        self.state = State()

    def load_table(self, table_ref: str) -> None:
        if self.state.tables[table_ref].config:
            return
        warehouse_name, _ = self._table_ref_parts(table_ref)
        table_info = self._table_raw(table_ref)
        self.state.tables[table_ref].config = (
            self._filter_table_config_response(table_info.get("config") or {}) or {}
        )

    def load_all_checks(self, table_ref: str) -> None:
        for check_ref in self._checks_for_table_raw(table_ref).keys():
            self.load_check(table_ref, check_ref)

    def load_check(self, table_ref: str, check_ref: str) -> None:
        try:
            raw_check = self._checks_for_table_raw(table_ref)[check_ref]
        except KeyError as e:
            raise CheckNotFound(table_ref, check_ref) from e
        self.state.tables[table_ref].checks[check_ref] = Check(
            check_type=raw_check["check_type"],
            params=(raw_check["config"].get("params") or {})
            | {"notification_channel": raw_check["additional_notification_channel_id"]},
        )

    def load_from_state(self, other_state: State) -> None:
        for table_ref, table in other_state.tables.items():
            if table.config:
                self.load_table(table_ref)
            for check_ref in table.checks.keys():
                with suppress(CheckNotFound):
                    self.load_check(table_ref, check_ref)

    def apply_action(self, action: Action) -> None:
        if isinstance(action, TableConfigAction):
            if action.new:
                self.client.configure_table(
                    table_id=self._table_id(action.table_ref), **action.new
                )
        elif isinstance(action, CheckAction):
            if action.new:
                self.client.create_check(
                    self._table_id(action.table_ref),
                    action.new.check_type,
                    **(action.new.params | {"ref": action.check_ref}),
                )
            else:
                self.client.delete_check(
                    self._table_id(action.table_ref),
                    # Current check ID for this check
                    self._checks_for_table_raw(action.table_ref)[action.check_ref][
                        "check_id"
                    ],
                )

    @cached_property
    def table_refs(self) -> set[str]:
        return set(self._tables.keys())

    @cached_property
    @retry_requests
    def _warehouses_raw(self) -> Sequence[tuple[int, str]]:
        return [
            (w["id"], w["name"]) for w in self.client.list_warehouses()["warehouses"]
        ]

    @cached_property
    def _warehouses(self) -> dict[str, int]:
        warehouse_counts = defaultdict(int)
        for _, wh_name in self._warehouses_raw:
            warehouse_counts[wh_name] += 1
        # Exclude non-unique warehouse names
        duplicates = {
            wh_name for wh_name, count in warehouse_counts.items() if count > 1
        }
        ret = {
            wh_name: wh_id
            for wh_id, wh_name in self._warehouses_raw
            if wh_name not in duplicates
        }
        return ret

    @cached_property
    def _warehouse_names(self) -> set[str]:
        return set(self._warehouses.keys())

    @cached_property
    @retry_requests
    def _tables(self) -> dict[str, int]:
        request_kwargs: dict[str, int] = {}
        all_tables: dict[str, int] = {}
        while True:
            result = self.client.tables(**request_kwargs)
            all_tables |= {
                f"{table['warehouse']['name']}.{table['full_name']}": table["id"]
                for table in result
                if table["warehouse"]["name"] in self._warehouse_names
            }
            if "next" not in result.pages:
                break
            request_kwargs = result.pages["next"]
        return all_tables

    def _table_id(self, table_ref: str) -> int:
        return self._table_raw(table_ref)["id"]

    @lru_cache(maxsize=None)
    @retry_requests
    def _table_raw(self, table_ref: str) -> dict[str, Any]:
        warehouse_name, table_name = self._table_ref_parts(table_ref)
        try:
            return self.client.get_table_information(
                warehouse_id=self._warehouses[warehouse_name], table_name=table_name
            )
        except KeyError as e:
            raise TableNotFound(table_ref) from e

    def _table_ref_parts(self, table_ref: str) -> tuple[str, str]:
        try:
            warehouse, schema, table = table_ref.rsplit(".", 2)
        except ValueError as e:
            raise InvalidTableRef(table_ref) from e
        return (warehouse, f"{schema}.{table}")

    def _filter_table_config_response(self, response: dict[str, Any]) -> dict[str, Any]:
        return {
            k: v
            for k, v in response.items()
            if k
            not in {
                "table_id",
                "last_edited_at",
                "last_edited_by",
                "created",
                "created_by",
                "slack_users",
            }
        }

    @lru_cache(maxsize=None)
    @retry_requests
    def _checks_for_table_raw(self, table_ref: str) -> dict[str, Any]:
        return {
            check["ref"]: check
            for check in self.client.get_checks_for_table(
                table_id=self._table_id(table_ref)
            )["checks"]
            if check["ref"]
        }
