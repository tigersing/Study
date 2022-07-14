def reverse_string(st):
    return ' '.join(reverse_word(word) for word in st.split())

def reverse_string(st):
    return ' '.join(reverse_word(word) for word in st.split())

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

instr = 's3ghcggggg hgtpopopo!!!!!!yj%h'

print(reverse_string(instr))#g3ggggchgs hjyopopop!!!!!!tg%h



