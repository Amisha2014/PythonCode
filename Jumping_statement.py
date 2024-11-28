#Jumping statement
# break,continue,pass

#Break -lets us exit a loop early if a certain condition is met

# for num in range (0, 10):
#     if num == 3:
#         break
#    print (num)


#Continue - skips the current loop cycle and moves on to the nest one
# for num in range (1, 15):
#     if num ==3:
#         continue
#     print (num)

# Pass is like do nothing statement it used as a placeholder for code
# we haven't written yet or if we want to skip a step without affecting the loop

# for num in range (1, 15):
#     if num ==3:
#         pass
#     print (num)



# I just need a loop from 1 to 10
# if num==3 means do nothing
# elif num is even means just skip the number
# elif num reaches 9 means it stop the loop entirely
# else print num

for num in range (1, 11):
    if num ==3:
        pass
    elif num % 2 == 0:
        continue
    elif num == 9:
        break

    print (num)

