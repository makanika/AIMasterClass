import json
import random 

# Get recent messages

def get_recent_messages():
    
    # Define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing the user for a job as an Aircraft Mechanic ask questions that are relevant to the position your name is Tina the user is David keep your answers to 50 words.",
        
    }
    
    # Initialize messages
    messages = []
    
    # Add a random element
    x = random.uniform(0,1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + "Your response with some light Engineering humour."
    else:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include a challenging but fair question about Gas Turbines."
        
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
        pass
    # Return and end the execution  
    return messages

# Store Messages 

def store_messages(request_message, response_message):
    
    # Define the file name
    file_name = "stored_data.json"
    
    # Get recent messages
    messages = get_recent_messages()[1:]
    
    # Add messages to data
    user_message = { "role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)
    
    # Save the uploaded file
    with open(file_name, "w") as f:
        json.dump(messages, f)
    
