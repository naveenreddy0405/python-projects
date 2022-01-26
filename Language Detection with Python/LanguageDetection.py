from langdetect import detect
input_text = input("Enter text in any language: ")
print(detect(input_text))