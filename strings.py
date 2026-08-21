#Ask the user for name

name = input("What's your name ? :")


#Ask the user for age

age = input("What's your age ? :")

#Ask the user for city

city = input("Which city do you live in ? :" )


#Ask the user for what they enjoy

enjoy = input("What do you enjoy doing the most ? :")

#Create the output

statement = 'My name is' + name + '\n' +'My age is' + age + '\n' + 'I live in' + city + '\n' + 'I enjoy' + enjoy

output = "My name is {} & My age is {}. I live in {} & I enjoy {}"
s = output.format(name,age,city,enjoy)
#Print the output

print (statement)
print (s)