import pyttsx
path=raw_input("Enter path of text file:")
with open(path) as doc:
    content=doc.read()
doc.close()
engine = pyttsx.init()
engine.say(content)
engine.runAndWait()
