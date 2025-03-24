# Create an empty list, simillar to js
my_list = []

# Append dot-notation to add elements 10, 20, 30, 40 to array index
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserts 15 at the second position of index 1
my_list.insert(1, 15)

# Extend my_list var with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# pop() funtion
my_list.pop()

# Sort() function my_list in ascending
my_list.sort()

# Find and print the index of value 30
index_30 = my_list.index(30)

print("Index of 30:", index_30)
