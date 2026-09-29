with open("sample2.txt", "r") as file:
    text = file.read()
print(text)
print("No of characters: " ,len(text))
print("no fo words :",len(text.split()))
print("no of lines:",len(text.splitlines()))