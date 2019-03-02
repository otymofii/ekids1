import random
dogs=[" robot"," tuk","parker"]
cats=[" nota"," sun"," Max "]
food=[" apple"," pasta"," eggs "]

random.shuffle(dogs)
random.shuffle(cats)
random.shuffle(food)
for item in range (1):
    print(dogs[1] +  " " + "with" + cats[0] + " " + "eat" + food[1])

for item in range (1):
    print(dogs[0] +  " " + "with" + cats[1] + " " + "eat" + food[0])

for item in range(1):
    print(dogs[2] + " " + "with" + cats[0] + " " + "eat" + food[1])