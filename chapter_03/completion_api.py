
import os
from openai import OpenAI
import certifi


def get_token():
    try:
        with open('../token.txt', 'r') as file:
            content = file.read();

    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return content;

def completion(content):


    STAGE_URL="http://godric.nixy.stg-drove.phonepe.nb6/v1"
    PROD_URL="https://godric.drove.fra.phonepe.mhz/v1"

    MODEL_NAME = "global:LLM_GLOBAL_LLAMA_3_1_8B_STG" # LLAMA 3.1 deployment on stage
    auth_token_val = str(get_token()).strip();
    client = OpenAI(base_url=STAGE_URL, api_key=str(auth_token_val)) # Do not add O-Bearer/Bearer in the api_key
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": str(content),
            }
    ], model=MODEL_NAME)
    print(response)
    print(">>>")
    return response.choices[0].message.content






def print_cert():
    print(certifi.where())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_cert()
    print(completion("Say this is a test"))
    while True:
        query = input("Please enter your name: ")
        print(completion(str(query)))


