def reverse_index(reverse_word):
    new_word = ''
    new_word = (reverse_word[6] + reverse_word[5] + reverse_word[4] + reverse_word[3] + reverse_word[2] + reverse_word[1] + reverse_word[0])
    print(new_word)
    return(new_word)
reverse_index("Goodbye")

def capitalize_string(strong):
    word_one = strong[0]
    word_two = strong[4]
    word_three = strong[9]
    new_list = strong
    dev = word_one[0]
    code = word_two[0]
    camp = word_three[0]
    if (dev) == 'd':
        strong.remove('d')
    if (code) == 'c':
        strong.remove('c')
    if (camp) == 'c':
        strong.remove('c')
    return new_list
    

new_list = capitalize_string('dev code camp')
print()