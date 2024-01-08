print("Hello!\nThis is a program showing the number of words in a text.")
num = int(input("How many words do you want to analyze? "))
fname = input("Enter a file: ")
fhand = open(fname)

counter = {}
for line in fhand:
    words = line.split()
    for word in words:
        counter[word] = counter.get(word, 0) + 1


print(sorted([(v,k) for k,v in counter.items()], reverse=True)[:num])
"""
lst = []
for k,v in counter.items():
    lst.append((v, k))

print(sorted(lst, reverse=True)[:num])
"""
