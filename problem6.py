squareOfSums = 0
sumOfSquares = 0
for x in range (1, 101):
    sumOfSquares += x * x
    squareOfSums += x
squareOfSums *= squareOfSums

print (sumOfSquares)
print (squareOfSums)
print (squareOfSums - sumOfSquares)
