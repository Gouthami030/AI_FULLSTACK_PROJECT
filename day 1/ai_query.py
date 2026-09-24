import ollama
response =ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Example ai in 40 words"
        }
    ]
)
print(response["message"]["content"])