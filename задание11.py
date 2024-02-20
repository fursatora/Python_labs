#1 В порядке увеличения разницы между количеством согласных и количеством гласных букв в строке.
def count_vow_conson(sentence):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    vowel_count = sum(1 for char in sentence if char in vowels)
    consonant_count = sum(1 for char in sentence if char in consonants)

    return consonant_count - vowel_count

input_str = input("Введите строку: ")
sentences = input_str.split()
sorted_sentences = sorted(sentences, key=count_vow_conson)

for sentence in sorted_sentences:
    print(sentence)