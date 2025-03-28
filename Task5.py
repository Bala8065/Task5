Name: Balakumar
Email: bala8065@gmail.com
Phno: 9790816791
Batch code: PAT-C-WE-E-B7


Task 5
1. Given a list of dictionaries each representing a person with name and age keys use lambda function to filter out people under 18 and the map the remaining peoples names to a new list
                
people = [
 {"name": "Bala", "age": 25},
{"name": "kumar", "age": 17},
{"name": "Jeeva", "age": 30},
{"name": "Hema", "age": 15}
]
# Filter out people above 18
adults = list(filter(lambda person: person["age"] >= 18, people))


# Map the names of the adults to a new list
adult_names = list(map(lambda person: person["name"], adults))


#print person above 18 in list
print("Person above 18:",adult_names)


# Filter out people under 18
adults = list(filter(lambda person: person["age"] <= 18, people))


# Map the names of the adults to a new list
adult_names1 = list(map(lambda person: person["name"], adults))


#print person below 18 in list
print("Person below 18:", adult_names1)


Output:
Person above 18: ['Bala', 'Jeeva']
Person below 18: ['kumar', 'Hema']
 
2. Given a list of numbers use to reduce function and a lambda expression to calculate the product of all the numbers in the list 
        
        #import the reduce function 
from functools import reduce


def add(x, y):
                    return x + y
c = [1, 2, 3, 4, 5, 6]


#reduce function
total = reduce(add, c)


#print the value
print(“Product of all the number:”,total)
Output: 
Product of all the number: 21


3. Write a list comprehension that creates a new list of squares of even numbers from a given list, using a lambda function to check for even numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Comprehension and lambda function to filter even numbers and square


squareeven = [x**2 for x in numbers if (lambda x: x % 2 == 0)(x)]


print(squareeven)


Output:  [4, 16, 36, 64, 100]


4. Write a lambda function to check if a given string is a number 


is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))


Output: 
True
True
False
True
False
True


Print checking numbers:
True
True




5. Use a lambda function to extract the year month and day from a date time object 


import datetime


# Create a lambda function to extract year, month, date, and time
extract_datetime = lambda x: (x.year, x.month, x.day, x.time())


# Get the current date and time
current_datetime = datetime.datetime.now()


# Extract year, month, date, and time using the lambda function
year, month, day, time = extract_datetime(current_datetime)


# Print the extracted values
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Time:", time)


6. Create a lambda function to generate a fibonacci series up to n terms
        
                from functools import reduce


fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2] range(n-2), [0, 1])


print(fib(5))