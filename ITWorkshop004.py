text='Print every word in this sentence that has an even number of letters'
for words in text.split(" "):
    if len(words)%2 == 0:
        print(words,"even")