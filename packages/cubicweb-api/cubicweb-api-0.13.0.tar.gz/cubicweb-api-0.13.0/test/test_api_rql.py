# copyright 2023-2024 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact https://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
import json
import webtest

from test.util import ApiBaseTC, check_missing_custom_header_response
from cubicweb import Binary


class ApiRqlTC(ApiBaseTC):
    @property
    def content_type(self):
        return "application/json"

    def get_body(self, queries: list):
        return json.dumps(queries)

    def make_rql_request(self, queries: list[object], status: int = 200):
        return self.webapp.post(
            self.get_api_path("rql"),
            params=self.get_body(queries),
            content_type=self.content_type,
            headers=self.custom_headers,
            status=status,
        ).json

    def test_rql_route(self):
        queries = [
            {
                "query": "Any X Where X is CWUser, X login %(login)s",
                "params": {"login": "anon"},
            }
        ]
        response = self.make_rql_request(queries)
        with self.admin_access.repo_cnx() as cnx:
            rset_as_list = [
                list(
                    cnx.execute(
                        "Any X Where X is CWUser, X login %(login)s", {"login": "anon"}
                    )
                )
            ]

        assert rset_as_list == response

    def test_sending_bad_rql_query_returns_400(self):
        queries = [
            {
                "query": "SET X color 'red' Where X is CWUser",
            }
        ]
        response = self.make_rql_request(queries, 400)

        assert response == {
            "message": 'SET X color "red" WHERE X is CWUser\n** unknown relation `color`',
            "data": None,
            "title": "BadRQLQuery",
        }

    def test_sending_without_params_returns_400(self):
        response = self.webapp.post(
            self.get_api_path("rql"),
            content_type=self.content_type,
            headers=self.custom_headers,
            status=400,
        ).json

        assert response == {
            "data": [
                {
                    "exception": "MissingRequiredRequestBody",
                    "message": "Missing required request body",
                }
            ],
            "message": "Your request could not be validated against the openapi "
            "specification.",
            "title": "OpenApiValidationError",
        }

    def test_401_error_on_rql_when_not_authenticated(self):
        queries = [
            {
                "query": "SET X login 'MYLOGIN' Where X is CWUser",
            }
        ]
        response = self.make_rql_request(queries, 401)

        assert response == {
            "message": "You are not allowed to perform update operation on CWUser",
            "data": None,
            "title": "Unauthorized",
        }

    def test_200_on_rql_when_authenticated(self):
        self.login_request()
        queries = [
            {
                "query": "INSERT CWUser U: U login %(login)s, U upassword 'AZJEJAZO'",
                "params": {"login": "ginger"},
            },
            {
                "query": "INSERT CWGroup G: G name %(name)s",
                "params": {"name": "chickens"},
            },
            {
                "query": "SET U in_group G WHERE U eid %(ginger_eid)s, G eid %(chickens_eid)s",
                "params": {
                    "ginger_eid": {
                        "type": "query_reference",
                        "queryIndex": 0,
                        "row": 0,
                        "column": 0,
                    },
                    "chickens_eid": {
                        "type": "query_reference",
                        "queryIndex": 1,
                        "row": 0,
                        "column": 0,
                    },
                },
            },
        ]
        response = self.make_rql_request(queries)

        assert len(response) == 3
        assert isinstance(response[0][0][0], int)
        assert isinstance(response[1][0][0], int)
        assert isinstance(response[2][0][0], int)
        assert isinstance(response[2][0][1], int)

    def test_rollback_on_error(self):
        self.login_request()
        queries = [
            {
                "query": "INSERT CWUser U: U login %(login)s, U upassword 'AZJEJAZO'",
                "params": {"login": "ginger"},
            },
            {
                "query": "SET U in_group G WHERE U eid 'test'",
                "params": {},
            },
        ]
        response = self.make_rql_request(queries, status=400)

        assert response == {
            "data": None,
            "message": "781 (in_group-subject): at least one relation in_group is "
            "required on CWUser (781)",
            "title": "ValidationError",
        }

        # Check user not added, request should be rolled back
        queries = [
            {
                "query": "Any X WHERE X login %(login)s",
                "params": {"login": "ginger"},
            },
        ]
        response = self.make_rql_request(queries, status=200)

        assert response == [[]]

    def test_400_on_invalid_transactions(self):
        queries = [
            {
                "query": "INSERT CWUser U: U login %(login)s, U upassword 'AZJEJAZO'",
                "params": {
                    "login": {
                        "type": "query_reference",
                        "queryIndex": 0,
                        "row": 0,
                        "column": 0,
                    }
                },
            },
        ]
        response = self.make_rql_request(queries, 400)

        assert response == {
            "message": "A query reference index refers to a request which has not yet "
            "been executed",
            "data": None,
            "title": "InvalidTransaction",
        }

    def test_400_on_invalid_transactions_query_index(self):
        queries = [
            {
                "query": "INSERT CWUser U: U login %(login)s, U upassword 'AZJEJAZO'",
                "params": {
                    "login": {
                        "type": "query_reference",
                        "queryIndex": "not a number",
                        "row": 0,
                        "column": 0,
                    }
                },
            },
        ]
        response = self.make_rql_request(queries, 400)

        assert response == {
            "data": [
                {
                    "exception": "ValidationError",
                    "message": "{'type': 'query_reference', 'queryIndex': 'not a number', "
                    "'row': 0, 'column': 0} is not "
                    "valid under any of the given schemas",
                }
            ],
            "message": "Your request could not be validated against the openapi "
            "specification.",
            "title": "OpenApiValidationError",
        }

    def test_missing_custom_headers_returns_400(self):
        response = self.webapp.post(
            self.get_api_path("rql"),
            status=400,
        ).json
        check_missing_custom_header_response(response)
        response = self.webapp.post(
            self.get_api_path("rql"),
            content_type=self.content_type,
            status=400,
        ).json
        check_missing_custom_header_response(response)
        response = self.webapp.post(
            self.get_api_path("rql"),
            params=self.get_body([{"query": "test", "params": {}}]),
            content_type=self.content_type,
            status=400,
        ).json
        check_missing_custom_header_response(response)


