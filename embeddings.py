from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

text="Eiffel Tower is in Paris and is famous landmark, it is 324 meters tall"

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-large"
)

print("vector embeddings", response.data[0].embedding)