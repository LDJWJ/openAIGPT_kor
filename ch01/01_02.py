# Import the necessary libraries
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the pre-trained GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Set the model to evaluation mode
model.eval()

# Define a prompt for the model to complete
prompt = input("You: ")

# Tokenize the prompt and generate text
input_ids = tokenizer.encode(prompt, return_tensors = 'pt')
output = model.generate(input_ids, max_length = 50, do_sample = True)

# Decode the generated text and print it to the console
generated_text = tokenizer.decode(output[0], skip_special_tokens = True)
print("AI: " + generated_text)
