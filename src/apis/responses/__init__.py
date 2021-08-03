import json

from flask import Response


# Base Responses
# ------------------------------------------------------------------

def _format_response(response, code):
    return Response(
        response=json.dumps(response),
        status=code,
        mimetype='application/json'
    )


def response_success(response):
    return _format_response(response, 200)


def response_failed(response):
    return _format_response(response, 400)
