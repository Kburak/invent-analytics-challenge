#
# CHARS = 26
#
#
# def is_anagram(str1, str2):
#
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)
#
#     if len(sorted_str1) != len(sorted_str2):
#
#         count_str1 = [0] * CHARS
#         count_str2 = [0] * CHARS
#
#         i = 0
#
#         "count frequency of each character first string"
#         while i < len(str1):
#             count_str1[ord(str1[i]) - ord('a')] += 1
#             i += 1
#
#         i = 0
#         """count frequency of each character  second string"""
#         while i < len(str2):
#             count_str2[ord(str2[i]) - ord('a')] += 1
#             i += 1
#
#         result_first = 0
#         result_second = 0
#         for i in range(26):
#             result_first += abs(count_str1[i])
#             result_second += abs(count_str2[i])
#         return f"Remove {result_first} characters from {str1}, {result_second} characters from {str2}"
#
#     else:
#         for i in range(len(str1)):
#             if sorted_str1[i] == sorted_str2[i]:
#                 return 'They are anagrams'
#
#
# if __name__ == '__main__':
#     str1 = 'hea'
#     str2 = 'heal'
#     print(is_anagram(str1, str2))


# def is_anagram():
#
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)
#
#     if len(sorted_str1) != len(sorted_str2):
#         counter_str1 = len(str1) - len(str2)
#         counter_str2 = len(str2) - len(str1)
#         if counter_str1 < 0:
#             counter_str1 = 0
#         if counter_str2 < 0:
#             counter_str2 = 0
#         counter_str1 = abs(counter_str1)
#         counter_str2 = abs(counter_str2)
#         return f"Remove {counter_str1} characters from '{str1}', {counter_str2} characters from '{str2}'"
#     else:
#         for i in range(len(str1)):
#             if sorted_str1[i] == sorted_str2[i]:
#                 return "They are anagrams"
#
#
# if __name__ == '__main__':
#     str1 = input('Enter first string')
#     str2 = input('Enter second string')
#     print(is_anagram())

from collections import Counter


# def is_anagram(str1, str2):
#
#     """Dictionaries from both strings"""
#     dict1 = Counter(str1)
#     dict2 = Counter(str2)
#
#     keys1 = dict1.keys()
#     keys2 = dict2.keys()
#
#     """Count keys for each string"""
#     count_str1 = len(keys1)
#     count_str2 = len(keys2)
#
#     """Convert list of keys to set to find common keys"""
#     set1 = set(keys1)
#     common_keys = len(set1.intersection(keys2))
#
#     if common_keys == 0:
#         return f"Remove {count_str1} characters from {str1}, {count_str2} characters from {str2}"
#     else:
#         str1_remove = count_str1 - common_keys
#         str2_remove = count_str2 - common_keys
#         return f"Remove {str1_remove} characters from {str1}, {str2_remove} characters from {str2}"
#
#
# if __name__ == '__main__':
#     str1 = 'tom riddle'
#     str2 = 'voldemort'
#     print(is_anagram(str1, str2))

def is_anagram(a, b):
    """Lowercase the strings prevent Uppercase problems"""
    a = a.lower()
    b = b.lower()

    """Sort the strings to find if they are equal, if so they are anagrams"""
    sorted_str1 = sorted(a)
    sorted_str2 = sorted(b)

    if sorted_str1 == sorted_str2:
        return "They are anagrams"
    else:
        c1 = Counter(a)
        c2 = Counter(b)

        # finding the common elements from both dictionary
        common = c1 & c2

        value = 0
        # adding up the key from common dictionary in order
        # to get the total number of common elements
        for key in common:
            value = value + common[key]

        # returning the number of elements to be
        # removed to form an anagram
        str1_remove = len(a) - value
        str2_remove = len(b) - value
        return f"Remove {str1_remove} characters from '{a}', {str2_remove} characters from '{b}'"

    # Driver program


if __name__ == "__main__":
    str1 = input('Enter First String')
    str2 = input('Enter Second String')
    print(is_anagram(str1, str2))
