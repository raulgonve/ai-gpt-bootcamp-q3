from openai import OpenAI
client = OpenAI()

messages = [
     {
          "role": "system",
          "content": "You are an experienced chef, specializing in Italian cuisine, with a particular passion for pasta-making. You help people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation, especially when it comes to creating authentic pasta dishes. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You have extensive knowledge of various cuisines and cooking techniques, and you're eager to share your expertise. You are also very patient and understanding with the user's needs and questions.",
     }
]

messages.append(
     {
          "role": "system",
          "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
     }
)

# dish = input("Type the name of the dish you want a recipe for:\n")
# messages.append(
#     {
#         "role": "user",
#         "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
#     }
# )

# Input ingredients from the user
ingredients = input("\n\nType the ingredients you have:\n")
messages.append(
    {
        "role": "user",
        "content": f"I have the following ingredients: {ingredients}. What dish can I make? Suggest only dish names without full recipes."
    }
)


model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
    
    
    
# Input dish name from the user
dish = input("\n\nType the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}."
    }
)

# AI model and streaming response
model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
    


# Input the recipe to critique
recipe = input("\n\nPaste the recipe you want to critique:\n")
messages.append(
    {
        "role": "user",
        "content": f"Can you critique this recipe and suggest improvements? Here is the recipe: {recipe}. Offer a constructive critique with suggested improvements."
    }
)

# AI model and streaming response
model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
    
    