from google import genai
from key import api_key
from google.genai import types
from PIL import Image

client = genai.Client(api_key=api_key)

image = Image.open("Images/saas.png")

response = client.models.generate_content_stream(
        model='gemini-3.1-flash-lite',
        contents = [image, "Tell me about this image"],
        config = types.GenerateContentConfig(
            system_instruction = "Your response should uld be within 100 words, be funny",
            temperature=0.1
    )
)

for chunk in response:
    print(chunk.text, end="---\n---")

# print("The response is")
# print("-------")
# print("-------")
# print(response.text)
