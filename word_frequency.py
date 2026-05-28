def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


sentence = "Python is easy and Python is fun and useful"

result = word_frequency(sentence)


sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

print("Word Frequencies:")

for word, count in sorted_result:
    print(word, ":", count)