def reverse_sentence(sentence):
    slova = sentence.split()
    r_sentence = ' '.join(slova[::-1])
    return r_sentence
print(reverse_sentence("We are ready"))