# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import os
from openai import OpenAI



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    STAGE_URL="http://godric.nixy.stg-drove.phonepe.nb6/v1"
    PROD_URL="https://godric.drove.fra.phonepe.mhz/v1"

    MODEL_NAME = "global:LLM_GLOBAL_LLAMA_3_1_8B_STG" # LLAMA 3.1 deployment on stage

    client = OpenAI(base_url=STAGE_URL, api_key="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJpZGVudGl0eU1hbmFnZXIiLCJ2ZXJzaW9uIjoiNC4wIiwidGlkIjoiZWY2Mzc3OWEtMDJlMi00MzE0LWE3MTAtNWYzYzJkNzYwNmI3Iiwic2lkIjoiMDk5MWY5Y2YtOGJmMy00ZWYxLTlhNTItNTk5YzJiM2EzMGM2IiwiaWF0IjoxNzQ5MTEyMzQxLCJleHAiOjE3NDk3MTcxNDF9.nkjA2yTc0ZmNVkuwvswD2VJlwAg-goOm8uQ-PHT6khRDVcUS8bnRwrn5RKm3a6QOgU0a315ZL88PctGXuhlz3A") # Do not add O-Bearer/Bearer in the api_key
    client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
    ], model=MODEL_NAME)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
