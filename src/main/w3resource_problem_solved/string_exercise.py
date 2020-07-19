"""
resource link: https://www.w3resource.com/python-exercises/string/
"""

"""
1. Write a Python program to calculate the length of a string.
"""


def get_length(string):
    count = 0
    for _ in string:
        count += 1
    return count


"""
2. Write a Python program to count the number of characters (character frequency) in a string.
"""


def get_characters_frequency(string):
    char_freq = {}
    for char in string:
        keys = char_freq.keys()
        if char not in keys:
            char_freq[char] = 1
        else:
            char_freq[char] += 1

    return char_freq


"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.
"""


def solved_problem_3(string):
    if get_length(string) < 2:
        return ""
    return string[:2] + string[-2:]


"""
4. Write a Python program to get a string from a given string where 
all occurrences of its first char have been changed to '$', except the first char itself.
"""


def solved_problem_4(string):
    result = ""
    for char in string:
        if char not in result:
            result += char
        else:
            result += "$"
    return result


"""
5. Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""


def swap_characters(str1, str2):
    return str2[:2] + str1[2:], str1[:2] + str2[2:]


"""
6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""


def solved_problem_6(string):
    if get_length(string) < 3:
        return string

    ing = string[-3:]
    if ing == "ing":
        return string + "ly"
    else:
        return string + "ing"


"""
7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""


def solved_problem_7(string, a, b, r):
    pos_of_1st_word = string.find(a)
    pos_of_2nd_word = string.find(b)

    if pos_of_2nd_word > pos_of_1st_word >= 0:
        string = string.replace(string[pos_of_1st_word : pos_of_2nd_word + len(b)], r)

    return string


"""
12. Write a Python program to count the occurrences of each word in a given sentence.
"""


def get_word_frequency(line):
    word_frequency = {}
    words = line.split()

    for word in words:
        keys = word_frequency.keys()
        if word not in keys:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    return word_frequency


"""
24. Write a Python program to check whether a string starts with specified characters.
"""


def check_starts_with(line, prefix):
    return line.startswith(prefix)


"""
25. Write a Python program to create a Caesar encryption.
"""


def caesar_cipher_encrypt(line):
    encrypt_line = ""
    for i in range(get_length(line)):
        if "z" >= line[i] >= "a":
            encrypt_line += chr((ord(line[i]) + 3 - 97) % 26 + 97)
        elif "Z" >= line[i] >= "A":
            encrypt_line += chr((ord(line[i]) + 3 - 65) % 26 + 65)
        else:
            encrypt_line += line[i]
    return encrypt_line


"""
38. Write a Python program to count occurrences of a substring in a string.
"""


def count_substring_occurrences(string, substring):
    return string.count(substring)


"""
39. Write a Python program to reverse a string.
"""


def reverse(string):
    return "".join(reversed(string))


"""
40. Write a Python program to reverse words in a string.
"""


def reverse_words(text):
    for line in text.split("\n"):
        return " ".join(line.split()[::-1])
