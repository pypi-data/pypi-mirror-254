import json 

from google.cloud import dialogflowcx as cx
from google.protobuf.json_format import MessageToDict

from httpx import Client

def wh_request(tag: str, 
    parameters: dict = None, 
    text: str = None, 
    transcript: str = None
):
    wh_request = cx.WebhookRequest({}, ignore_unknown_fields=True)
    wh_request.fulfillment_info.tag = tag
    if parameters:
        wh_request.session_info.parameters = parameters
    if text:
        wh_request.text = text
    if transcript:
        wh_request.transcript = transcript
    
    return MessageToDict(wh_request._pb, including_default_value_fields=True)


with Client() as client:
    server_url = 'http://localhost:9080/'
    print('\t--- --- ---\t')
    response = client.post(server_url, json=wh_request('hello_world'))
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))
    
    print('\t--- --- ---\t')
    response = client.post(server_url, json=wh_request('user_query', text='hi there!'))
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))

    print('\t--- --- ---\t')
    response = client.post(server_url, json=wh_request('user_query', transcript='hi there!'))
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))

    print('\t--- --- ---\t')
    response = client.post(server_url, json=wh_request('session_parameters', parameters={'message': 'ezcx makes cx ez'}))
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))

    print('\t--- --- ---\t')
    response = client.post(server_url, json=wh_request('update_session_parameters', parameters={'message': 'ezcx makes cx ez'}))
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))

    print('\t--- --- ---\t')
    response = client.post(server_url, json=wh_request('telephony_transfer'))
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))

    print('\t--- --- ---\t')
    response = client.post(server_url, json=wh_request('multichannel_responses'))
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))
    