import os
import future
import openai
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
os.environ["OPENAI_API_KEY"] = ""
openai.api_key = os.getenv("OPENAI_API_KEY")


root = tk.Tk()
root.withdraw()

name = simpledialog.askstring("Input", "Let's Write a Country Song! What is Your Name?")
root.wm_attributes("-topmost", True)
root.geometry("+{}+{}".format(root.winfo_screenwidth()//2, root.winfo_screenheight()//2))
partner = simpledialog.askstring("Input", "What is the name of your partner?")
root.wm_attributes("-topmost", True)
root.geometry("+{}+{}".format(root.winfo_screenwidth()//2, root.winfo_screenheight()//2))
adjective = simpledialog.askstring("Input", "Please give me an adjective?")
root.wm_attributes("-topmost", True)
root.geometry("+{}+{}".format(root.winfo_screenwidth()//2, root.winfo_screenheight()//2))
favorite1 = simpledialog.askstring("Input", "Please provide an object?")
title = name + " & " + partner
lyrics = "the lyrics of classic country artists such as George Jones, Hank Williams, Conway Twitty, Loretta Lynn, Alan Jackson, Garth Brooks, George Strait, Ernest Tubb, Kris Kristoferson, Johnny Cash, Waylon Jennings, Willie Nelson, & other classic country artists"

#name,city =  prompt.split(" ")

response6 = openai.Completion.create(
#  model="text-davinci-003",
  model="text-curie-001",
  prompt="Give me a classic, twangy, sad, country song intro in the style of " + lyrics + " about two doomed, star-crossed, jilted, cheating lovers named " + name + " and " + partner + ". The song title is: " + name + " and " + partner,
  max_tokens=50,
  temperature=0.15,
)

intro = response6.choices[0].text

response = openai.Completion.create(
#  model="text-davinci-003",
  model="text-curie-001",
  prompt="In the style of " + lyrics + " please give me another, non-repeating line that continues the thought of and rhymes with: " + intro,
  max_tokens=50,
  temperature=0.15,
)

text = response.choices[0].text

response2 = openai.Completion.create(
  #  model="text-davinci-003",
  model="text-curie-001",
  prompt="Give me an extremely sad lyric in the style of " + lyrics + " that rhymes with " + " " + text + " and incorporates the name, " + partner + " and compares said partner to " + favorite1,
  max_tokens=50,
  temperature=0.15,
)

text2 = response2.choices[0].text

response3 = openai.Completion.create(
  #  model="text-davinci-003",
  model="text-curie-001",
  prompt="Give me a sad chorus (really turn the screws!) and make in the style of " + lyrics + " that continues this song: " + intro + " " + text + " " + text2 + " " + " and that specifically incorporates the concept and imagery of " + adjective + " " + favorite1,
  max_tokens=50,
  temperature=0.15,
)
chorus = response3.choices[0].text

response4 = openai.Completion.create(
  #  model="text-davinci-003",
  model="text-curie-001",
  prompt="Give me a repeating, strongly emotional three-line lyrical refrain in the style of " + lyrics + " and have the end of each line rhyme with " + partner,
  max_tokens=50,
  temperature=0.15,
)
refrain = response4.choices[0].text

response5 = openai.Completion.create(
  #  model="text-davinci-003",
  model="text-curie-001",
  prompt="Give me a stark and poetic turn of phrase regarding: " + favorite1 + " that uses the word " + adjective + " to describe the situation",
  max_tokens=50,
  temperature=0.15,
)

powline = "When you left, you whispered, " + name + " " + response5.choices[0].text

response7 = openai.Completion.create(
  #  model="text-davinci-003",
  model="text-curie-001",
  prompt="Give me a plaintive, countrified, redneck, but sad and sorrowful lyric that rhymes with " + response5.choices[0].text,
  max_tokens=50,
  temperature=0.15,
)

verse2 = response7.choices[0].text

beforeconc = title + '\n' + intro + '\n' + text + '\n' + text2 + '\n' + chorus + '\n' + powline + '\n' + verse2 + '\n' + verse2 + '\n' + refrain + '\n' + chorus

response8 = openai.Completion.create(
  #  model="text-davinci-003",
  model="text-curie-001",
  prompt="Can you write a good ending to this classic country song in the style of (but without copying) " + lyrics + "? Here is the sad and sweet classic country song I would like you to complete :" + beforeconc,
  max_tokens=50,
  temperature=0.15,
)

conclusion = response8.choices[0].text

song = title + '\n' + intro + '\n' + text + '\n' + text2 + '\n' + chorus + '\n' + powline + '\n' + verse2 + '\n' + verse2 + '\n' + refrain + '\n' + chorus + '\n' + conclusion

response9 = openai.Completion.create(
  #  model="text-davinci-003",
  #model="text-curie-001",
  model="text-babbage-001",
  prompt="Please provide one block of text, in which three named fictional music critics each provide a short, subjectively rating " + song + " on a scale of 0-100, along with a short, one-sentence review",
  max_tokens=75,
  temperature=0.15,
)

critics = response9.choices[0].text

messagebox.showinfo("Output", f"Here is your custom country song:\n{title}\n{intro}\n{text}\n{text2}\n{chorus}\n{powline}\n{verse2}\n{verse2}\n{refrain}\n{chorus}\n{conclusion}")

messagebox.showinfo("Output", f"Here is what the critics had to say about the song:\n{critics}")

