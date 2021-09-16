
#functions go here

from random import shuffle
score = 0
score =int(score)

#main routine goes here

name = str(input("whats your name "))
print("kia ora ", name )
print("welcome to your annual maaori quiz within the following questions we will test your knowledge of the maaori language ")
print (" ")
print (" ")

##############################################
############### question 1 ###################
##############################################

#This code will decorate the title "question 1" allowing it to look nice and and set it apart from the rest of the code
#thesee 4 lines program the computer to ...
greeting= "QUESTION 1"
#greeting = 'question 1' is the heading in the middle in which the next few codes surround
sides = "!!!!" * 3
#position = (item) * amount this is side and i used ! to decorate and i want it to repeate 4 times
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
#postition = item * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

#asking the question
#print(" text ")
#print ("question")
print ("how do you say hello in maaori")
#answers to the question but only one is right
print ("A. kia ora ")
print ("B. aroha ")
print ("C. kia ara")
print ('')
#answering the question and checking it
#q1answer = answer to question
#in this question the correct answer is a, kia ora as it is how you say hello in maaori
Q1answer = "a" 
#this line allows the answer or letter to be typed ineither uppercase or lowercase and it will still count as right
Q1response= input('Your answer : ').lower()

#if else statement to continue from the question and see the reaction to what they have answered
#if response = answer it is to be counted as correct
if (Q1response == Q1answer):
  #again print text programming the computer to type something
    print ('Well done! ' + Q1response + ' is correct!')
    #score keeps up with the score +1 for every correct question
    score = score + 1
else:
  #if response doesn't = to answer then print. "unlucky that is incorrect" and continue
    print("unlucky, that is incorrect")
#displays how much questin you have gotten right
print ('Your current score is ' + str(score) + ' out of 15')
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
print ("B. tena koutou")
print ("C. tena koe")
print ('')

Q1answer = "c"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
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
print ("B. tena koutou")
print ("C. tena koe")
print ('')

Q1answer = "a"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ("Sorry, that is incorrect!")
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
#empty prints are for spacing in the code so it doesn't look jumbled up
print (" ")
print (" ")

##############################################
############### question 4 ###################
##############################################


greeting= "QUESTION 4"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" i wanna go have some kai, what does kai mean?")
print ("A. jacket")
print ("B. food ")
print ("C. sleep ")
print ('')

Q1answer = "b"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")

##############################################
############### question 5 ###################
##############################################


greeting= "QUESTION 5"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" what part of the body does poku refer to")
print ("A. arm ")
print ("B. stomach")
print ("C. ankle ")
print ('')

Q1answer = "b"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")

##############################################
############### question 6 ###################
##############################################


greeting= "QUESTION 6"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" what is a kiwi ")
print ("A. a flightless bird that lives in new zealand ")
print ("B. the name of a dolphin in the hamiltion zoo")
print ("C. the maaori name for ankle")
print ('')

Q1answer = "a"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")

##############################################
############### question 7 ###################
##############################################


greeting= "QUESTION 7"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" i need a rakau pumahara. what is a rakau pumahara? ")
print ("A. usb stick ")
print ("B. smartphone")
print ("C. computer settings")
print ('')

Q1answer = "a"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")

##############################################
############### question 8 ###################
##############################################


greeting= "QUESTION 8"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" taihoa means... ")
print ("A. help ")
print ("B. code ")
print ("C. delay ")
print ('')

Q1answer = "c"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")

##############################################
############### question 9 ###################
##############################################


greeting= "QUESTION 9"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" awa ")
print ("A. current  ")
print ("B. river ")
print ("C. stream ")
print ('')

Q1answer = "b"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")

##############################################
############### question 10 ###################
##############################################


greeting= "QUESTION 10"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" He tī māu?")
print ("A. would you like a tea? ")
print ("B. Would you like a water? ")
print ("C. Yes, one moment please ")
print ('')

Q1answer = "a"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")



##############################################
############### question 11 ###################
##############################################


greeting= "QUESTION 11"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" pai, what does pai mean?")
print ("A. ok ")
print ("B. okay ")
print ("C. aye ")
print ('')

Q1answer = "a"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")


##############################################
############### question 12 ###################
##############################################


greeting= "QUESTION 12"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" He tī māu?")
print ("A. would you like a tea? ")
print ("B. Would you like a water? ")
print ("C. Yes, one moment please ")
print ('')

Q1answer = "a"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")


##############################################
############### question 14 ###################
##############################################


greeting= "QUESTION 14"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" hey kei te pēhea koe?")
print ("A. hey, what you doing")
print ("B. hey how are you? ")
print ("C. hey how is it going ")
print ('')

Q1answer = "b"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")


##############################################
############### question 15 ###################
##############################################


greeting= "QUESTION 15"
sides = "!!!!" * 3
greeting = "{} {} {}". format(sides, greeting, sides)
top_bottom = "*" * len(greeting)
print (top_bottom)
print (greeting)
print (top_bottom)

print (" kotahi wa koa")
print ("A. one sad place ")
print ("B. one time man ")
print ("C. one,happy time ")
print ('')

Q1answer = "c"
Q1response= input('Your answer : ').lower()

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 15')
print (" ")
print (" ")

