import openai
import pyttsx3
from os import startfile



engine = pyttsx3.init()

openai.api_key = "OPEN AI API KEY"
question_to_be_asked_to_ai = input("Video Title: ")



model_engine = "text-davinci-003"
prompt = f"{question_to_be_asked_to_ai}"

completion = openai.Completion.create(
    engine= model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text

print(f"here are the {question_to_be_asked_to_ai}", response)
what_to_say = (f"here are the {question_to_be_asked_to_ai}")

save = what_to_say + response
engine.say(save)
engine.save_to_file(save, 'C://Users//Asus//PycharmProjects//pythonProject//speech.mp3')
engine.runAndWait()

my_file = open("yt_speech.txt", "a")
my_file.write(f"{save}")
my_file.close()
startfile( "yt_speech.txt" )
