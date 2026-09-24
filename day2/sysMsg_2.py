import ollama
response =ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"give content in 2-3 lines for 6 years old child to understand."
        },
        {
            "role": "user",
            "content": "explain engineering"
        }
    ]
)
print(response["message"]["content"])