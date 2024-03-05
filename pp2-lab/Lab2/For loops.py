#For loops1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#For loops2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#For loops3
for x in range(6):
  print(x)

#For loops4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)