# Write your solution here
def prime_numbers():
    number = 2
    while True:
        if prime_check(number):
            yield number
        number += 1    
        
def prime_check(number):
    for n in range (2, number):
        if number % n == 0:
            return False
    return True

#I tried to do this without a helper method but it felt difficult and spaghetti. Model solution also used a helper function!

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))