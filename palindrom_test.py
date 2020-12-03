word = list(input())
print(word)
if word == word.reverse():
    print('Entered word is palindrome')
else:
    print('Entered word is not palindrome')