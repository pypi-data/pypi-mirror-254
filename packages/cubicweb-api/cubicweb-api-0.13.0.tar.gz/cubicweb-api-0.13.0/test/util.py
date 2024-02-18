import json
from typing import Optional

from cubicweb.pyramid.test import PyramidCWTest

from cubicweb_api.constants import API_PATH_DEFAULT_PREFIX

# Don't use cubicweb.devtools.BASE_URL because pyramid routes in CubicWeb < 4.x
# are mounted on the domain root instead of /cubicweb
BASE_URL = "https://testing.cubicweb/"


def check_missing_custom_header_response(response, index_in_data: Optional[int] = 0):
    assert response["data"][index_in_data]["exception"] == "MissingRequiredParameter"
    assert response["data"][index_in_data]["field"] == "X-Client-Name"


class ApiBaseTC(PyramidCWTest):
    settings = {
        "cubicweb.includes": ["cubicweb.pyramid.auth"],
        "cubicweb_api.enable_login_route": "yes",
    }
    custom_headers = {"X-Client-Name": "Pytest"}

    @classmethod
    def init_config(cls, config):
        super().init_config(config)
        config.global_set_option("base-url", BASE_URL)

    @classmethod
    def get_api_path(cls, endpoint: str):
        return f"{BASE_URL[:-1]}{API_PATH_DEFAULT_PREFIX}/v1/{endpoint}"

    def login_request(self):
        self.webapp.post(
            self.get_api_path("login"),
            params=json.dumps({"login": self.admlogin, "password": self.admpassword}),
            content_type="application/json",
            headers=self.custom_headers,
            status=204,
        )
