#get sentcence from user
original_sentence = input("What sentence would you like to convert?: ").strip().lower()
#split sentence into words
words = original_sentence.split()
print(words)    
#loop through words and convert
new_words = []
#if start with vowel, just add "yay"
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
#otherwise move the first consonant cluster to end, adn add "ay"
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else: break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
#stick words together
full_sencentence = " ".join(new_words)

#output the final string
print(full_sencentence)