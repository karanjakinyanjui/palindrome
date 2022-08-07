def is_palindrome(string: str):
    string = string.lower()
    string = ''.join(char for char in string if char.isalnum())
    return string == string[::-1]
