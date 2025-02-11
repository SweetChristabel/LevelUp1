# Write your solution to exercise 3 here
def save_data(strings: list, filename = "shoppinglist.csv"):
    with open(filename, "w") as savefile:
        for i in strings:
            parts = i.split(", ")
            name = parts[0].replace("name: ", "")
            price = parts[1].replace("unit price: ", "")
            unit = price.split("/")[-1]
            price = price.split("€")[0]
            quantity = parts[2].replace("quantity: ","").replace(unit, "")
            totalprice = parts[3].replace("total price: ", "").replace("€","")
            savefile.write(f"{name};{price};{unit};{quantity};{totalprice}\n")



def load_data(filename = "shoppinglist.csv"):
    output = []
    with open(filename, "r") as loadfile:
        for line in loadfile:
            line = line.replace("\n","")
            components = line.split(";")
            output.append(f"name: {components[0]}, unit price: {components[1]}€/{components[2]}, quantity: {components[3]}{components[2]}, total price: {components[4]}€")
    return output
