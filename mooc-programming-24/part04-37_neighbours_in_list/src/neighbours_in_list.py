# Write your solution here
def longest_series_of_neighbours(integers: list):
    rep = 0
    wintemp = 0
    winner = 0
    while rep < len(integers) - 1:
        if abs(integers[rep] - integers[rep+1]) == 1:
            wintemp += 1
            if wintemp > winner:
                winner = wintemp
        else:
            wintemp = 0
        rep += 1
    winner += 1
    return winner


#Here the suggested solution had a slightly smarter approach, using a for loop for range between 1 and list length
#and the calculation of absolute value with the number prior, not after.
#No need for rep variable then, nor the hard coded +1 in the end.
#To update the winner variable, a max function was used within the loop. 

if __name__ == "__main__":
    integers = [1, 2, 3, 2, 1, 5, 4, 6, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 5, 2, 6, 5, 3, 1, 6]
    print(longest_series_of_neighbours(integers))