# Write your solution here
def search(products: list, criterion: callable):
    return [prod for prod in products if criterion(prod)]


