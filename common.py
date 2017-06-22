

def is_anagram(str1, str2, case_sensitive=True):

    # Check for Nulls
    if str1 is None or str2 is None:
        print("Invalid")
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


# Invalid
is_anagram(None, None) # nulls
is_anagram(None, 'abc') # nulls
is_anagram('abc', None) # nulls
print('--------------')

# Fail
is_anagram('', 'abc') # str1 is empty
is_anagram('abc', '') # str2 is empty
is_anagram('abc', 'def') # no matching characters
is_anagram('bcd', 'abcde') # str1 substring of str2
is_anagram('abcde', 'bcd') # str2 substring of str1
print('--------------')

# Pass
is_anagram('', '') # empty strings
is_anagram(' ', ' ') # blanks
is_anagram('abc', 'abc') # exact copy
is_anagram('abc', 'cba') # reverse string
is_anagram('!@#$', '$#@!') # special characters

