print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction=str(input("You come across two direction panels in the island as soon as u reach there so which direction you wanna go left or right:"))
if direction=="left":
  action=str(input("You come across a big lake out of nowhere,in the middle of nowhere as you feel like you were teleported .What do you wanna do swim or wait?"))
  if action=="wait":
    door=str(input("After coming out of the lake you come across many doors but what intrigues u the most are red,blue and yellow doors,you can also open other doors but remember you can only open one door at a time so which one will it be?"))
    if door=="red":
       print("Burned by fire.\nGame Over.")
    elif door=="blue":
       print("Eaten by beasts.\nGame Over.")
    elif door=="yellow":
       print("You Win!")
    else:
       print("Game Over.")
  else:
    print("Attacked by trout.\nGame Over.")
else:
  print("Fall into a hole.\nGame Over.")



    
    


