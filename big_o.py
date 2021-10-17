# initial big O example. 1N
def fact(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

print (fact(5))

# algorithm 2
def fact2(n):
    if n == 0:
        return 1
    else: 
        return n* fact2(n-1)

print (fact2(5))

# another Big O(log n) example
