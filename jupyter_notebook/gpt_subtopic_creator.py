from gpt import GPT
import openai
from gpt import Example

# Openai key
with open("openai_key.txt") as file:
    key = file.read()
    openai.api_key = key

# GPT Model to create bulletpoints from a topic
gpt_point_creation = GPT(engine="davinci", temperature=.5, max_tokens=120)

gpt_point_creation.add_example(Example("car",
                                       "motor, vehicle, transportation, road, wheels"
                                       ))

gpt_point_creation.add_example(Example("tiger",
                                       "cat, panthera, predator, wildlife, endangered"
                                       ))

gpt_point_creation.add_example(Example("blockchain",
                                       "crypto, cryptography, transaction, bitcoin, cryptocurrency"
                                       ))

gpt_point_creation.add_example(Example("germany",
                                       "country, europe, berlin, european union, demogracy"
                                       ))


# Create Text (Bulletpoints) from a topic
def create_text_from_topic(prompt):
    output = gpt_point_creation.submit_request(prompt)
    text_output = output.choices[0].text[8:]
    einzeldaten = text_output.split(",")
    print("GPT-3 generated subtopics:\n" + text_output)
    return einzeldaten

create_text_from_topic("network")