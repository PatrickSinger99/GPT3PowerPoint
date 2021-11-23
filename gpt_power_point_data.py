import openai
from gpt import GPT
from gpt import Example
from google_images_download import google_images_download
import gpt_power_point_creator
import os
import shutil
import wikipediaapi

# Set wikipedia language
wiki_wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

# Get topic
while True:
    # Inputs
    prompt = input("Topic: ")

    # Define the wikipedia page
    p_wiki = wiki_wiki.page(prompt)

    # Summary of the wikipedia page
    wiki_summary = p_wiki.summary
    print(wiki_summary)
    verify = input("Do you want to summarize this text? (y/n): ")
    if verify.lower() == "y":
        break

# Openai key
with open("openai_key.txt") as file:
    key = file.read()
    openai.api_key = key
    print(key)

# Create model
gpt_sum = GPT(engine="davinci", temperature=.3, max_tokens=70)

# Training the model with examples
gpt_sum.add_example(Example("Napoleon III (Charles Louis Napoléon Bonaparte; 20 April 1808 – 9 January 1873) was the "
                            "first President of France (as Louis-Napoléon Bonaparte) from 1848 to 1852 and the Emperor "
                            "of the French from 1852 to 1870. A nephew of Napoleon I, he was the last monarch to rule "
                            "over France. Elected to the presidency of the Second Republic in 1848, he seized power by "
                            "force in 1851, when he could not constitutionally be reelected; he later proclaimed "
                            "himself Emperor of the French. He founded the Second Empire, reigning until the defeat "
                            "of the French Army and his capture by Prussia and its allies at the Battle of Sedan in "
                            "1870. Napoleon III was a popular monarch, who used plebiscites to guide his actions, "
                            "oversaw the modernisation of the French economy and worked to have the centre of Paris "
                            "rebuilt following the guidelines of the Napoleon III style. He expanded the French "
                            "overseas empire and made the French merchant navy the second largest in the world, "
                            "engaged in the Second Italian War of Independence as well as the disastrous "
                            "Franco-Prussian War, in which he commanded his soldiers during the fight and was "
                            "captured.",
                            "Napoleon III was the first President of France. "
                            "He founded the Second Empire, reigning until the defeat. "
                            "He made the French merchant navy the second largest in the world."
                            ))

gpt_sum.add_example(Example("A mitochondrion (/ˌmaɪtəˈkɒndriən/;[1] pl. mitochondria) is a double-membrane-bound "
                            "organelle found in most eukaryotic organisms. Mitochondria generate most of the "
                            "cell's supply of adenosine triphosphate (ATP), used as a source of chemical energy.[2] "
                            "They were first discovered by Albert von Kölliker in 1880 in the voluntary muscles of "
                            "insects. The mitochondrion is popularly nicknamed the powerhouse of the cell,"
                            " a phrase coined by Philip Siekevitz in a 1957 article of the same name.",
                            "A mitochondrion is a double-membrane-bound organelle. "
                            "Mitochondria generate most of the cell's supply of adenosine triphosphate. "
                            "The mitochondrion is often called the powerhouse of the cell. "
                            ))

gpt_sum.add_example(Example("A blockchain is a growing list of records, called blocks, that are linked together "
                            "using cryptography.[1][2][3][4] Each block contains a cryptographic hash of the "
                            "previous block, a timestamp, and transaction data (generally represented as a Merkle "
                            "tree). The timestamp proves that the transaction data existed when the block was published"
                            " in order to get into its hash. As blocks each contain information about the block "
                            "previous to it, they form a chain, with each additional block reinforcing the ones "
                            "before it. Therefore, blockchains are resistant to modification of their data because "
                            "once recorded, the data in any given block cannot be altered retroactively without "
                            "altering all subsequent blocks.",
                            "A blockchain is a list of blocks, that are linked together. "
                            "Blockchains are resistant to modification of their data. "
                            "The data in any given block cannot be altered once recorded."
                            ))


output = gpt_sum.submit_request(wiki_summary)
output = output.choices[0].text[8:]
if len(output) > 280:
    to_cut = ""
    for i in reversed(range(1, len(output))):
        if output[i] == ".":
            output = output.replace(to_cut, "")
            break
        to_cut = output[i] + to_cut


print("\nSummarized points:")
for sentence in output.split("."):
    print("    - " + sentence)


# Getting the keywords
keyword_response = openai.Completion.create(engine="davinci", prompt="Text: " + output + "Keywords:", temperature=0.3, max_tokens=60, top_p=1.0,
                                            frequency_penalty=0.8, presence_penalty=0.0, stop=["\n"])


# convert enumeration into list
keywords = keyword_response.choices[0].text
keywords = keywords.split(",")

print("\n Extracted keywords:")
for keyword in keywords:
    print("    - " + keyword)

# Delete download folder if it exists
try:
    shutil.rmtree('downloads')
except FileNotFoundError:
    pass

# Download an image to every keyword (currently just the first one)
for i in keywords[:1]:
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": i, "limit": 1, "print_urls": True, format: "jpg"}
    response.download(arguments)

# Create path to image
pic_path = "downloads/" + keywords[0] + "/" + os.listdir("downloads/" + keywords[0])[0]

gpt_power_point_creator.create_power_point_from_gpt(keywords[0], output, pic_path)
