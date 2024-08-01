# initializing list
test_list = [ '14', '62', '23','17', '2', '8', '71', '3']

# printing original list
print(" \n The original list is: " + str(test_list))

# Using sort()+ key
# Decending sort string numbers
test_list.sort(key = int, reverse = True)
print(" \n The resultant reverse sorted list : " + str(test_list))

# Acending sort string numbers
test_list.sort(key = int, reverse = False)
print(" \n The resultant list : " + str(test_list))
