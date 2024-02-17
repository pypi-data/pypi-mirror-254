import requests

from lapa_database_helper.configuration import (
    config_int_lapa_database_port,
    config_str_lapa_database_ip,
    config_str_lapa_database_protocol,
)


class LAPADatabaseHelper:
    def __init__(self):
        try:
            self.global_str_lapa_database_url_base = (
                f"{config_str_lapa_database_protocol}://"
                f"{config_str_lapa_database_ip}:{config_int_lapa_database_port}"
            )
        except Exception:
            raise

    def _make_request(self, method, endpoint, data=None):
        try:
            url = f"{self.global_str_lapa_database_url_base}/{endpoint}"
            response = requests.request(method, url, json=data)
            response.raise_for_status()
            return response.json()
        except Exception:
            raise

    def insert_rows(
        self, data: list[dict], database_name: str, schema_name: str, table_name: str
    ):
        try:
            endpoint = "insert_rows"
            payload = {
                "data": data,
                "database_name": database_name,
                "schema_name": schema_name,
                "table_name": table_name,
            }
            return self._make_request("POST", endpoint, payload)
        except Exception:
            raise

    def get_rows(
        self,
        filters: dict,
        database_name: str,
        schema_name: str,
        table_name: str,
        ignore_filters_and_get_all: bool = False,
    ):
        try:
            endpoint = "get_rows"
            payload = {
                "filters": filters,
                "database_name": database_name,
                "schema_name": schema_name,
                "table_name": table_name,
                "ignore_filters_and_get_all": ignore_filters_and_get_all,
            }
            return self._make_request("POST", endpoint, payload)
        except Exception:
            raise

    def edit_rows(
        self,
        data: dict,
        filters: dict,
        database_name: str,
        schema_name: str,
        table_name: str,
        ignore_filters_and_edit_all: bool = False,
    ):
        try:
            endpoint = "edit_rows"
            payload = {
                "data": data,
                "filters": filters,
                "database_name": database_name,
                "schema_name": schema_name,
                "table_name": table_name,
                "ignore_filters_and_edit_all": ignore_filters_and_edit_all,
            }
            return self._make_request("PUT", endpoint, payload)
        except Exception:
            raise

    def delete_rows(
        self,
        filters: dict,
        database_name: str,
        schema_name: str,
        table_name: str,
        ignore_filters_and_delete_all: bool = False,
    ):
        try:
            endpoint = "delete_rows"
            payload = {
                "filters": filters,
                "database_name": database_name,
                "schema_name": schema_name,
                "table_name": table_name,
                "ignore_filters_and_delete_all": ignore_filters_and_delete_all,
            }
            return self._make_request("DELETE", endpoint, payload)
        except Exception:
            raise
