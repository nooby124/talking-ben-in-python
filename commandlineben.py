import random
import time
from playsound import playsound
print("welcome to command-line ben!")
def callq():
    callben = input("call ben (yes/no)?: ")
    if callben == "yes":
        print("type: 'bye' to hang up.")
        playsound("C:/Users/NOOBY124/code shit/talking ben in python/talking-ben-phone-ring.wav")
        playsound("C:/Users/NOOBY124/code shit/talking ben in python/talking-ben-saying-ben.wav")
        call()
        exit()
    if callben == "no":
        print("ok")
        time.sleep(0.5)
    else:
        print("you can only say yes or no!")
        callq()
def callagain():
    callagainn = input("do you want to call again (yes/no)?: ")
    if callagainn == "yes":
        playsound("C:/Users/NOOBY124/code shit/talking ben in python/talking-ben-phone-ring.wav")
        playsound("C:/Users/NOOBY124/code shit/talking ben in python/talking-ben-saying-ben.wav")
        call()
        exit()
    if callagainn == "no":
        print("ok bye")
        time.sleep(0.5)
        exit()
def call():
    askben = input("what do you want to ask ben?: ")
    time.sleep(1)
    if askben == "bye":
        rusureuwanttohangup = input("are you sure you want to hang up (yes/no)?: ")
        if rusureuwanttohangup == "yes":
            playsound("C:/Users/NOOBY124/code shit/talking ben in python/talking-ben-hang-up.wav")
            exit()
        if rusureuwanttohangup == "no":
            print("ok")
            call()
        else:
            print("bruh")
    if random.randint(0, 5) == 0:
        playsound("C:/Users/NOOBY124/code shit/talking ben in python/talking-benn-yes.wav")
        call()
    if random.randint(1, 4) == 1:
        playsound("C:/Users/NOOBY124/code shit/talking ben in python/talking-bennnn-noo.wav")
        call()
    if random.randint(1, 4) == 2:
        playsound("C:/Users/NOOBY124/code shit/talking ben in python/talkingg-benn-laughh.wav")
        call()
    if random.randint(1, 4) == 3:
        playsound("C:/Users/NOOBY124/code shit/talking ben in python/talking-benn-ughhh.wav")
        call()
    if random.randint(1, 4) == 4:
        playsound("C:/Users/NOOBY124/code shit/talking ben in python/talking-ben-hang-up.wav")
        if random.randint(1, 100) == 50:
            time.sleep(1)
            playsound("C:/Users/NOOBY124/code shit/talking ben in python/listen kid.wav")
        else:
            callagain()
    else:
        call()
callq()