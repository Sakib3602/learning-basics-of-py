x = {"sakib", "rahim" , "karim"}

x.add("lol")
x.remove("sakib")
print(x)


# object / dictionary

phone = {
    "name" : "sakib",
    "phone" : 1928383,
    "age" : 24,
    "job" : "student"
}

for i,j in phone.items():
    print(f'here he value :: {i} and this is value result ::{j}')


phone = [{
    "name" : "iphone",
    "phone" : 1928383,
    "ranf" : 24,
    "job" : "student"
},
{
    "name" : "samsung",
    "phone" : 1928383,
    "ranf" : 24,
    "job" : "student"
},
]

for i in phone:
    for x,y in i.items():
        print(f'vari :: {x} and value ::: {y}')

