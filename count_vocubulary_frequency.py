def processLine(line, wordCounts):
    line = repalcePunctuations(line)
    # exactrat words each line
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[words] +=1
            wordCounts[words] = 1

#replace Punctuations into space
def repalcePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_+=<>?/,.{}[]|'":
            line.replace(ch, "")
        return line

fileName = input("enter your filename:").strip()
infile = open(fileName, "r")

wordCounts = {}
for line in infile:
    processLine(line.lower(), wordCounts)

# get items exchange x,y and sort
paris = list(wordCounts.items())

items = [[x, y]for (y, x)in paris]
items.sort()

print(wordCounts)