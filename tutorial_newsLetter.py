s = input("Enter the news: ")

cLetters = 0
cWords = 0
cLines = 0

for i in s:
    if i.isalpha():
        cLetters += 1

    elif i in [".", "!", "?"]:
        cLines += 1

cWords = len(s.split())

print(cLetters, cWords, cLines)
