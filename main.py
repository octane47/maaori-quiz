from testing1 import*


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

print ("QUESTION 1: how do you say hello in maaori")
print ("A. kia ora ")
print (" B. none ")
print (" C. bunga")
print ('')

Q1answer = "A"
Q1response= input('Your answer : ')

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')




