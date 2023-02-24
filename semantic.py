import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word1))
print(word3.similarity(word2))
print(word3.similarity(word1))
print()

tokens = nlp('cat apple monkey banana ')
# The for loops below will tokenize the sentence into words and then in line 15 it will perform the similarities
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print()

my_tokens = nlp('dog cat man woman water ')
for my_tests in my_tokens:
    for my_tests2 in my_tokens:
        print(my_tests.text, my_tests2.text, my_tests.similarity(my_tests2))


# NOTE
# The sn argument printed the similarities when I only enter the code from line 1-9,
# but it comes with a paragraph, which makes it difficult to spot the comparison straightaway
# but when I added the code from line 11-13 the program crashes OSError
# on the other hand the md argument outputs the result well-structured and easy to read
