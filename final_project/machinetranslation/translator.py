'''Functions which translate english and french text'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def englishToFrench(english_text):
    '''Function to convert english to french'''
    if english_text:
        french_text = LANGUAGE_TRANSLATOR.translate(text=english_text,
            model_id='en-fr').get_result()['translations'][0]['translation']
    else:
        french_text = ''
    return french_text

def frenchToEnglish(french_text):
    '''Function to convert french to english'''
    if french_text:
        english_text = LANGUAGE_TRANSLATOR.translate(text=french_text,
            model_id='fr-en').get_result()['translations'][0]['translation']
    else:
        english_text = ""
    return english_text
