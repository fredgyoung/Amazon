

def find_common(str1, str2):

    str1 = str(str1)
    str2 = str(str2)

    print( str1, str2)

    result = ''

    for letter in str1:
        if letter in str2:
            result += letter

    return result


#x = find_common('string', 'strong')
#print(x)

#x = find_common(1234, 2345)
#print(x)

x = find_common(['a', 'b'], ['b', 'c'])
print(x)

