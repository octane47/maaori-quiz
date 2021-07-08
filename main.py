


#functions go here
score = 0
score =int(score)

#rules

#main routine goes here
name = str(input("whats your name"))
print("kia ora", name)
print("welcome to your annual maaori quiz within the following questions we will test your knowledge of the maaori language, goodluck and have fun remember its also a game so dont worry to much ")
print (" ")
print (" ")

##############################################
############### question 1 ###################
##############################################
greeting= "QUESTION 1"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)


print ("how do you say hello in maaori")
print ("A. kia ora ")
print ("B. aroha ")
print ("C. kia ara")
print ('')

Q1answer = "A"
Q1response= input('Your answer : ')

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print (" ")
print (" ")

##############################################
############### question 2 ###################
##############################################

greeting= "QUESTION 2"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print ("how would you greet one person")
print ("A. nau mai")
print (" B. tena koutou")
print (" C. tena koe")
print ('')

Q1answer = "c"
Q1response= input('Your answer : ')

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print (" ")
print (" ")
##############################################
############### question 3 ###################
##############################################


greeting= "QUESTION 3"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print ("aroha means....")
print ("A. love")
print (" B. tena koutou")
print (" C. tena koe")
print ('')

Q1answer = "A"
Q1response= input('Your answer : ')

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print (" ")
print (" ")


