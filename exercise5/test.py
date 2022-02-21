a_list = [1,2,3,5,5]
print(any(a_list.count(element) > 1 for element in a_list))