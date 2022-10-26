
# ******************************
# Make your Code
# ******************************
strval = input().split()
numbers = list(map(int, strval))
#print (numbers)

keyword = int(input("one number: "))

countme = numbers.count(keyword)
print(countme)