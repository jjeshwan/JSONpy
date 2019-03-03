Feature: REST API testing framework using REST Assured library
	Raise request(s) using REST Assured library
	Validate HTTP response code and parse JSON response using REST Assured library

Background:
	Given Set basic web application url is "https://jsonplaceholder.typicode.com/"


Scenario: GET request users
  Given Set GET api endpoint as "users"
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200


Scenario: GET request albums
  Given Set GET api endpoint as "albums"
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200