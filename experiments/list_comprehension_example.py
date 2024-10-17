
integers = [1,2,3,4,5,6]
odd_ints = [x for x in integers if x % 2 == 1]
squared_odds = [x*x for x in odd_ints]
total = sum(squared_odds)

print(squared_odds)
print(odd_ints)