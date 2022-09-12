# thing='a'
# place='b'

# print(f'THE {thing} is in the {place}')

def aaa(word):
    if word[0] in "aeiou":
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'
    

print(aaa("python"))