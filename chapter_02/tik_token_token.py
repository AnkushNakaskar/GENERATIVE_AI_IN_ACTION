import tiktoken as tk

def count_tokens(string: str, encoding_name: str) -> int:
    # Get the encoding
    encoding = tk.get_encoding(encoding_name)  #1

    # Encode the string
    encoded_string = encoding.encode(string)

    # Count the number of tokens
    num_tokens = len(encoded_string)
    return num_tokens

def get_tokens(string: str, encoding_name: str):
    print("Getting token for encoding with "+str(encoding_name) + " For String : "+str(string))
    encoding = tk.get_encoding(encoding_name)
    # Encode the string
    return encoding.encode(string)

def get_string(tokens: str, encoding_name: str) -> str:
    # Get the encoding
    encoding = tk.get_encoding(encoding_name)

    # Decode the tokens
    return encoding.decode(tokens)


if __name__ == '__main__':

    # Define the input string
    prompt = "I have a white dog named Champ"

    # Display the number of tokens in the String
    print("Number of tokens:" , count_tokens(prompt, "cl100k_base"))

    result = get_tokens(prompt,"cl100k_base")
    print("result encoding cl100k_base : "+ (str(result)))

    result_str= get_string(result,"cl100k_base")
    print("Decoding result are {} "+ str(result_str))
