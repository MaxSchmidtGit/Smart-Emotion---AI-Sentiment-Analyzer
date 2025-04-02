import openai
import config

# Set your API key
client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

def analyze_with_openai(text):
    """
    Analyze sentiment using OpenAI's GPT model (v1+ SDK).
    Returns a response text with emotion percentages.
    """
    prompt = (
        "Analyze the emotional tone of this sentence and give a score (0-100%) for each emotion:\n"
        f"{text}\n"
        "Emotions: joy, sadness, anger, fear, disgust.\n"
        "Return the result as a JSON object."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that detects emotions in text."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=150
    )

    return response.choices[0].message.content
