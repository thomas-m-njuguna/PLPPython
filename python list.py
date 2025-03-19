my_list = []
my_list.append([10, 20, 30, 40])  # Now my_list = [[10, 20, 30, 40]]
my_list[0].append(15)  # my_list = [[10, 20, 30, 40, 15]]

sec_list = [50, 60, 70]

my_list.extend(sec_list)  # my_list = [[10, 20, 30, 40, 15], 50, 60, 70]

my_list.pop(-1)  # Removes the last element (70)

print(my_list)  # Output: [[10, 20, 30, 40, 15], 50, 60]
