# Write your solution here
def create_tuple(x: int, y: int, z: int):
    myfirstevertuple = (min(x, y, z), max(x, y, z), (x+y+z))
    return myfirstevertuple


if __name__ == "__main__":
     print(create_tuple(5, 3, -1))