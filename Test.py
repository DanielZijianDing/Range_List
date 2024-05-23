from Range_List import range_list
# How to use:
# X = range_list(), to initialize, now X is empty expressing y is always 0
# X.add(from ,to, amount), to add an amount to the y where x in range [from, to)
# X.set(from ,to, amount), to set the value of y to amount where x in range [from, to)


## Test Example
#Test 1
X = range_list()
X.add(10, 30, 1)
X.add(20, 40, 1)
X.add(10, 40, -2)
X.show()

#Test 2
X = range_list()
X.add(11, 30.5, 1)
X.add(20.1, 45, 1)
X.add(10, 45, -2)
X.show()