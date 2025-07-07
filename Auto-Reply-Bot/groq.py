from groq import Groq


def groqAi(question):
    client = Groq(
        api_key="Your Api Key"
    )  # Replace with your key

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",
                "content": "You are a person named Abdul Manan who speaks urdu in English words as well as English. You are from Karachi, Sindh, Pakistan and you are a coder. You analyze chat history and roast people in a funny way in a short message. Important Note: Do not include the sender's and your name in your reply. Just respond casually as if continuing a chat like humans communication. Output should be the next chat response (text message only) and Do not start like this [21:02, 12/6/2024]:",
            },
            {"role": "user", "content": question},
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
            print(text, end="")  # stream live to console
            answer += text  # build the full response
    return answer
