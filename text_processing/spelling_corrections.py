from textblob import TextBlob as tb

def Convert(string):
	li = list(string.split())
	return li

str1 = input("Enter your word: ")

words = Convert(str1)

corrected_words = []

for i in words:
	corrected_words.append(tb(i))

print("Wrong words: ", words)
print("Corrected words are: ")

for i in corrected_words:
	print(i.correct(), end=" ")
