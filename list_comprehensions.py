#list comprehension

list_even_odd = ["even" if number%2 == 0 else "odd" for number in range (1,21)]
print(list_even_odd)

#list of multiples of 3
multiples_of_3 = [number for number in range (1,10) if number%3 == 0]
print(multiples_of_3)