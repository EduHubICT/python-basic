from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()


# Count the number of characters (character appearance) in a string
def count_char_appearance(string):
    char_dict = {}
    for n in string:
        keys = char_dict.keys()
        if n in keys:
            char_dict[n] += 1
        else:
            char_dict[n] = 1
    return char_dict


#  Add 'ing' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'ing' then add 'ly' instead.
#  If the string length of the given string is less than 3, leave it unchanged
def add_string(string):
    length = len(string)
    if length > 2:
        if string[-3:] == "ing":
            string += "ly"
        else:
            string += "ing"
    return string


# Find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string
def replace_string(string):
    string_not = string.find("not")
    string_poor = string.find("poor")

    if string_poor > string_not > 0 and string_poor > 0:
        # replace 'not...poor' with 'good'
        string = string.replace(string[string_not : (string_poor + 4)], "good")
        return string
    else:
        return string


# takes a list of words and returns the length of the longest one
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]


# Remove the nth index character from a nonempty string
def remove_char(string, n):
    first_part = string[:n]  # slice the string upto nth index
    last_part = string[n + 1 :]  # slice the string after nth index
    return first_part + last_part  # concatenate the two slice


# Count the occurrences of each word in a given sentence
def count_word(string):
    counts = dict()
    words = string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
