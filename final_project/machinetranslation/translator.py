"""Translation English to French and back"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('mxqyrWhY9uLYOFypO1eLH-epw5m35PXohveJBgiN4j-v')
language_translator = LanguageTranslatorV3(
    version='2023-04-23',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')


def english_to_french(english_text):
    """Translation English to French"""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def  french_to_english(french_text):
    """Translation French to English"""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text