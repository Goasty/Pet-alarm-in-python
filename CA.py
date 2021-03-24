import datetime
import time
import playsound
animaldict = {}
animals_to_add = True
#Time = time.strftime('%H:%M')
#introduction to program

print('Hello this is your frendly program to help you remeber to feed those animals of yours')
while animals_to_add:
    #input animal information and time
    animal = input('What is the animal you would like to feed?')
    hour = (input('What hour would you like to feed them?'))
    min = (input('What minute would you like to feed them in the hour?'))
    ampm = input('AM or PM')
    if(ampm == 'pm'):
        hour = hour + 12
    #time = int(str(hour) + str(min))
    #changed for format in datetime.time
    #time = datetime.time(hour, min, 00)
    time = (hour) +':'+ (min) + ':00'
    #store info in the dict
    animaldict[animal] = time
    #ask if there are more animal
    repeat = input('Do you have any other animals to add?')
    if repeat == 'no':
        animals_to_add = False
print('Animals to feed: ')
for animal, time in animaldict.items():
    print(animal + ' at ' + str(time))
print(animaldict)
print(datetime.datetime.now())
#to get time to cycle and set alarms of
while(1 == 1):
    #now = time.strftime('%H:%M')
    for animal, time in animaldict.items():
        now = datetime.datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        #if time == datetime.datetime.now().hour and datetime.datetime.now().min:
        if time == dt_string:
            print('Time to feed the ' + animal)
