# Write your solution here:
def sort_by_seasons(items: list):
    def get_season(item: dict):
        return item["seasons"]
    return sorted(items, key=get_season)