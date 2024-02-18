from marshmallow import Schema, fields
from http import HTTPStatus


def openapi_route(route, blueprint):
    def testResponseApi(fn):
        _data = data.get(route, {})

        # Doc decorator parameters
        doc_params = {
            "description": _data.get("desc"),
            "summary": _data.get("sum"),
            "security": _data.get("security", None),
        }
        not_none_doc_params = {k: v for k, v in doc_params.items() if v is not None}

        # Response decorator parameters
        response_params = {
            "schema": _data.get("schema", None),
            "example": _data.get("example", None),
        }
        not_none_response_params = {
            k: v for k, v in response_params.items() if v is not None
        }

        # Endpoint without documented endpoint
        if not_none_response_params == {}:

            @blueprint.route(route, methods=_data.get("methods", ["GET"]))
            @blueprint.doc(**not_none_doc_params)
            def wrapper(**kwargs):
                nonlocal fn
                return fn(**kwargs)

            return wrapper
        # Endpoint with documented endpoint
        else:

            @blueprint.route(route, methods=_data.get("methods", ["GET"]))
            @blueprint.doc(**not_none_doc_params)
            @blueprint.response(
                _data.get("status", HTTPStatus.OK), **not_none_response_params
            )
            def wrapper(**kwargs):
                nonlocal fn
                return fn(**kwargs)

            return wrapper

    return testResponseApi


# -------------------------------------------------------------------------
# String/JSON - actualy used when procesing a response


# /verify/<string:consent_id>
class consent_attrs_schema(Schema):
    # consent.attributes fields
    pass


# /ban/<string:ba_id>
# /AuthenticateKerberosTicket
class string_schema(Schema):
    _text = fields.String()


# /users/me/consents
class consent_schema(Schema):
    user_id = fields.String()
    requester = fields.String()
    attributes = fields.Dict()
    months_valid = fields.String()
    timestamp = fields.String()


class user_consents_schema(Schema):
    consents = fields.List(fields.Nested(consent_schema))


# /users/me/consents/<string:consent_id>
class delete_consent_schema(Schema):
    deleted = fields.Boolean()
    message = fields.String()


# -------------------------------------------------------------------------
# Schemas for Response type return value (Response, redirect, ...)
# only for API purpose


# /banned-users-generic/
# /banned-users/
class response_schema(Schema):
    response = fields.String(load_default="flask.Response class is returned")


# /save_consent
class redirect_schema(Schema):
    response = fields.String(
        load_default="flask.Response class via redirect is returned"
    )


data = {
    # ------------- Kerberos -------------------------------------------------
    "/AuthenticateKerberosTicket": {
        "desc": "AuthenticateKerberosTicket description",
        "sum": "AuthenticateKerberosTicket summary",
        "security": [{"NegotiateAuth": []}],
        "status": HTTPStatus.UNAUTHORIZED,
        "example": {"_text": "Kerberos authentication successful"},
        "schema": string_schema,
    },
    # ------------ Backchannel logout -----------------------------------------
    "/backchannel-logout": {
        "methods": ["POST"],
        "desc": "Page for Backchannel logout.",
        "sum": "Performs OIDC Back-Channel Logout 1.0 in the role of RP.",
        "status": HTTPStatus.NO_CONTENT,
        "schema": response_schema,
    },
    # ------------ Consent API ------------------------------------------------
    "/verify/<string:consent_id>": {
        "desc": "page",
        "sum": "verify",
        "status": HTTPStatus.OK,
        # "schema": consent_attrs_schema,
    },
    "/creq/<string:jwt>": {
        "methods": ["GET", "POST"],
        "desc": "creq-page",
        "sum": "creq",
        "security": [{"bearerAuthJWT": []}],
        # "schema": consent_attr_schema
    },
    "/save_consent": {
        "desc": "save_consent_page",
        "sum": "save_consent",
        "status": 302,
        "schema": redirect_schema,
    },
    "/users/me/consents": {
        "methods": ["GET"],
        "desc": "Returns list of Consent objects",
        "sum": "consents",
        "security": [{"oAuthScheme": []}],
        "status": HTTPStatus.OK,
        "schema": user_consents_schema,
    },
    "/users/me/consents/<string:consent_id>": {
        "methods": ["DELETE"],
        "desc": "page",
        "sum": "delete_consents",
        "security": [{"oAuthScheme": []}],
        "status": HTTPStatus.OK,
        "schema": delete_consent_schema,
    },
    # ------------ Ban API --------------------------------------------------
    "/banned-users/": {
        "methods": ["PUT"],
        "desc": "page",
        "sum": "update_banned_users",
        "status": HTTPStatus.NO_CONTENT,
        "schema": response_schema,
    },
    "/banned-users-generic/": {
        "methods": ["PUT"],
        "desc": "page",
        "sum": "update_banned_users_generic",
        "status": HTTPStatus.NO_CONTENT,
        "schema": response_schema,
    },
    "/ban/<string:ban_id>": {
        "methods": ["GET"],
        "desc": "page",
        "sum": "find_ban",
        "status": HTTPStatus.OK,
        "example": {"_text": "Found ban dictionary"},
        "schema": string_schema,
    },
}
