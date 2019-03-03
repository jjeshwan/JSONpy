#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then
import requests
import json


global_general_variables = {}
http_request_header = {}
http_request_body = {}
http_request_url_query_param = {}


@given(u'Set basic web application url is "{basic_app_url}"')
def step_impl(context, basic_app_url):
    global_general_variables['basic_application_URL'] = basic_app_url


@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type


@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    http_request_header['Accept'] = header_accept_type


@given(u'Set GET api endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    global_general_variables['GET_api_endpoint'] = get_api_endpoint


@when(u'Raise "{http_request_type}" HTTP request')
def step_impl(context, http_request_type):
    url_temp = global_general_variables['basic_application_URL']
    if 'GET' == http_request_type:
        url_temp += global_general_variables['GET_api_endpoint']
        http_request_body.clear()
        global_general_variables['response_full'] = requests.get(url_temp,
                                                                 headers=http_request_header,
                                                                 params=http_request_url_query_param,
                                                                 data=http_request_body)


@then(u'Valid HTTP response should be received')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, 'Null response received'


@then(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    global_general_variables['expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['response_full'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print (str(global_general_variables['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    global_general_variables['expected_response_content_type'] = expected_response_content_type
    actual_response_content_type = global_general_variables['response_full'].headers['Content-Type']
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type


@then(u'Response BODY should not be null or empty')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, '***ERROR:  Null or none response body received'


@then(u'Response time in milliseconds should be less than {expected_response_time:d}')
def step_impl(context, expected_response_time):
    global_general_variables['expected_response_time'] = expected_response_time
    actual_response_time = global_general_variables['response_full'].elapsed.seconds
    if expected_response_time < actual_response_time:
        assert False, '***ERROR: the response time is more than 1: ' + actual_response_time


@then(u'Total Users should be {expected_user_ids:d}')
def step_impl(context, expected_user_ids):
    global_general_variables['expected_user_ids'] = expected_user_ids
    user_json = global_general_variables['response_full'].json()
    user_json_dmps = json.dumps(user_json)
    userdata = json.loads(user_json_dmps)
    for x in range(1, 11):
        if "'id':"+' '+str(x) not in str(userdata):
            assert False, '***ERROR: User id missing is: ' +str(x)


@then(u'Total Albums should be {expected_album_ids:d}')
def step_impl(context, expected_album_ids):
    global_general_variables['expected_album_ids'] = expected_album_ids
    album_json = global_general_variables['response_full'].json()
    album_json_dmps = json.dumps(album_json)
    albumdata = json.loads(album_json_dmps)
    for x in range(1, 101):
        if "'id':"+' '+str(x) not in str(albumdata):
            assert False, '***ERROR: album id missing is: ' +str(x)


@then(u'Each User has published {expected_album_per_user:d} Albums')
def step_impl(context, expected_album_per_user):
    global_general_variables['expected_album_per_user'] = expected_album_per_user
    album_per_user_json = global_general_variables['response_full'].json()
    album_per_user_json_dmps = json.dumps(album_per_user_json)
    apudata = json.loads(album_per_user_json_dmps)
    store_list = []
    for item in apudata:
        store_details = {"userId": None, "id": None}
        store_details['userId'] = item['userId']
        store_details['id'] = item['id']
        store_list.append(store_details)

    for x in range(1, 10):
        if x == 1:
            for y in range(0, 9):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)
        elif x == 2:
            for y in range(10, 19):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)
        elif x == 3:
            for y in range(20, 29):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)
        elif x == 4:
            for y in range(30, 39):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)
        elif x == 5:
            for y in range(40, 49):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)
        elif x == 6:
            for y in range(50, 59):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)
        elif x == 7:
            for y in range(60, 69):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)
        elif x == 8:
            for y in range(70, 79):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)
        elif x == 9:
            for y in range(80, 89):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)
        elif x == 10:
            for y in range(90, 99):
                if "'userId':" + ' ' + str(x) not in str(store_list[y]):
                    assert False, '***ERROR: 10 albums are not published by userId: ' + str(x)

