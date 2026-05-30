sentence = input("Enter a sentence: ").lower()
words = sentence.split()
uniquelist = []
mostrepeated = ''
highestcount = 0
count = 0
for x in words:
 if x not in uniquelist:
  uniquelist.append(x)
for i in uniquelist:
 count = words.count(i)
 if count > highestcount:
  highestcount = count
  mostrepeated = i
print(f'Total words: {len(words)}')
print(f'Unique words: {len(uniquelist)}')
print(f'Most repeated: {mostrepeated}') 
