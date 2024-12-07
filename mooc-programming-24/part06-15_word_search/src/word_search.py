# Write your solution here
def find_words(search_term: str):
    wordlist = []
    hitlist = []
    with open("words.txt") as rawlist:
        for line in rawlist:
            wordlist.append(line.strip())
    
    if search_term[0] == "*":
        search = search_term.strip("*")
        for word in wordlist:
            if word.endswith(search):
                hitlist.append(word)
    
    if search_term[-1] == "*":
        search = search_term.strip("*")
        for word in wordlist:
            if word.startswith(search):
                hitlist.append(word)

    elif "." in search_term:
        import fnmatch
        search = search_term.replace(".","?")
        hitlist = fnmatch.filter(wordlist, search)
                    

    else:
        if search_term in wordlist:
            hitlist.append(search_term)
    return hitlist


if __name__ == "__main__":
    print(find_words("ane*"))