print("Welcome to my quiz game.")

playing = input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()

print("okay lets play:)")
score = 0

answer = input("what is 1 + 1 = ")
if answer == '2':
    print("Correct")
    score += 1

else:
    print("Incorrect")
 
answer = input("what is 2 + 2 = ")
if answer == '4':
    print("Correct")
    score += 1 
else:
    print("Incorrect")

answer = input("what is 4 + 4 = ")
if answer == '8':
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what is 9 + 1 = ")
if answer == '10':
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what is 3 + 4 = ")
if answer == '7':
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what is 9 + 4 = ")
if answer == '12':
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what is 11 + 1 = ")
if answer == '12':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")  
print("You got " + str((score / 7) * 100 ) + "%")  
