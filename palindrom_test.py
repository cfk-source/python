word = input()
palindrome = word[::-1]
if palindrome == word:
    print('Is palindrome')
else:
    print('Not palindrome')