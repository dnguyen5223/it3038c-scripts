import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "cybersecurity expert"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Welcome to Dylan Nguyen sample of GPT")

demo.launch(share=True)