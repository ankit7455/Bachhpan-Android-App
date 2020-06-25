from gtts import gTTS 


import os 
mytext = 'hello Google my name is john my name is johnny my name is roy'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("welcome.mp3") 
 
os.system("play welcome.mp3") 

