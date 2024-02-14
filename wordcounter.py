print("Hello!\nThis is a program showing the number of words in a text.")
inp = int(input("What would you like to do?\nFor analyzing whole text press 1\nFor counting a spesific word in the text press 2...: "))

fname = input("Enter a file name: ")
fhand = open(fname)
counterd = {}
for line in fhand:
    words = line.split()
    for word in words:
        counterd[word.lower()] = counterd.get(word.lower(), 0) + 1

if inp == 1:
    num = int(input("How many words do you want to analyze? "))
    res = sorted([(v,k) for k,v in counterd.items()], reverse=True)[:num]
    for k,v in res:
        print("Word <<<", v.upper(), ">>> passes in text for", k, "times")
elif inp == 2:
    wrd = input("Enter the word you want to check the count: ").lower()
    if wrd in counterd.keys():
        print("Word <<<", wrd.upper(), ">>> passes in text for", counterd[wrd], "times")
    else:
        print("Sorry <<<", wrd.upper(), ">>> is NOT in the text")


