from gtts import gTTS
import os
myText = "Text to speech test test test haha čauky čurák"
language = "cs"
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")
