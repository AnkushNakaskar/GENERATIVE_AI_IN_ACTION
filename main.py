# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import os
from openai import OpenAI
import certifi



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    STAGE_URL="http://godric.nixy.stg-drove.phonepe.nb6/v1"
    PROD_URL="https://godric.drove.fra.phonepe.mhz/v1"

    MODEL_NAME = "global:LLM_GLOBAL_LLAMA_3_1_8B_STG" # LLAMA 3.1 deployment on stage

    client = OpenAI(base_url=STAGE_URL, api_key="<Token>") # Do not add O-Bearer/Bearer in the api_key
    client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
    ], model=MODEL_NAME)


def print_cert():
    print(certifi.where())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_cert()
    print_hi("Ankush")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
