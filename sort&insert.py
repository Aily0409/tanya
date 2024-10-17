#INSERT
insert_list =["Master", "Online"]
insert_list.insert(1,"Code")
print(insert_list)
C = [4,5,6]
D =[1,2,3]
C.insert(0,D)
print(C)

#SORT
people = ["Jason", "Conner", "Megan"]
people.sort()
print(people)

numbers = [3,5,8,1,8.2,9]
numbers.sort()
print(numbers)

other_people = ["Richard", "Bruce", "Alfred", "John"]
other_people.sort(reverse=True)
print(other_people)

other_numbers = [2,5,4,67,7,3,58,5,9,4]
other_numbers.sort(reverse=True)
print(other_numbers)

more_names= ["Clark", "Artemis", "Wally"]
more_names.sort(reverse=True, key=len)
print(more_names)

another_names= ["Emmy", "Ana", "Richardson"]
another_names.sort(reverse=True,key=len)
print(another_names)