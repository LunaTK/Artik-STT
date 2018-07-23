import requests
import json

# data = open('./introduce.wav', 'rb').read()

def transcript(data):
    response = requests.post(
        url='https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=ko-KR_NarrowbandModel',
        auth=('236f4487-fd5f-49ca-b286-6232520fa834', 'BryjOY7dZylp'),
        data=data, \
        headers={'Content-Type': 'audio/wav'})
    print('text type : ', type(response.text))
    # text = response.text.encode('utf-8').decode('utf-8')
    # print('response : ', text)
    response = json.loads(response.text)
    # transcript = response['results'][0]['alternatives'][0]['transcript']
    # print('transcript : ', response)
    return response
