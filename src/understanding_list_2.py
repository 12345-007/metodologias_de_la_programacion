# SLICING
players = ['sr7', 'messi', 'travis', 'chicha',  'corona']
print(players[0:3])

# SLICE es trabajar con un grupo espesifico 
# de elementos de una lista 
print(players[1:3])  #['messi', 'travis', 'chicha']
print(players[:4])   #['cr7', messi, 'travis, 'chicha']
print(players[2:])   #

print(players[-3:])
print(players[-3:-1])
print(players[4:2])

# slicing en for 
players = ['sr7', 'messi', 'travis', 'chicha', 'corona', 'jorge', '']
first_three_players = players[0:3]
print("frist three player", first_three_players)
print("aqui vienen los tres mejores del salon:")
for player in players[0:3]:
    print(player.upper())

# copia de listas 
my_food = ['pizza', 'gorditas de gaumave', 'machacado']
#copy_of_food = my_food    # manera incorrecta de copiar una lista 
copy_of_food_1 = my_food[:]
copy_of_food_2 = my_food.copy()
copy_of_food_3 = list(my_food)



#pregunta de examen: [las listas son elemntos mutables para almacenar elemntos  ]
#las tuplas son listas inmutables tambien sirven para almacenar elementos pero no se pueden modificar 

#modificando elementos 
cars = ['bwm', 'porch', 'masda', 'totoya', 'ford']
cars=[0]="bmw"
cars=[1]="porshe"
cars=[2]="mazda"
cars=[3]="toyota"

    


