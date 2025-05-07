from langdetect import detect

text = input("Enter text here: ")

language = detect(text)

print("Detected Language Is: ", language)