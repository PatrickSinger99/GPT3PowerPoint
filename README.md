# GPT3PowerPoint
The goal of this project was to automatically create presentation slides using openAI's GPT-3 model.

### First Version
The first Version uses a Text as input and using GPT-3 summarizes it to bulletpoints.
Then, using the bulletpoints, a different GPT-3 Model tries to get the topic from the text. This topic is used to download a matching image
Finally the bulletpoints and the image are used to automatically create a PowerPoint file (.pptx)

### Second Version
The second version uses a wikipedia api to get the text of a given topic and generates bulletpoint from it.
The picture downloading algortithm is used again and expanded to get multiple matching images
Now a presentation with multiple slides corresponding to the subtopics of the wikipedia article is generated

### Third Version
In the third version we wanted GPT to generate the text on its own.
We we trained a model to generate bulletpoint from a single topic.
This is used in combination with the image downloader to create a PowerPoint presentation file

### HTML Version
In the fourth version we wanted GPT to generate the code for its presentation.
We therefore switched to a html Presentation using markdown and the jupyter notebook framework for design
First a trained GPT model uses the topic input to generate subtopics
Then a second model generates text from all the subtopics
A third GPT model uses the generated text as input to generate the html markdown code for the presentation
At the end a html presentation with one slide per subtopic is automatically generated
