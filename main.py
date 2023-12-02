import hashlib
from itertools import permutations

def find_hash(original_hash):
    wordfile=open("words.txt", "r")
    wordfile=list(wordfile)
    
    anagram = "who outlay thieves"
    words = anagram.count(" ")
    words+=1

    char_list = list(set(anagram))

    if ' ' in char_list:
        char_list.remove(" ")
    
    finalWords = []
    
    for i in wordfile:
        flag = False
        temp_word = i.replace("\n", " ")
        temp_char = list(set(temp_word))
        for i in temp_char:
            if i not in char_list:
                flag = True
                break
        
        if flag == False:
            finalWords.append(temp_word)
    
    for element in permutations(finalWords, words):
        hashelement = " ".join(element)

        if len(hashelement) != len(anagram):
            continue
        
        m = hashlib.md5()
        m.update(hashelement.encode("utf-8"))
        wordhash = m.hexdigest()

        if wordhash == original_hash:
            return hashelement
        

hash = '13b382e1a2f8e22535b4730d78bc8591'
answer = find_hash(hash)
print(f"Collision!  The word corresponding to the given hash is '{answer}'")