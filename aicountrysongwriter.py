import os
os.environ["OPENAI_API_KEY"] = ""
import future
import openai
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

lyrics = "I work a forty hour week and I earn my keep And try to walk proud and tall I keep my nose to the grind and I don't get behind And I don't back up at all, Well my neck's a little red my collar's blue, I sip a little coffee and drink a little booze, Cause I'm a all American country boy, I’m my daddy's spittin' image and my momma's pride and joy, There ain't nothing down home, There ain't nothing down home, That I don't really enjoy, Cause I'm a all American country boy; Beneath the floor and ever greens, That kept the ridge on high, There lives a green eyed mountain girl that stole my heart one night She loved me like I never known And cast me down below To never feel her touch again Or taste that mountain snow That Appalachian Mountain Girl That haunts me from above My heart will never beat the same Without her mountain love I often wake up late at night Dreaming about her Then walked on floor till morning comes And hope she will return; Rolling down-a backwoods Tennessee byway, One arm on the wheel holding my lover, With the other a sweet soft southern thrill, Worked hard all week Got a little jingle, On a Tennessee Saturday night  couldn't feel better, I'm together with my Dixieland Delight, Spend my dollar park in a holler, 'Neath the mountain moonlight, Hold her up tight make a little loving, A little turtledoving on a Mason-Dixon night, Fits my life oh so right, My Dixieland Delight, White-tail buck deer munching on clover, Red-tail hawk sitting on a limb chubby old groundhog, Croaking bullfrog free as a feeling in the wind, Homegrown country girl gonna give me a whirl, On a Tennessee Saturday night  lucky as a seven, Living in heaven with my Dixieland Delight; I lost all my money in a crooked poker game, Now I’m going home on this old freight train, I got the boxcar blues shuffle on down the tracks, I got the boxcar blues and Lord I may never get back, Well I am so lonely I think I could die, These ain’t cinders they are tears in my eyes, I got the boxcar blues shuffle on down the tracks, I got the boxcar blues and Lord I may never get back, I dream of my big baked biscuit in the pan, I dream of my woman with another man, I got the boxcar blues shuffle on down the tracks, I got the boxcar blues and Lord I may never get back, When I get back home I’ll get down on my knees, I’ll beg to my woman to have a little mercy please, I got the boxcar blues shuffle on down the tracks, I got the boxcar blues and Lord I may never get back; There's a lot of ways of saying, What I want to say to you, There's songs and poems and promises, And dreams that might come true, But I won't talk of starry skies, Or moonlight on the ground, I'll come right out and tell ya, I'd just love to lay you down, Lay you down and softly whisper, Pretty love words in your ear, Lay ya down and tell ya all the things, A woman loves to hear, I'll let you know how much it means, Just having you around, Oh Darling how I'd, Love to lay ya down, There's so many ways your sweet love's, Made this house into a home, You've got a way of doing little, Things that turn me on, Like standing in the kitchen, In your faded cotton gown, With your hair all up in curlers, I'd still love to lay you down, When a whole lot of Decembers, Are showing in your face, Your auburn hair has faded, And silver takes it's place, You'll be just a lovely, And I'll still be around, And if I can I know that I'll still, Love to lay you down, Lay you down and softly whisper, Pretty love words in your ear, Lay ya down and tell ya all the things, My woman loves to hear, I'll let you know how much it means, Just having you around, Oh Darling how I'd, Love to lay ya down; Well it was all that I could do to keep from cryin', Sometimes it seemed so useless to remain, But you don't have to call me darlin'  darlin', You never even call me by my name, You don't have to call me Waylon Jennings, And you don't have to call me Charley Pride, And you don't have to call me Merle Haggard anymore, Even though you're on my fightin' side, And I'll hang around as long as you will let me, And I never minded standin' in the rain, But you don't have to call me darlin' darlin', You never even call me by my name, Well I've heard my name a few times in your phonebook (hello hello), And I've seen it on signs where I've played, But the only time I know I'll hear David Allan Coe Is when Jesus has His final judgement day, Well I was drunk the day my mom got out of prison, And I went to pick her up in the rain, But before I could get to the station in a pickup truck, She got run'd over by a damned old train And I'll hang around as long as you will let me, And I never minded standin' in the rain, Ohh you don't have to call me darlin'  darlin', You never even call me but I wonder why you don’t call me, Why you don’t ever call me by my name; Hear that lonesome whippoorwill, He sounds too blue to fly, The midnight train is whining low, I'm so lonesome I could cry, I've never seen a night so long, When time goes crawling by, The moon just went behind the clouds, To hide its face and cry, Did you ever see a robin weep, When leaves began to die?, Like me, he's lost the will to live, I'm so lonesome I could cry, The silence of a falling star, Lights up a purple sky, And as I wonder where you are, I'm so lonesome I could cry; Your cheatin' heart will make you weep, You'll cry and cry and try to sleep, But sleep won't come the whole night through, Your cheatin' heart will tell on you, When tears come down like fallin' rain, You'll toss around and call my name, You'll walk the floor the way I do, Your cheatin' heart will tell on you, Your cheatin' heart will pine someday, And crave the love you threw away, The time will come when you'll be blue, Your cheatin' heart will tell on you, When tears come down like fallin' rain, You'll toss around and call my name, You'll walk the floor the way I do, Your cheatin' heart will tell on you; I shoulda took you dancin', A little candle light romancin' with roses, But I was high upon a bar stool, I was such a blind fool, now I know it, You won't believe how much I've changed since you left, It took losin' you, for me to find myself, Oh, I wish that you could see me, Steady hands without the whiskey, you'd be so proud, Got that job down at the factory, A brand new suit for Sunday, I'm in church now, It's been one year since I sat behind a bar, I went by the junk-yard, they've still got our car, I still see you on your knees, Beggin' me not to drive, But I took away the keys, And made you climb inside, An' I'd take your place in this field of stone if I only had the power, Look what it took for me to finally bring you flowers; There's a long line of mourners coming down our street, Their fancy cars're such a sight to see, They're all of your rich friends that knew you in the city, And now they finally brought you back to me, The papers told of how you lost your life, Of the party and that fatal crash that night, The race on the highway the curve nobody seen, Now you're riding in that long black limousine, When you left home you told me that someday you'd be returnin', With a fancy car for a whole town to see, Well now everybody's watching now and I guess you finally got your dream, You're riding in one of them long black limousines, Through tears I watch as you ride by, With a chauffeur at the wheel dressed up so fine, I'll never love another for my heart and all my dreams, Ride with you in that long black limousine; He said, I'll love you til I die, She told him, You'll forget in time, As the years went slowly by, She still preyed upon his mind, He kept her picture on his wall, Went half crazy now and then, But he still loved her through it all, Hoping she'd come back again, He kept some letters by his bed, Dated 1962, He had underlined in red, Every single 'I love you', I went to see him just today, Oh but I didn't see no tears, All dressed up to go away, First time I'd seen him smile in years, He stopped loving her today, They placed a wreath upon his door, And soon they'll carry him away, He stopped loving her today, You know she came to see him one last time, Oh, and we all wondered if she would, And it kept runnin' through my mind, This time, he's over her for good, He stopped loving her today, They placed a wreath upon his door, And soon they'll carry him away, He stopped loving her today; She put him out like the burnin' end of a midnight cigarette, She broke his heart, he spent his whole life tryin' to forget, We watched him drink his pain away a little at a time, But he never could get drunk enough to get her off his mind, Until the night, He put that bottle to his head and pulled the trigger, And finally drank away her memory, Life is short, but this time it was bigger, Than the strength he had to get up off his knees, We found him with his face down in the pillow, With a note that said, I'll love her till I die, And when we buried him beneath the willow, The angels sang a whiskey lullaby, La, la, la, la, la, la, la, La, la, la, la, la, la, la, The rumors flew but nobody knew how much she blamed herself, For years and years she tried to hide the whiskey on her breath, She finally drank her pain away a little at a time, But she never could get drunk enough to get him off her mind, Until the night She put that bottle to her head and pulled the trigger, And finally drank away his memory, Life is short, but this time it was bigger, Than the strength she had to get up off her knees, We found her with her face down in the pillow, Clinging to his picture for dear life, We laid her next to him beneath the willow, While the angels sang a whiskey lullaby, La, la, la, la, la, la, la, La, la, la, la, la, la, la; I know you loved him, A long time ago, Even now in my arms, You still want him, I know, But darling this time, Let your memories die, When you hold me tonight, Don't close your eyes, Don't close your eyes, Let it be me, Don't pretend it's him, In some fantasy, Darling, just once, let yesterday go, And you'll find more love, Than you've ever known, Just hold me tight, When you love me tonight, And don't close your eyes, Maybe I've been a fool, Holding on all this time, Lyin' here in your arms, Knowing he's in your mind, But I keep hoping some day, That you'll see the light, Let it be me tonight, Don't close your eyes, Don't close your eyes, Let it be me, Don't pretend it's him, In some fantasy, Darling, just once let yesterday go, And you'll find more love, Than you've ever known, Just hold me tight, When you love me tonight, And don't close your eyes, Don't close your eyes, Let it be me, Don't pretend it's him, In some fantasy, Darling, just once let yesterday go, You'll find more love than you've ever known, Just hold me tight, When you love me tonight, And don't close your eyes, Just hold me tight, When you love me tonight, And don't close your eyes"

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

