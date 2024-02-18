from __future__ import annotations

import json
import os
from typing import Any
from urllib.parse import urlparse

import requests

from .result import Result


class Client:
    output_style = "json"

    def __init__(
        self,
        api_token=None,
        host=None,
        proto=None,
        ssl_cert_verify=None,
        output_style=None,
        legacy_auth: bool = True,
    ):
        if output_style:
            self.output_style = output_style
        self.host = host if host else os.environ.get("ANOMALO_INSTANCE_HOST")
        self.api_token = (
            api_token if api_token else os.environ.get("ANOMALO_API_SECRET_TOKEN")
        )

        if not self.host:
            raise RuntimeError(
                "Please specify Anomalo instance host via ANOMALO_INSTANCE_HOST env var"
            )
        if not self.api_token:
            raise RuntimeError(
                "Please specify Anomalo api token via ANOMALO_API_SECRET_TOKEN env var"
            )

        parsed_host_url = urlparse(self.host)
        host_scheme = parsed_host_url.scheme
        if host_scheme:
            self.proto = host_scheme
            self.host = parsed_host_url.netloc
        else:
            self.proto = proto if proto else "https"

        self.request_headers = (
            {"X-Anomalo-Token": self.api_token}
            if legacy_auth
            else {"Authorization": f"Bearer {self.api_token}"}
        )

        self.verify = ssl_cert_verify

    def _api_call(self, endpoint, method="GET", empty_response=False, **kwargs) -> Any:
        endpoint_url = "{proto}://{host}/api/public/v1/{endpoint}".format(
            proto=self.proto, host=self.host, endpoint=endpoint
        )

        if method in ["PUT", "POST", "PATCH", "DELETE"]:
            request_args = dict(json=kwargs)
        else:
            request_args = dict(params=kwargs)

        r = requests.request(
            method,
            endpoint_url,
            headers=self.request_headers,
            verify=self.verify,
            allow_redirects=False,
            **request_args,
        )

        if not r.ok:
            raise RuntimeError(r.text)
        if empty_response:
            return r
        return Result.from_raw(r, self.output_style)

    def ping(self):
        return self._api_call("ping")

    def get_active_organization_id(self):
        res = self._api_call("organization")
        if self.output_style != "json":
            res = json.loads(res)
        return res.get("id")

    def set_active_organization_id(self, organization_id):
        res = self._api_call("organization", method="PUT", id=organization_id)
        if self.output_style != "json":
            res = json.loads(res)
        return res.get("id")

    def get_all_organizations(self):
        return self._api_call("organizations")

    def create_organization(self, name: str):
        return self._api_call("deployment/organization", method="POST", name=name)

    def list_warehouses(self):
        return self._api_call("list_warehouses")

    def get_warehouse(self, warehouse_id: int):
        return self._api_call(f"warehouse/{warehouse_id}")

    def create_warehouse(
        self, name: str, warehouse_type: str, connection: dict[str, Any]
    ):
        return self._api_call(
            "warehouse",
            name=name,
            warehouse_type=warehouse_type,
            connection=connection,
            method="POST",
        )

    def update_warehouse(
        self, warehouse_id: int, name: str, connection: dict[str, Any]
    ):
        return self._api_call(
            f"warehouse/{warehouse_id}", name=name, connection=connection, method="PUT"
        )

    def delete_warehouse(self, warehouse_id: int):
        self._api_call(
            f"warehouse/{warehouse_id}", method="DELETE", empty_response=True
        )

    def refresh_warehouse(self, warehouse_id):
        return self._api_call(f"warehouse/{warehouse_id}/refresh", method="PUT")

    def refresh_warehouse_tables(self, warehouse_id, table_full_names):
        if not table_full_names:
            raise RuntimeError("Must specify a list of full table names to sync")
        return self._api_call(
            f"warehouse/{warehouse_id}/refresh",
            method="PUT",
            table_full_names=table_full_names,
        )

    def refresh_warehouse_new_tables(self, warehouse_id):
        return self._api_call(f"warehouse/{warehouse_id}/refresh/new", method="PUT")

    def list_notification_channels(self):
        return self._api_call("list_notification_channels")

    def configured_tables(
        self,
        check_cadence_type: str | None = None,
        warehouse_id: int | None = None,
        details: bool = True,
        limit: int = 0,
        offset: int = 0,
    ):
        return self._api_call(
            "configured_tables",
            check_cadence_type=check_cadence_type,
            warehouse_id=warehouse_id,
            details=details,
            limit=limit,
            offset=offset,
        )

    def tables(self, limit: int = 0, offset: int = 0):
        return self._api_call("tables", limit=limit, offset=offset)

    def filter_tables_by_label(self, label_id):
        return self._api_call(f"tables?label_id={label_id}")

    def get_table_information(self, warehouse_id=None, table_id=None, table_name=None):
        if (not table_id or not warehouse_id) and not table_name:
            raise RuntimeError(
                "Must specify either warehouse_id & table_id or a full table_name for get_table_information"
            )
        else:
            return self._api_call(
                "get_table_information",
                warehouse_id=warehouse_id,
                table_id=table_id,
                table_name=table_name,
            )

    def get_table_profile(self, warehouse_id=None, table_id=None, table_name=None):
        if (not table_id or not warehouse_id) and not table_name:
            raise RuntimeError(
                "Must specify either warehouse_id & table_id or a full table_name for get_table_profile"
            )
        else:
            return self._api_call(
                "get_table_profile",
                warehouse_id=warehouse_id,
                table_id=table_id,
                table_name=table_name,
            )

    def get_check_intervals(self, table_id=None, start=None, end=None):
        if not table_id:
            raise RuntimeError("Must specify a table_id for get_check_intervals")
        else:
            results = []
            page = 0
            paged_results = None
            while paged_results is None or len(paged_results) > 0:
                paged_results = self._api_call(
                    "get_check_intervals",
                    table_id=table_id,
                    start=start,
                    end=end,
                    page=page,
                )["intervals"]
                results.extend(paged_results)
                page = page + 1
            return results

    def get_checks_for_table(self, table_id):
        return self._api_call("get_checks_for_table", table_id=table_id)

    def run_checks(
        self,
        table_id,
        interval_id=None,
        check_ids=None,
        force=False,
        respect_data_freshness_gate=False,
    ):
        if check_ids:
            if not isinstance(check_ids, list) and not isinstance(check_ids, tuple):
                check_ids = [check_ids]
            check_ids = list(check_ids)  # Convert from Tuple
            return self._api_call(
                "run_checks",
                method="POST",
                table_id=table_id,
                interval_id=interval_id,
                check_ids=check_ids,
                force=force,
                respect_data_freshness_gate=respect_data_freshness_gate,
            )
        else:
            return self._api_call(
                "run_checks",
                method="POST",
                table_id=table_id,
                interval_id=interval_id,
                force=force,
                respect_data_freshness_gate=respect_data_freshness_gate,
            )

    def get_run_result(self, job_id):
        return self._api_call("get_run_result", run_checks_job_id=job_id)

    def get_run_result_triage_history(self, job_id):
        return self._api_call("get_run_result_triage_history", run_checks_job_id=job_id)

    def create_check(self, table_id, check_type, **params):
        return self._api_call(
            "create_check",
            table_id=table_id,
            check_type=check_type,
            method="POST",
            params=params,
        )

    def delete_check(self, table_id, check_id):
        return self._api_call(
            "delete_check",
            table_id=table_id,
            check_id=check_id,
            method="POST",
        )

    def clone_check(self, table_id, check_id, new_table_id):
        return self._api_call(
            "clone_check",
            table_id=table_id,
            check_id=check_id,
            new_table_id=new_table_id,
            method="POST",
        )

    def configure_table(
        self,
        table_id,
        *,
        check_cadence_type=None,
        definition=None,
        time_column_type=None,
        notify_after=None,
        time_columns=None,
        fresh_after=None,
        interval_skip_expr=None,
        notification_channel_id=None,
        slack_users=None,
        check_cadence_run_at_duration=None,
        always_alert_on_errors=False,
    ):
        time_columns = [] if time_columns is None else time_columns
        slack_users = {} if slack_users is None else slack_users

        return self._api_call(
            "configure_table",
            table_id=table_id,
            method="POST",
            check_cadence_type=check_cadence_type,
            definition=definition,
            time_column_type=time_column_type,
            notify_after=notify_after,
            notification_channel_id=notification_channel_id,
            time_columns=time_columns,
            fresh_after=fresh_after,
            interval_skip_expr=interval_skip_expr,
            slack_users=slack_users,
            check_cadence_run_at_duration=check_cadence_run_at_duration,
            always_alert_on_errors=always_alert_on_errors,
        )

    # deprecated
    def create_table_label_for_organization(self, name):
        return self.create_label_for_organization(name)

    # deprecated
    def list_table_labels_for_organization(self):
        return self.list_labels_for_organization()

    # deprecated
    def update_table_label_name_for_organization(self, label_id, new_name):
        return self.update_label_name_for_organization(label_id, new_name)

    # deprecated
    def delete_table_label_for_organization(self, label_id):
        self.delete_label_for_organization(label_id)

    # deprecated
    def merge_table_labels_for_organization(
        self, source_label_id, destination_label_id
    ):
        return self.merge_labels_for_organization(source_label_id, destination_label_id)

    def create_label_for_organization(self, name, scope=None):
        if scope is None:
            scope = "everywhere"
        return self._api_call(
            "org_labels",
            method="POST",
            name=name,
            scope=scope,
        )

    def list_labels_for_organization(self, scope=None):
        if scope:
            return self._api_call(f"org_labels?scope={scope}")
        return self._api_call("org_labels")

    def update_label_name_for_organization(self, label_id, new_name):
        return self._api_call(
            f"org_labels/{label_id}",
            method="PATCH",
            name=new_name,
        )

    def update_label_scope_for_organization(self, label_id, new_scope):
        return self._api_call(
            f"org_labels/{label_id}",
            method="PATCH",
            scope=new_scope,
        )

    def delete_label_for_organization(self, label_id):
        self._api_call(
            f"org_labels/{label_id}",
            method="DELETE",
            empty_response=True,
        )

    def merge_labels_for_organization(self, source_label_id, destination_label_id):
        return self._api_call(
            f"org_labels/{destination_label_id}/merge",
            method="POST",
            source_label_id=source_label_id,
        )

    def replace_labels_for_check(self, check_id, labels, table_id=None):
        if not table_id:
            return self._api_call(
                f"checks/{check_id}/labels",
                method="PUT",
                empty_response=True,
                labels=labels,
            )
        return self._api_call(
            f"checks/{check_id}/labels",
            method="PUT",
            empty_response=True,
            labels=labels,
            table_id=table_id,
        )

    def add_new_labels_to_check(self, check_id, labels, table_id=None):
        if not table_id:
            return self._api_call(
                f"checks/{check_id}/labels",
                method="PATCH",
                empty_response=True,
                labels=labels,
            )
        return self._api_call(
            f"checks/{check_id}/labels",
            method="PATCH",
            empty_response=True,
            labels=labels,
            table_id=table_id,
        )

    def replace_labels_for_table(self, table_id, labels):
        return self._api_call(
            f"tables/{table_id}/labels",
            method="PUT",
            empty_response=True,
            labels=labels,
        )

    def add_new_labels_to_table(self, table_id, labels):
        return self._api_call(
            f"tables/{table_id}/labels",
            method="PATCH",
            empty_response=True,
            labels=labels,
        )

    def add_new_user(self, name, email, role, is_service_account=False):
        return self._api_call(
            "users",
            name=name,
            email=email,
            role=role,
            is_service_account=is_service_account,
            method="POST",
        )

    def list_users(self, limit=None, offset=None, without_access_groups=False):
        return self._api_call(
            "users",
            limit=limit,
            offset=offset,
            without_access_groups=without_access_groups,
            method="GET",
        )

    def get_user(self, user_id):
        return self._api_call(
            f"users/{user_id}",
            method="GET",
        )

    def list_user_access_groups(self, user_id, limit=None, offset=None):
        return self._api_call(
            f"users/{user_id}/access_groups",
            limit=limit,
            offset=offset,
            method="GET",
        )

    def list_tables_from_user_access_groups(self, user_id, limit=None, offset=None):
        return self._api_call(
            f"users/{user_id}/access_groups/tables",
            limit=limit,
            offset=offset,
            method="GET",
        )

    def list_user_api_keys(self, user_id, limit=None, offset=None):
        return self._api_call(
            f"users/{user_id}/api-keys",
            limit=limit,
            offset=offset,
            method="GET",
        )

    def add_user_api_key(self, user_id, description, expires):
        return self._api_call(
            f"users/{user_id}/api-keys",
            description=description,
            expires=expires,
            method="POST",
        )

    def revoke_user_api_key(self, user_id, api_key_id):
        self._api_call(
            f"users/{user_id}/api-keys/{api_key_id}",
            method="DELETE",
            empty_response=True,
        )
