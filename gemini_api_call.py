from google import genai
from key import api_key

client = genai.Client(api_key=api_key)

prompt = input("Enter your prompt : ")

response = client.models.generate_content(
    model='gemini-3.1-flash-lite',
    contents = prompt
)

print("The response is ")
print("-------------------")
print("-------------------")
print(response.text)
