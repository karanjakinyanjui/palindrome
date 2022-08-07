def is_palindrome(string: str):
    string = string.lower()
    string = ''.join(char for char in string if char.isalnum())
    if string == string[::-1]:
        return True


if __name__ == '__main__':
    assert is_palindrome('Race Car')
    assert is_palindrome('eye')
    assert is_palindrome('_eye')
    assert is_palindrome('A man, a plan, a canal. Panama')
    assert is_palindrome('never odd or even')
    assert is_palindrome('0_0 (: /-\ :) 0-0')
    assert not is_palindrome('1 eye for of 1 eye.')
    assert not is_palindrome('Not a palindrome')
