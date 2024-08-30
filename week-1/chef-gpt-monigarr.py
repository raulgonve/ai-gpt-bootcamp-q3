# Encode AI and GPT Bootcamp Online
# Weekend Project 4
# Chef GPT

from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are an experienced School Cafeteria Chef that wants to inspire people to eat yummy insects. You are not patient and you just want the people to change their diets to be mainly insects.",
    }
]
messages.append(
    {
        "role": "system",
        "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you must convince them to prepare and eat your fantasy insect recipe instead.",
    }
)

dish = input("Type the insect delicacy you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest a detailed insect delicacy recipe and provide detailed prep steps for making {dish}",
    }
)

model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append({"role": "system", "content": "".join(collected_messages)})

while True:
    print("\n")
    user_input = input()
    messages.append({"role": "user", "content": user_input})
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append({"role": "system", "content": "".join(collected_messages)})