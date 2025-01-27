*** Settings ***
Resource    /opt/robot-tests/tests/resources/common.resource
Library     /opt/robot-tests/tests/libraries/api_publish_service/bodyRequests.py
Resource    /opt/robot-tests/tests/resources/common/basicRequests.robot

Test Setup    Initialize Test And Register    role=apf    db_col=serviceapidescriptions

*** Variables ***
${APF_ID_NOT_VALID}            apf-example
${SERVICE_API_ID_NOT_VALID}    not-valid

*** Keywords ***


*** Test Cases ***
Publish API by Authorised API Publisher
	[Tags]    capif_api_publish_service-1

	${request_body}=    Create Service Api Description
	${resp}=            Post Request Capif                /published-apis/v1/${APF_ID}/service-apis    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    201

Publish API by NON Authorised API Publisher
	[Tags]     capif_api_publish_service-2
	[Setup]    Initialize Test And Register    role=invoker    db_col=serviceapidescriptions

	${request_body}=    Create Service Api Description
	${resp}=            Post Request Capif                /published-apis/v1/${APF_ID_NOT_VALID}/service-apis    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    401

Retrieve all APIs Published by Authorised apfId
	[Tags]    capif_api_publish_service-3

	${request_body}=    Create Service Api Description
	${resp}=            Post Request Capif                /published-apis/v1/${APF_ID}/service-apis    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    201

	${request_body}=    Create Service Api Description    other_service
	${resp}=            Post Request Capif                /published-apis/v1/${APF_ID}/service-apis    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    201

	${resp}=    Get Request Capif    /published-apis/v1/${APF_ID}/service-apis

	Should Be Equal As Strings    ${resp.status_code}    200

	Log    ${resp.json()}

Retrieve all APIs Published by NON Authorised apfId
	[Tags]     capif_api_publish_service-4
	[Setup]    Initialize Test And Register    role=invoker    db_col=serviceapidescriptions

	${resp}=    Get Request Capif    /published-apis/v1/${APF_ID_NOT_VALID}/service-apis

	Should Be Equal As Strings    ${resp.status_code}    401

	Log    ${resp.json()}

Retrieve single APIs Published by Authorised apfId
	[Tags]    capif_api_publish_service-5

	${request_body}=    Create Service Api Description    first_service
	${resp}=            Post Request Capif                /published-apis/v1/${APF_ID}/service-apis    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    201
	${serviceApiId1}=             Set Variable           ${resp.json()['apiId']}

	${request_body}=    Create Service Api Description    other_service
	${resp}=            Post Request Capif                /published-apis/v1/${APF_ID}/service-apis    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    201

	${serviceApiId2}=    Set Variable    ${resp.json()['apiId']}

	${resp}=    Get Request Capif    /published-apis/v1/${APF_ID}/service-apis/${serviceApiId1}

	Should Be Equal As Strings    ${resp.status_code}    200

	Should Be Equal    ${resp.json()['api_name']}    first_service

	${resp}=    Get Request Capif    /published-apis/v1/${APF_ID}/service-apis/${serviceApiId2}

	Should Be Equal As Strings    ${resp.status_code}    200

	Should Be Equal    ${resp.json()['api_name']}    other_service

Retrieve single APIs non Published by Authorised apfId
	[Tags]    capif_api_publish_service-6

	${resp}=    Get Request Capif    /published-apis/v1/${APF_ID}/service-apis/${SERVICE_API_ID_NOT_VALID}

	Should Be Equal As Strings    ${resp.status_code}    404

	Log    ${resp.json()}

Retrieve single APIs Published by NON Authorised apfId
	[Tags]     capif_api_publish_service-7
	[Setup]    Initialize Test And Register    role=invoker    db_col=serviceapidescriptions

	${resp}=    Get Request Capif    /published-apis/v1/${APF_ID}/service-apis/${SERVICE_API_ID_NOT_VALID}

	Should Be Equal As Strings    ${resp.status_code}    401

	Log    ${resp.json()}

Update API Published by Authorised apfId with valid serviceApiId
	[Tags]    capif_api_publish_service-8

	${request_body}=    Create Service Api Description    first_service
	${resp}=            Post Request Capif                /published-apis/v1/${APF_ID}/service-apis    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    201
	${serviceApiId1}=             Set Variable           ${resp.json()['apiId']}
	${url}=                       Parse Url              ${resp.headers['Location']}

	${request_body}=    Create Service Api Description    first_service_modified

	${resp}=    Put Request Capif    ${url.path}    ${request_body}    server=${NGINX_HOSTNAME}

	Should Be Equal As Strings    ${resp.status_code}    200

Update APIs Published by Authorised apfId with invalid serviceApiId
	[Tags]    capif_api_publish_service-9

	${request_body}=    Create Service Api Description    first_service_modified

	${resp}=    Put Request Capif    /published-apis/v1/${APF_ID}/service-apis/${SERVICE_API_ID_NOT_VALID}    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    404

Update APIs Published by NON Authorised apfId
	[Tags]    capif_api_publish_service-10

	${request_body}=    Create Service Api Description    first_service
	${resp}=            Post Request Capif                /published-apis/v1/${APF_ID}/service-apis    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    201
	${serviceApiId1}=             Set Variable           ${resp.json()['apiId']}
	${url}=                       Parse Url              ${resp.headers['Location']}

	Register User At Jwt Auth    username=robot2    role=invoker

	${request_body}=    Create Service Api Description    first_service_modified

	${resp}=    Put Request Capif    ${url.path}    ${request_body}    server=${NGINX_HOSTNAME}

	Should Be Equal As Strings    ${resp.status_code}    401

Delete API Published by Authorised apfId with valid serviceApiId
	[Tags]    capif_api_publish_service-11

	${request_body}=    Create Service Api Description    first_service
	${resp}=            Post Request Capif                /published-apis/v1/${APF_ID}/service-apis    ${request_body}

	Should Be Equal As Strings    ${resp.status_code}    201
	${serviceApiId1}=             Set Variable           ${resp.json()['apiId']}
	${url}=                       Parse Url              ${resp.headers['Location']}

	${resp}=    Delete Request Capif    ${url.path}    server=${NGINX_HOSTNAME}

	Should Be Equal As Strings    ${resp.status_code}    204

Delete APIs Published by Authorised apfId with invalid serviceApiId
	[Tags]    capif_api_publish_service-12

	${resp}=    Delete Request Capif    /published-apis/v1/${APF_ID}/service-apis/${SERVICE_API_ID_NOT_VALID}

	Should Be Equal As Strings    ${resp.status_code}    404

Delete APIs Published by NON Authorised apfId
	[Tags]     capif_api_publish_service-13
	[Setup]    Initialize Test And Register    role=invoker    db_col=serviceapidescriptions

	${resp}=    Delete Request Capif    /published-apis/v1/${APF_ID}/service-apis/${SERVICE_API_ID_NOT_VALID}

	Should Be Equal As Strings    ${resp.status_code}    401


