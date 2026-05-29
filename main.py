import ollama

response = ollama.chat(
    model='qwen2.5:1.5b',
    messages=[
        {
            'role': 'system',
            'content': 'You are a cybersecurity AI assistant.'
        },
        {
            'role': 'user',
            'content': 'Explain TCP briefly'
        }
    ]
)

print(response['message']['content'])
