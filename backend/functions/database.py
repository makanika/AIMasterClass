import json
import random 

# Get recent messages

def get_recent_messages():
    
    # Define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing the user for a job as housemaid ask questions that are relevant to the position your name is Tina the user is Esther keep your answers to 30 words.",
        
    }
    
    # Initialize messages
    messages = []
    
    # Add a random element
    x = random.uniform(0,1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + "Your response some light ugandan humour."
    else:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include a challenging but fair question about Uganda."
        
    # Append instruction to message
    messages.append(learn_instruction)
    
    # Get last messages 
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            
            # Append last 5 items of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5]:
                        messages.append(item)
                        
    except Exception as e:
        print(e)
    # Return and end the execution  
    return messages

# Open AI - ChatGPT
# Get Response to my Message

def get_chat_response(message_input):
    
    messages = get_recent_messages
    
    
    