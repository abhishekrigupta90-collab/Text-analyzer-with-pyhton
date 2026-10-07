# A simple text analyzer

text = input("Enter the text:")

# basic counts
char_count = len(text)
words = text.split()


words_count = len(words)

# count the sentence

sentence = 0
for ch in text:
    if ch in ". ! ?":
        sentence += 1

# find the common words
word_freq = {}
for word in words:
    word = word.strip(".?!").lower()
    if word == "":
        continue
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1


total_letters = 0
for word in words:
    total_letters += len(word)
    


print("\n--- Text Analysis Report ---")
print("Characters:", char_count)
print("total words:", words)
print("Sentence:", sentence)
print("word freq:", word_freq)
print("total lettter after cleaned:", total_letters)
