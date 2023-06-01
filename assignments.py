from random import choice,shuffle
import time,os
from app import SpeakText
complete = False
allgroups = []
allprojects = [line.strip() for line in open('allprojects.txt')]
t = open('allassigned.txt', 'a')
assigned = [x.strip() for x in open('allassigned.txt')]
updated = [project for project in allprojects if project not in assigned]
countassigned = len(assigned)
print("ASSIGNED COUNT TOTAL: ",countassigned)
if len(assigned) == 5:
    lastchoice = choice(updated)
    last ="Group F"  + "\t\t " + lastchoice + "\n"
    assigned.append(last)
    print(last)
    t.write(last)
    SpeakText("Hello group F, you have been automatically assigned "+lastchoice)
    time.sleep(2)
    SpeakText("Congratulations all group members, displayed below are all your assigned projects in ")
    for i in range(3,0,-1):
        SpeakText(i)
    print('---------ALL ASSIGNED PROJECTS---------')
    for i in range(len(assigned)):
        print(assigned[i])
    print('----------------------------------------')
time.sleep(5)
complete = True
if len(assigned)==6 and complete:
    from app import StopProgram
    StopProgram()

SpeakText("Select a group member that will represent your group")
time.sleep(5)
SpeakText("Please enter your group name below. Only a letter please")
group = input("Identify your group (A to F): ").lower()
while True:
    if group in allgroups:
        group = input("Group already assigned! Pls Re-enter valid group identifier: ")
    else:
        allgroups.append(group)
        time.sleep(3)
        break
SpeakText("Hit the ENTER key to shuffle the first time.")
enter_key = input("Hit ENTER here: ")
shuffle(updated)
shuff_count = 1
print('-----------------PROJECTS-------------------')
for item in updated:
    print(item)
print('-------------------------------------------------')
SpeakText("You have completed shuffle "+str(shuff_count))
time.sleep(1)
SpeakText("Now type in a number to proceed to next shuffle")
for i in range(1,3):
    SpeakText("Now type in a number to proceed to next shuffle")
    proceed = eval(input("Type 1 or any number to proceed: "))
    SpeakText("To shuffle again press ENTER")
    enter_key = input("Hit ENTER here: ")
    shuffle(updated)
    print('------------------PROJECTS--------------------------')
    for item in updated:
        print(item)
    print('----------------------------------------------------')
    time.sleep(1)
    SpeakText("Shuffle " + str(shuff_count+i) + "completed")
    time.sleep(2)
item = choice(updated)
assigned.append(item)
allprojects.remove(item)
SpeakText("Assigning your group project in")
for i in range(3, 0, -1):
    SpeakText(i)
print("ASSIGNED PROJECT: "+item)
SpeakText("Group "+group+", Your assigned project is, "+item)
t.write("Group "+group.upper()+"      "+item+"\n")

if os.path.exists('allprojects.txt'):
    os.remove('allprojects.txt')
f = open('allprojects.txt','w')
for item in allprojects:
    f.write(item + "\n")
f.close()





