from groq import Groq

def groqAi(question):
    client = Groq(api_key="Your Api Key")  # Replace with your key

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "system", "content": "You are Jarvis, a virtual assistant that gives short, clear answers. Respond like Alexa or Google Assistant."},
            {"role": "user", "content": question}
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
    )

    answer = ""

    for chunk in completion:
        if chunk.choices[0].delta.content:
            text = chunk.choices[0].delta.content
            print(text, end="")   # stream live to console
            answer += text        # build the full response
    return answer
