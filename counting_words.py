fname = input("Enter a file name: ")
fhand = open(fname)

counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

"""
if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1
"""

biggest_count = None
biggest_word = None

for k, v in counts.items():
    if biggest_count is None or v > biggest_count:
        biggest_word = k
        biggest_count = v

print("The most repeated word in your text is:", "<<<---",biggest_word,"--->>> for <<<---",biggest_count,"--->>> times")
