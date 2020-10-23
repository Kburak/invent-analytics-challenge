
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
