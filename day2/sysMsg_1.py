import ollama
response =ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"give the answers in 2-3 lines only."
        },
        {
            "role": "user",
            "content": "explain engineering"
        }
    ]
)
print(response["message"]["content"])