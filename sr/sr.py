import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('')
service = SpeechToTextV1(authenticator=authenticator)
service.set_service_url('https://stream.watsonplatform.net/speech-to-text/api')

# models = service.list_models().get_result()
#
# model = service.get_model('en-US_BroadbandModel').get_result()

with open("chunk0000.wav", 'rb') as audio_file:
    print(json.dumps(service.recognize(audio=audio_file, content_type='audio/wav').get_result()))





