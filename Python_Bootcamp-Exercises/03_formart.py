# inserting value in the {}
print('this is a string {}'.format('INSERTED'))

# ordering the values {}
print('the {2} {1} {0}'.format('fox','brown','quick'))

# ordering the values {}
print('the {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

# Float formatting:

result = 100/777

print("the result was: {r} ".format(r= result))

# Float formatting: follows {value: width(white space).precision f}

print("the result was {r:1.3f}".format(r= result))

print("the result was {r:10.1f}".format(r= result))

# Other way to use formating is:

name = "Luana"
age = 30
print(f"My name is {name} and I am {age} old")