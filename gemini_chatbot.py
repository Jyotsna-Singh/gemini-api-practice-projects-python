from google import genai
from key import api_key
from google.genai import types

client = genai.Client(api_key=api_key)

print("Chat starts here... type 'endchat' to close")
chat = []

userinput = input("User : ")

while userinput != 'endchat':
    chat.append("User : " + userinput)
    systemoutput =  client.models.generate_content(
        contents = chat,
        model = 'gemini-3.1-flash-lite',
        config = types.GenerateContentConfig(
            system_instruction="Answer in 1 line, within 50 chracters"
        )
    )
    chat.append("Jobot : " + systemoutput.text)
    print("Jobot : ", systemoutput.text)
    userinput =  input("User : ")




