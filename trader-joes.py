import random
from datetime import datetime

#date/time info
now = datetime.now()
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
current_month = str(month_names[now.month - 1])
current_day = str(now.day)

#manager name generator
possible_names = ["Cedar", "Lavar", "Celik", "Zhenna", "Ivy", "Krysta", "Moonbeam", "Donna", "Sasha"]
def random_name():
    chosen_name = random.choice(possible_names)
    possible_names.remove(chosen_name)
    return chosen_name

#food name generator
possible_foods = [["organic valencia peanut butter", "peanut butter"], ["ginger snap cookies", "cookie"], ["organic olive oil popcorn", "popcorn"], ["mochi ice cream balls", "ice cream"]] #[specific item, singular generic description]
def new_food():
    chosen_food = random.choice(possible_foods)
    possible_foods.remove(chosen_food)
    return chosen_food

#class for all characters, including user
class Character:
    pass
    def __init__(self, name):
        self.day = 1
        self.name = name
        self.love = 0
    def speak(self, message):
        print (self.name.upper() + ":")
        print(message + "\n")
        input()
    def ask(self, question):
        print (self.name.upper() + ":")
        print(question + "\n")
    def decide_speech(self, speech1, speech2):
        announce("decision!!")
        print("\"" + speech1 + "\" (1)\nOR\n\"" + speech2 + "\" (2)")
        line_break()
        self.decision = demand_decision()
        line_break()
    def decide_action(self, action1, action2):
        announce("decision!!")
        print("" + action1 + " (1)\nOR\n" + action2 + " (2)")
        line_break()
        self.decision = demand_decision()
        line_break()
    def love_update(self, n):
        if n > 0:
            print("MORE LOVE! +" + str(n))
        elif n < 0:
            print("LOVE LOWERED... :( " + str(n))
        self.love = self.love + n
        if (self.love > 10):
            self.love = 10
        elif (self.love < 1):
            self.love = 1
        announce("Your love meter is " + str(self.love) + " out of 10.")

#narration tools
def announce(announcement):
    print("** "+ announcement.upper() + " **")
    print("")
    input()

def get_fired():
    announce("You got fired :( That's ok, another capitalist will happily exploit your labor.")
    end_screen()

#screen tools
def line_break():
    print("")

def header(user):
    print ("\033c")
    print(
    '''
   _______  ______    _______  ______   _______  ______    
  |       ||    _ |  |   _   ||      | |       ||    _ |   
  |_     _||   | ||  |  |_|  ||  _    ||    ___||   | ||   
    |   |  |   |_||_ |       || | |   ||   |___ |   |_||_  
    |   |  |    __  ||       || |_|   ||    ___||    __  | 
    |   |  |   |  | ||   _   ||       ||   |___ |   |  | | 
    |___|  |___|  |_||__| |__||______| |_______||___|  |_| 

      ___  _______  _______  __   _______
     |   ||       ||       ||  | |       |   
     |   ||   _   ||    ___||__| |  _____|
     |   ||  | |  ||   |___      | |_____
  ___|   ||  |_|  ||    ___|     |_____  |
 |       ||       ||   |___       _____| |
 |_______||_______||_______|     |_______|
    

    {}
    HINT: PRESS <ENTER> TO ADVANCE
      '''.format("DAY " + str(user.day)))

def end_screen():
    print ("\033c")
    print("GAME OVER")
    print(
    """
     _______  __   __  _______  __    _  ___   _  _______
    |       ||  | |  ||   _   ||  |  | ||   | | ||       |
    |_     _||  |_|  ||  |_|  ||   |_| ||   |_| ||  _____|
      |   |  |       ||       ||       ||      _|| |_____
      |   |  |       ||       ||  _    ||     |_ |_____  |
      |   |  |   _   ||   _   || | |   ||    _  | _____| |
      |___|  |__| |__||__| |__||_|  |__||___| |_||_______|
                   _______  _______  ______
                  |       ||       ||    _ |
                  |    ___||   _   ||   | ||
                  |   |___ |  | |  ||   |_||_
                  |    ___||  |_|  ||    __  |
                  |   |    |       ||   |  | |
                  |___|    |_______||___|  |_|
     _______  ___      _______  __   __  ___   __    _  _______
    |       ||   |    |   _   ||  | |  ||   | |  |  | ||       |
    |    _  ||   |    |  |_|  ||  |_|  ||   | |   |_| ||    ___|
    |   |_| ||   |    |       ||       ||   | |       ||   | __
    |    ___||   |___ |       ||_     _||   | |  _    ||   ||  |
    |   |    |       ||   _   |  |   |  |   | | | |   ||   |_| |
    |___|    |_______||__| |__|  |___|  |___| |_|  |__||_______|


                     Designed by Stel Abrego
                    https://github.com/stelabrego

    """
    )
    quit()


#type safety functions
def demand_input():
    answer = input("> ")
    if answer == "":
        print("Try Again")
        answer = demand_input()
    return answer