#name,city =  prompt.split(" ")

response6 = openai.Completion.create(
  model="text-davinci-003",
  prompt="Give me a classic, twangy, sad, country song intro in the style of " + lyrics + " about two doomed, star-crossed, jilted, cheating lovers named " + name + " and " + partner + ". The song title is: " + name + " and " + partner,
  max_tokens=50,
  temperature=0.1,
)

intro = response6.choices[0].text

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="In the style of " + lyrics + " please give me another, non-repeating line that continues the thought of and rhymes with: " + intro,
  max_tokens=50,
  temperature=0.1,
)

text = response.choices[0].text

response2 = openai.Completion.create(
  model="text-davinci-003",
  prompt="Give me an extremely sad lyric in the style of " + lyrics + " that rhymes with " + " " + text + " and incorporates the name, " + partner + " and compares said partner to " + favorite1,
  max_tokens=50,
  temperature=0.1,
)

text2 = response2.choices[0].text

response3 = openai.Completion.create(
  model="text-davinci-003",
  prompt="Give me a sad chorus (really turn the screws!) and make in the style of " + lyrics + " that continues this song: " + intro + " " + text + " " + text2 + " " + " and that specifically incorporates the concept and imagery of " + adjective + " " + favorite1,
  max_tokens=50,
  temperature=0.1,
)
chorus = response3.choices[0].text

