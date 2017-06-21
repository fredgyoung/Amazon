

def is_anagram(str1, str2, case_sensitive=True):

    # Check for Nulls
    if str1 is None or str2 is None:
        print("Cannot compare Null variables")
        return

    # If we don't care about case
    if not case_sensitive:
        str1 = str1.lower()
        str2 = str2.lower()

    # Convert to list
    str1 = list(str1)
    str2 = list(str2)
    
    for letter in str1:
        if letter in str2:
            str2.remove(letter)
        else:
            print("Fail")
            return

    if len(str2) > 0:
        print("Fail")
    else:
        print("Pass")

    return

"""
1. f (string, strong) // happy path
2. f (null, null) // both null
3. f ("", "") // both empty strings
4. f (" ", " ") // both empty strings with spaces - blank strings
5. f ("abc", "zxy") // no matches
6. f ("!@#$", "1@#!@") // special chars
7. f (null, "somestring") // 1st param null other not
8. f ("somestring", null) // 2nd param null other not
9. Test with very large inputs
10. f ("azzzzzzzz", "zzzzzzza") // mathcing in different positions
"""


is_anagram('string', 'gnirts')
is_anagram(None, None)
is_anagram('', '')
is_anagram(' ', ' ')
is_anagram('abc', 'def')
is_anagram('!@#$', '$#@!')
is_anagram(None, 'abc')
is_anagram('abc', None)
is_anagram('azzzzzzzzz', 'zzzzzzzzza')

