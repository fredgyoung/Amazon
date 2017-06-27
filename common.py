

def is_anagram(str1, str2, case_sensitive=True):

    # Check for Nulls
    if str1 is None or str2 is None:
        print("Invalid")
        return

    # Check length
    if len(str1) != len(str2):
        print("Fail")
        return

    # If we don't care about case
    if not case_sensitive:
        str1 = str1.lower()
        str2 = str2.lower()

    # Convert to list
    str1 = list(str1)
    str2 = list(str2)

    # Sort
    str1.sort()
    str2.sort()

    if str1 == str2:
        print("Pass")
    else:
        print("Fail")

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
is_anagram('abc', 'ABC', True) # different case
print('--------------')

# Pass
is_anagram('', '') # empty strings
is_anagram(' ', ' ') # blanks
is_anagram('abc', 'abc') # exact copy
is_anagram('abc', 'cba') # reverse string
is_anagram('!@#$', '$#@!') # special characters
is_anagram('abc', 'ABC', False) # different case

