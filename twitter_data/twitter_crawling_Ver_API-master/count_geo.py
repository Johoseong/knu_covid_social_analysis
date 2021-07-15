file = open('화이자 2021-03-01~2021-07-13.txt', "r", encoding="utf-8")
 
text = file.read() 
wordList = text.split()

count = 0
 
for word in wordList:
    if '"geo"' in word:
        count += 1

print(count)