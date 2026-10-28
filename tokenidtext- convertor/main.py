import tiktoken
print("Welcome to our Text to Token ID and Token ID to Text Generator")
print("Choose what you want:")
print("1. Text to Token IDs")
print("2. Token IDs to Text")

choice = int(input("1 for text to token id  2 for token id to text"))

encoding = tiktoken.get_encoding("cl100k_base")
if(choice == 1):
    text = str(input("enter the text to be converted into token id "))
    token_ids = encoding.encode(text)
    print(f"this is your token_id {token_ids}")
    
elif(choice==2):
    sentence = input("Enter token IDs separated by commas: ")
    token_ids = [int(x.strip()) for x in sentence.split(",")]
    

    result = encoding.decode(token_ids)
    print(f"this is your sentence ->> {result}")
    
else:
    print("Invalid choice. Please enter 1 or 2.")
        