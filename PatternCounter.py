file = open("dataset_2_7.txt", "r")

fileContent = file.readlines()

Text = fileContent[0]
Pattern = fileContent[1].replace("\n","")
file.close()

def PatternCount(Text, Pattern):

    textLength = len(Text)
    patternLength = len(Pattern)
    counter = 0

    for x in range(0, textLength - patternLength + 1):
        if Text[x : x + patternLength ] == Pattern:
            counter = counter + 1
    return counter

print(PatternCount(Text, Pattern))

