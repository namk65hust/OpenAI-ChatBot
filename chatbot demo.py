import openai
import gradio

api_key = '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'#insert your openai api key here
openai.api_key = api_key
message = [{
        "role": "system",
        "content":"You are a powerful AI assistant designed to help with a variety of tasks"
    }]
def customChatBot(user_input):
    message.append({
        "role": "user",
        "content":user_input
    })
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message
    )
    reply = response['choices'][0]['message']['content']
    message.append({
        "role": "assistant",
        "content":reply
    })
    return reply 

demo = gradio.Interface(fn = customChatBot, inputs = "text", outputs = "text", title = "Chatbot Demo")
demo.launch(share = True)



