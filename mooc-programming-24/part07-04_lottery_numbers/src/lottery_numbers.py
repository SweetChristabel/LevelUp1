# Write your solution here
def lottery_numbers(amount: int, lower: int, upper: int):
    from random import sample
    pool = list(range(lower, upper+1))
    draw = sample(pool, amount)
    return sorted(draw)