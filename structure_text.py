from google import genai
from key import api_key
from pydantic import BaseModel
import enum

class Grade(enum.Enum):
    A_PLUS = "a+"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]
    rating: Grade

client = genai.Client(api_key=api_key)

prompt ="List a few popular cookie recipes, and include the amount of ingredients"

response = client.models.generate_content(
    model='gemini-3.1-flash-lite',
    contents = prompt,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[Recipe]
    }
)

print("The response is ")
print("-------------------")
print("-------------------")
print(response.text)