def demand_int():
    answer = input("> ")
    try:
        answer = int(float(answer))
    except ValueError:
        print("Try Again")
        answer = demand_int()
    if answer < 10:
        print("Try Again")
        answer = demand_int()
    return int(float(answer))

def demand_decision():
    answer = input("> ")
    if (answer != "1") and (answer != "2"):
        print("Try Again")
        answer = demand_decision()
    return int(float(answer))




#set initial values
manager = Character(random_name())
coworker1 = Character(random_name())
coworker2 = Character(random_name())
user = Character("")

#begin simulation
header(user)
user.love_update(0)
announce("Today, you begin working at Trader Joe's. Meet your new manager, " + manager.name + ".")

#interview
manager.ask("What is your name?")
user.name = demand_input().title()
line_break()

manager.ask("Alright... What are you here to do?")
user.purpose = demand_input().lower()
line_break()

manager.ask("Fair enough.\nNow, what is your favorite movie genre?")
user.movie = demand_input().lower()
line_break()
manager.ask("Great! So you are " + user.name + " who is here to " + user.purpose + " and you like watching " + user.movie + " movies. Welcome to Trader Joe's. You'll fit right in.\nLooks like your first day will be " + current_month + " " + current_day + ".\nOh by the way, how old are you?")
user.age = demand_int()
line_break()

#manager's age reaction
if (user.age < 21):
    manager.speak("Whoa! I saw you sampling the Charles Shaw Zinfandel. That's highly illegal. You are fired. I have no choice.")
    get_fired()
elif (user.age >= 21 and user.age < 30):
    manager.speak("Omg you are a millenial?? Me too omg omg.")
    user.love_update(6)
else:
    manager.speak("That's fantastic.")

#segway
manager.speak("Ok, " + user.name + ". Let's meet your new teammates.")
announce("You and " + manager.name + " walk over to the wine aisles.")

#meet coworker1
coworker1.speak("Hi, my name is " + coworker1.name + ". My favorite ice cream is moose tracks and I use they/them. Nice to meet you.")
user.decide_speech("I love moosetracks too!", "Moosetracks is ok, but what about mint chocolate chip?")

#coworker1 first impression
if user.decision == 1:
    coworker1.speak("You only said that because I did. You're a follower. It's easy to see that. You won't last long here.")
    user.love_update(-3)
elif user.decision == 2:
    coworker1.speak("I respect your courage. Mint is a great flavor. You aren't afraid to be different. I like that. You're fresh. Like the mint you crave. Welcome aboard sailor.")
    user.love_update(3)

#segway
manager.speak(coworker1.name + " is one of our resident wine experts, so don't be afraid to ask questions.")
coworker1.speak("Yeah! Don't be shy. I love talking about wine. I like drinking it even more! Luv 2 Partyyyy!!")
manager.speak("Haha... Don't we all. Alright, let's head into the back and I can show you where the beans are counted.")
announce("You and " + manager.name + " walk through the wine aisle, past the sample center, and through the big red swinging doors on the back wall.")

#Meet coworker2
coworker2.speak("Oh my god!! A new friend!!")
announce("An unfamiliar human hobbles towards you, arms open wide.")
user.decide_action("Embrace incoming hug", "Go for the handshake")

#coworker2 first impression
if user.decision == 1:
    announce("You and " + coworker2.name + " gently quickly embrace.")
    coworker2.speak("The sweet warmth of friendship!")
    user.love_update(1)
elif user.decision == 2:
    coworker2.speak("UHhhh.")
    coworker2.speak("*LAUGHS*")
    coworker2.speak("What are you like a dork or something? Ew.")
    manager.speak("Oh my god " + user.name + ", are you alright?")
    manager.speak("... because you just got roasted so badly lmaooo")
    coworker2.speak("See you later, hand shaker!")
    user.love_update(-2)

#shift activities
stocking_food = new_food()
manager.speak("What an exciting first day! Anyway, let's get you started with stocking, " + user.name + ". Ooo look, it's a box of our " + stocking_food[0] + "! Yum yum.")
announce(manager.name + " shows you how to stock the shelves for an hour or so, and eventually you're able to do it yourself. Another hour goes by and " + manager.name + ", your manager, returns.")
manager.ask("I think that's enough for today, " + user.name + ". How do you think you did?")
self_eval = demand_input()
line_break()

#judgement
if user.love < 5:
    manager.speak("That's interesting.")
    announce("there is a long, awkward silence")
    manager.speak(user.name + ", I've got to keep it 100 with you. You are the slowest " + stocking_food[1] + " stocker I have ever trained. You only emptied one box in an hour,\nand you even put them on the wrong shelf. I'm not sure you're going to be a good fit here. \nWhy don't you just go home and not bother coming in tomorrow.")
    get_fired()
else:
    manager.speak("I think you did a great job. The " + stocking_food[1] + " section looks beautiful. \nYou're a friendly person, and I'm glad you're our new team member. See you tomorrow!")
    announce("day 1 completed")

#day 2
#todo

end_screen()
