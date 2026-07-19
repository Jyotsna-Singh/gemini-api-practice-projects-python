from google import genai
from key import api_key
from google.genai import types

client = genai.Client(api_key=api_key)

grounding_tool = types.Tool(
    google_search = types.GoogleSearch()
    )

response = client.models.generate_content(
        model='gemini-3.1-flash-lite',
        contents = "Who is leading CJP protest in India in 2026?",
        config=types.GenerateContentConfig(
            tools=[grounding_tool]
        )
)

print("The response is")
print("-------")
print("-------")
print(response.text)
time.sleep(2)
