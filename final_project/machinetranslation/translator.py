```py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(mxqyrWhY9uLYOFypO1eLH-epw5m35PXohveJBgiN4j-v)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    frenchtranslation=language_translator.translate(
        text=englishtext,
        model_id='en-fr'
    ).get_result()
    return frenchText.get("translations") [0] .get("translation")
    

    def frenchToEnglish(frenchText):
englishtranslation=language_translator.translate(
        text=frenchtext,
        model_id='fr-en'
    ).get_result()    
    return englishText.get("translations") [0] .get("translation")