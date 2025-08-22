
text = input("Introduceti cuvantul pentru a fi cenzurat")
word_to_censor = input("Introduceti cuvantul pentru a fi cenzurat")
censored_word = word_to_censor[0] + "*" * (len(word_to_censor)-1)
# find the word in text input to censsor

censored_text = text.replace(word_to_censor, censored_word)
print(" the censored text is :  " + censored_text)
