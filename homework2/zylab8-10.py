# Basim Siddiqui
# PSID: 1517778

def palindrome_test(word):
    new_word = word.replace(' ', '')
    word_length = len(new_word)
    reversed = new_word[word_length::-1]
    if reversed == new_word:
        print(word, 'is a palindrome')
    else:
        print(word, 'is not a palindrome')



user_word = input()
palindrome_test(user_word)