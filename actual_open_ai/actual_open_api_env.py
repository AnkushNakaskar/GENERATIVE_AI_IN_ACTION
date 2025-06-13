from openai import OpenAI
import httpx
# Get the API from gmail ankush.nakaskar@gmail.com Or from : https://platform.openai.com/settings/organization/api-keys
api_key=""
http_client = httpx.Client(verify=False)
client = OpenAI(base_url="https://api.openai.com/v1", api_key=api_key, http_client=http_client)


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "Who is CEO of microsoft ?"}
  ]
)
print(completion)
print(completion.choices[0].message);