class ApiRqlMultipartTC(ApiRqlTC):
    @property
    def content_type(self):
        return "multipart/form-data"

    def get_body(self, queries: list):
        return {"queries": json.dumps(queries)}

    def make_upload_request(self, params: object, status: int = 200):
        return self.webapp.post(
            self.get_api_path("rql"),
            params=params,
            content_type=self.content_type,
            headers=self.custom_headers,
            status=status,
        ).json

    def test_upload_file(self):
        self.login_request()
        queries = [
            {
                "query": "Insert EntityWithBinary X: X binary %(binary_ref)s",
                "params": {
                    "binary_ref": {"type": "binary_reference", "ref": "test_file"}
                },
            }
        ]
        response = self.make_upload_request(
            {
                "queries": json.dumps(queries),
                "test_file": webtest.Upload("filename.txt", b"content"),
            }
        )
        eid = response[0][0][0]
        with self.admin_access.repo_cnx() as cnx:
            rset = cnx.execute("Any X, B WHERE X eid %(eid)s, X binary B", {"eid": eid})
            binary: Binary = rset[0][1]
            self.assertEqual(binary.read(), b"content")

    def test_upload_file_missing_reference(self):
        self.login_request()
        queries = [
            {
                "query": "Insert EntityWithBinary X: X binary %(binary_ref)s",
                "params": {
                    "binary_ref": {"type": "binary_reference", "ref": "wrong_ref"}
                },
            }
        ]
        response = self.make_upload_request(
            {
                "queries": json.dumps(queries),
                "test_file": webtest.Upload("filename.txt", b"content"),
            },
            400,
        )

        assert response == {
            "message": "Could not find binary of id wrong_ref",
            "data": None,
            "title": "InvalidTransaction",
        }

    def test_upload_file_malformed_reference(self):
        self.login_request()
        queries = [
            {
                "query": "Insert EntityWithBinary X: X binary %(binary_ref)s",
                "params": {
                    "binary_ref": {
                        "type": "binary_reference",
                    }
                },
            }
        ]

        response = self.make_upload_request(
            {
                "queries": json.dumps(queries),
                "test_file": webtest.Upload("filename.txt", b"content"),
            },
            400,
        )

        assert response == {
            "data": [
                {
                    "exception": "ValidationError",
                    "message": "{'type': 'binary_reference'} is valid under each of "
                    "{'additionalProperties': False, 'properties': {'ref': "
                    "{'type': 'string'}, 'type': {'type': 'string'}}, "
                    "'type': 'object'}, {'additionalProperties': False, "
                    "'properties': {'column': {'type': 'number'}, "
                    "'queryIndex': {'type': 'number'}, 'row': {'type': "
                    "'number'}, 'type': {'type': 'string'}}, 'type': "
                    "'object'}",
                }
            ],
            "message": "Your request could not be validated against the openapi "
            "specification.",
            "title": "OpenApiValidationError",
        }
