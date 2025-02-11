# Write your solution here
def file_process(filename: str):
    recipes = {}
    with open(filename) as openedfile:
        recipe = []
        for line in openedfile:
            strline = line.strip()
            if strline == "":
                recipes[recipe[0]] = []
                for i in recipe[1:]:    
                    recipes[recipe[0]].append(i)
                recipe = []
                continue
            else:
                recipe.append(strline)
        recipes[recipe[0]] = []
        for i in recipe[1:]:    
            recipes[recipe[0]].append(i)
    return recipes

def search_by_name(filename:str, word:str):
    recipes = file_process(filename)
    foundrecipes = []
    wordlwr = word.lower()
    for key in recipes:
        lowerkey = key.lower()
        if wordlwr in lowerkey:
            foundrecipes.append(key)
    return foundrecipes

def search_by_time(filename:str, prep_time:int):
    recipes = file_process(filename)
    foundrecipes = []
    for key in recipes:
        preptime = int(recipes[key][0])
        if preptime <= prep_time:
            foundrecipes.append(f"{key}, preparation time {preptime} min")
    return foundrecipes

def search_by_ingredient(filename:str, ingredient:str):
    recipes = file_process(filename)
    foundrecipes = []
    for key in recipes:
        preptime = int(recipes[key][0])
        if ingredient in recipes[key]:
            foundrecipes.append(f"{key}, preparation time {preptime} min")
    return foundrecipes


if __name__ == "__main__":
    foundrecipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in foundrecipes:
        print(recipe)