import config
from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)

def ask_gpt3():
    messagesSequel = []
    
    while True:
        
        if question == "stop":
            print("GPT 3.5 ENDED")
            break
        
        else:
            question = input("What do you want to ask for GPT3?")
            messagesSequel.append({"role": "user", "content": question})
                
            answer = client.chat.completions.create(
                model= "gpt-3.5-turbo",
                messages = messagesSequel,
            )
            messagesSequel.append(answer.choices[0].message)
            
            print("GPT 3.5: ", answer.choices[0].message.content) 
    

