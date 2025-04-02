from sentiment.watson_analyzer import analyze_with_watson

text = "I am very happy today but also a bit nervous."
result = analyze_with_watson(text)
print(result)
