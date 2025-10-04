heroes = ['Spider man' , 'Thor' , 'Hulk','Iron man' ,'Captain America']

# 1 Length of list
print("Length of the list is:" ,len(heroes))

#2 Add Black Panther at the end of th list
heroes.append("Black Panther")
print("New superheores list :" , heroes)

#3 You realize that you need to add black panther after hulk
heroes.remove("Black Panther")
heroes.insert(3,"Black Panther")

print(heroes)


#4 now you don't like thor and hulk because they get angry easily , remove both and replace them with doctor strange
# Do that in one line of code

heroes[1:3] = ['Doctor Strange']
print(heroes)


#5 sort list in alphabetical order
heroes.sort()
print(heroes)
