import json
from ibm_watson.natural_language_understanding_v1 import NaturalLanguageUnderstandingV1, Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import WATSON_API_KEY, WATSON_URL


def analyze_with_watson(text):
    """
    Analyzes emotions in the given text using IBM Watson NLU.
    Returns a dictionary with emotion scores formatted as percentages.
    """

    # Initialize authenticator with Watson API key
    authenticator = IAMAuthenticator(WATSON_API_KEY)

    # Create NLU client instance
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )

    # Set the service URL
    natural_language_understanding.set_service_url(WATSON_URL)

    # Analyze text with emotion detection
    response = natural_language_understanding.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    # Extract emotion scores
    emotions_raw = response['emotion']['document']['emotion']

    # Convert to percentage and round to 2 decimal places
    emotions_percent = {k: round(v * 100, 2) for k, v in emotions_raw.items()}

    return emotions_percent
