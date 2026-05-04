def count_words(sentence):
 return len(sentence.strip().split())
 
 text = input("enter a sentence:")
 print(count_words(text))
