grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
list_ = []
for i in grades:
    sum_ = sum(i)
    avg = round(sum_/len(i),1)
    list_.append(avg)
my_dict = dict.fromkeys(students)
my_dict = {k: v for k, v in zip(my_dict,list_)}
print(my_dict)
