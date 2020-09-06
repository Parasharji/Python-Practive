names=['hello','world','wassup','mississippi','parashar']

for word in names:
    counts={}
    for letter in word:
        if letter in counts:
            counts[letter]+=1
        else:
            counts[letter]=1
    if max(counts.values())>2:
        print(word)
