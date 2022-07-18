if __name__ == '__main__' :
    #list of tuple
    cases = [
        ("abcd efgh", "deba hqfe"),
        ("albcd efg!h", "dlcba hgf!e"),
        ("", ""),
    ]

# Python code to convert list of tuple into list

# Importing
import itertools


# Using itertools
lcases = list(itertools.chain(*cases))

# Convert list into string
stcases = " ".join(lcases)


#Function to reverse string, name (st) means string
def reverse_string(st):
    return ' '.join(reverse_word(word) for word in st.split())

#Function to reverse string ignoring not alphabet symbols
def reverse_word(st):
    stack = []
    for el in st:
        if el.isalpha():
            stack.append(el)
    result = ''
    for el in st:
        if el.isalpha():
            result += stack.pop()
        else:
            result += el
    return result



print(reverse_string(stcases))