response4 = openai.Completion.create(
  model="text-davinci-003",
  prompt="Give me a repeating, strongly emotional three-line lyrical refrain in the style of " + lyrics + " and have the end of each line rhyme with " + partner,
  max_tokens=50,
  temperature=0.1,
)
refrain = response4.choices[0].text

response5 = openai.Completion.create(
  model="text-davinci-003",
  prompt="Give me a stark and poetic turn of phrase regarding: " + favorite1 + " that uses the word " + adjective + " to describe the situation",
  max_tokens=50,
  temperature=0.1,
)

powline = "When you left, you whispered, " + name + " " + response5.choices[0].text

response7 = openai.Completion.create(
  model="text-davinci-003",
  prompt="Give me a plaintive, countrified, redneck, but sad and sorrowful lyric that rhymes with " + response5.choices[0].text,
  max_tokens=50,
  temperature=0.1,
)

verse2 = response7.choices[0].text

beforeconc = title + '\n' + intro + '\n' + text + '\n' + text2 + '\n' + chorus + '\n' + powline + '\n' + verse2 + '\n' + verse2 + '\n' + refrain + '\n' + chorus

response8 = openai.Completion.create(
  model="text-davinci-003",
  prompt="Can you write a good ending to this classic country song in the style of (but without copying) " + lyrics + "? Here is the sad and sweet classic country song I would like you to complete :" + beforeconc,
  max_tokens=50,
  temperature=0.1,
)

conclusion = response8.choices[0].text

song = title + '\n' + intro + '\n' + text + '\n' + text2 + '\n' + chorus + '\n' + powline + '\n' + verse2 + '\n' + verse2 + '\n' + refrain + '\n' + chorus + '\n' + conclusion

response9 = openai.Completion.create(
  model="text-davinci-003",
  prompt="Please provide one block of text, in which three named fictional music critics each provide a short, subjectively rating " + song + " on a scale of 0-100, along with a short, one-sentence review",
  max_tokens=60,
  temperature=0.1,
)

critics = response9.choices[0].text

messagebox.showinfo("Output", f"Here is your custom country song:\n{title}\n{intro}\n{text}\n{text2}\n{chorus}\n{powline}\n{verse2}\n{verse2}\n{refrain}\n{chorus}\n{conclusion}")

messagebox.showinfo("Output", f"Here is what the critics had to say about the song:\n{critics}")

