words = ["cat", "dog", "cat", "dog", "cat", "bird"]
freq = {}
for animal in words:
 if animal in freq:
  freq[animal] += 1
 else:
  freq[animal] = 1
print(freq)
