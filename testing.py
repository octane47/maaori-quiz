score = 0
score =int(score)

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