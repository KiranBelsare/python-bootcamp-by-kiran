#que5
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
print(is_palindrome("Rotator"))
print(is_palindrome("Noon"))
print(is_palindrome("Book"))