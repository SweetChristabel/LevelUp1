# Write your solution here:
def sort_by_remaining_stock(items: list):
    def get_remaining_stock(item: tuple):
        return item[-1]
    return sorted(items, key=get_remaining_stock)