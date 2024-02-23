from flask import Flask
from app.utils.api_response import api_response

def test_api_response(test_app):
    with test_app.test_request_context():
        response, status_code = api_response(200,{"hello": "world"},"message")
    
    expected_response = {"hello": "world"}

    assert response.json['data'] == expected_response
    assert status_code == 200
    
def test_api_response_return_400(test_app):
    with test_app.test_request_context():
        response, status_code = api_response(400,{},"not found")
    
    expected_response = {}

    assert response.json['data'] == expected_response
    assert status_code == 400