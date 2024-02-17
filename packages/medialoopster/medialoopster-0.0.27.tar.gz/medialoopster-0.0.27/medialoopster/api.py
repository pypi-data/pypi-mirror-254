import time
import logging
from enum import Enum
from typing import List
from urllib.parse import urlparse, parse_qs, urljoin, urlencode

from requests import Session
from requests.exceptions import RequestException
from requests.auth import HTTPBasicAuth
from pydantic import HttpUrl

from medialoopster.model import Production

logger = logging.getLogger(__name__)


class Medialoopster:
    class AssetType(str, Enum):
        videoassets = "videoassets"
        imageassets = "imageassets"
        audioassets = "audioassets"
        projectassets = "projectassets"

    def __init__(self, url: str, user: str = None, password: str = None, verify: bool = False):
        self.session = Session()
        self.session.verify = verify

        if all([user, password]):
            self.session.auth = HTTPBasicAuth(user, password)

        self.url = url

    def __enter__(self):
        """Enable context management."""
        return self

    def __exit__(self, *args):
        """Clean up."""
        self.session.close()

    def _build_url(
            self,
            url: HttpUrl | None = None,
            path: str | None = None,
            params: dict | None = None
    ) -> HttpUrl:
        url = url if url else self.url
        url = f"{url}/" if not url.endswith('/') else url
        url = urljoin(url, url=f"{path}/") if path else url
        parsed_url = urlparse(url)

        query_params = parse_qs(parsed_url.query)
        query_params = query_params | params if params else query_params
        query = urlencode(query_params, doseq=True)

        return HttpUrl(urljoin(url, url=f"{parsed_url.path}?{query}"))

    def ping(self):
        try:
            response = self.session.get(f"{self.url}ping/")
            response.raise_for_status()
        except RequestException:
            return False

        return True

    def asset_import(
            self,
            production=None,
            asset_type=None,
            move_asset=False,
            name=None,
            description=None,
            approval=0,
            path_file=None,
            meta_field_store=None
    ):
        if meta_field_store is None:
            meta_field_store = {}

        request = {
            "production": production,
            "type": asset_type,
            "move_asset": move_asset,
            "asset": {
                "asset_meta": {
                    "name": name,
                    "description": description,
                    "approval": approval,
                    "path_file": path_file,
                    "meta_field_store": meta_field_store
                }
            }
        }

        response = self.session.post(f"{self.url}asset/import/", json=request)
        response.raise_for_status()

        response_json = response.json()

        return response_json.get("asset_import_id", None)

    def get_from_api(
            self,
            path="videoassets",
            url=None,
            production_id=None,
            with_sequences=True,
            is_archive=None
    ):
        if url is None:
            url_params = {}

            if path == "videoassets" and with_sequences is True:
                url_params["with_sequences"] = "true"
            if is_archive is not None:
                url_params["is_archive"] = "true" if is_archive else "false"
            if production_id is not None:
                url_params["production"] = production_id

            url = self._build_url(path=path, params=url_params)

        while url:
            try:
                response = self.session.get(url=url)
                response.raise_for_status()
            except RequestException:
                continue

            if response.links is not None:
                url = response.links.get("next", {}).get("url", None)
            else:
                url = None

            yield from response.json()

    def get_videoassets(self, production_id=None, with_sequences=True, is_archive=None):
        return self.get_from_api(
            path="videoassets",
            production_id=production_id,
            with_sequences=with_sequences,
            is_archive=is_archive
        )

    def get_videoassets_count(self):
        response = self.session.get(f"{self.url}videoassets")
        response.raise_for_status()

        return response.headers.get("X-Total-Count")

    def get_videoasset_sequences(self, asset_id):
        url = f"{self.url}videoassets/{asset_id}/sequences/"

        response = self.session.get(url=url)
        response.raise_for_status()

        return response.json()

    def get_videoasset_shots(self, asset_id):
        url = f"{self.url}videoassets/{asset_id}/shots/"

        response = self.session.get(url=url)
        response.raise_for_status()

        return response.json()

    def get_asset(self, asset_id=None, asset_type="videoassets", with_sequences=True, path_file=None):
        if asset_id is not None:
            url = f"{self.url}{asset_type}/{asset_id}/"

            if asset_type == "videoassets" and with_sequences is True:
                url = f"{url}?with_sequences=true"
        elif path_file is not None:
            url = f"{self.url}{asset_type}/?path_file={path_file}"

        response = self.session.get(url=url)
        response.raise_for_status()

        return response.json()

    def search_meta_field_store(self, field: str = None, value: str = None, asset_type: str = "videoassets"):
        assets = []

        for asset in self.get_from_api(path=asset_type):
            meta_field_store = asset.get("meta_field_store")
            if meta_field_store is not None:
                field_value = meta_field_store.get(field)
                if field_value is not None and field_value == value:
                    print(asset.get("id"))
                    assets.append(asset.get("id"))

        return assets

    def archiv_asset(self, content_type_id, asset_id, archive_type, archive_connector):
        url = urljoin(self.url, url="archiveactivities/")

        request = [{
            "content_type_id": content_type_id,
            "asset_id": asset_id,
            "archive_type": archive_type,
            "archive_connector": archive_connector,
        }]

        response = self.session.post(url, json=request)
        response.raise_for_status()

        return response.json()

    def restore_asset(self, content_type_id, asset_id):
        url = urljoin(self.url, url="restoreactivities/")

        request = [{
            "content_type_id": content_type_id,
            "asset_id": asset_id,
        }]

        response = self.session.post(url, json=request)
        response.raise_for_status()

        return response.json()

    def wait_is_production(self, asset_id, timeout=3600, sleep=30):
        timeout = time.time() + timeout  # timeout in seconds from now
        is_production = False

        while time.time() < timeout:
            try:
                asset = self.get_asset(asset_id=asset_id, with_sequences=False)
                is_production = asset.get("is_production")

                if is_production:
                    break
            except Exception:
                logger.exception("Error in wait_is_production")

            time.sleep(sleep)  # sleep in seconds

        return is_production

    def disapprove_asset(self, asset_id, asset_type="videoassets"):
        url = f"{self.url}{asset_type}/{asset_id}/"

        request = {
            "status_approval": 0
        }

        response = self.session.patch(url, json=request)
        response.raise_for_status()

        return response.json()

    def set_date_del_asset(self, asset_id, date_del, asset_type="videoassets"):
        url = f"{self.url}{asset_type}/{asset_id}/"

        request = {
            "date_del": date_del
        }

        response = self.session.patch(url, json=request)
        response.raise_for_status()

        return response.json()

    def set_date_add_asset(self, asset_id, date_add, asset_type="videoassets"):
        url = f"{self.url}{asset_type}/{asset_id}/"

        request = {
            "date_add": date_add
        }

        response = self.session.patch(url, json=request)
        response.raise_for_status()

        return response.json()

    def edit_meta_field_store(self, asset_id, meta_field_store, asset_type="videoassets"):
        url = f"{self.url}{asset_type}/{asset_id}/"

        request = {
            "meta_field_store": meta_field_store
        }

        response = self.session.patch(url, json=request)
        response.raise_for_status()

        return response.json()

    def productions(self) -> List[Production]:
        url = urljoin(self.url, url="productions/")

        response = self.session.get(url)
        response.raise_for_status()

        return [Production(**production) for production in response.json()]

    def production(self, production_id: int | None = None, production_name: str | None = None) -> Production:
        if production_id is not None:
            url = urljoin(self.url, url=f"productions/{production_id}/")

            response = self.session.get(url)
            response.raise_for_status()

            return Production(**response.json())
        elif production_name is not None:
            productions = self.productions()
            return next((production for production in productions if production.name == production_name), None)
