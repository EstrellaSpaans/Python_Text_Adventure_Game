#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# The DocString
"""
    DocString:
    
    A) Introduction:
    This game is inspired by the Wizarding World is a fantasy universe 
    centered on a tales by J.K. Rowling. The game contains references to 
    the details of the original Harry potter stories. The game focusses on 
    a person being selected to go an a journey with a friend to discover the 
    American Wizarding community. 

    Section 1: Start the game
    Section 2: Decide whether or to read the letter.
    Section 3: Decide if you are ok/
    Section 4: Decide how to defeat the spider.
    Section 5: Decide what item you will pick. 
    Section 6: Sorting ceremony

    
    B) Known Bugs and/or Errors:
    None.
    
"""

#importing required packages
import time
from datetime import date 
from sys import exit

#creating a function when people exit the 
def fail():
    # set colors for formatting
    OKBLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
    #Wait before end message appear. This gives time to read the previous message.
    time.sleep(3)
    
    print(BOLD + f"""
GAMED HAS ENDED. TOO BAD """+ ENDC)
    print(f""")
{'-'*60}
Wanna know more about the American Wizarding World?
check out the website: https://www.wizardingworld.com/writing-by-jk-rowling/ilvermorny""" )
    #exit the game with function
    exit()

#creating a function to finish the game
def ending(): 
    # set colors for formatting
    OKBLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
    ##Wait before end message appear. This gives time to read the previous message.
    time.sleep(3)
    
    #ending message 
    print(BOLD + f"""
{'-'*60}   
"Congratulations! You have finished the game!"""+ ENDC)
    print(f"""
{'-'*60}
Wanna know more about the American Wizarding World?
check out the website: https://www.wizardingworld.com/writing-by-jk-rowling/ilvermorny""")
    
    #exit the game with function
    exit()

#Section 1: (start_game) Introduction
def start_game(): 
    # set colors for formatting
    OKBLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
    print(BOLD + """
Hello there! Press enter to play this Wizarding Text Adventure game""" + ENDC)

    #starting prompt
    start_game = input(prompt = "Press ENTER to START THE GAME\n")

    # Getting information to feed the game
    print(f"""
{'-'*60}

Awesome, great! 
             """)

    #delay response
    time.sleep(1)

    print(BOLD + """
Before we actually start, I do need some information: """+ ENDC)

     #creating Globals + inputs for in the game
    global Player_name
    Player_name = input(prompt = "1. What is your name? - ")
    
    global Friend_name
    Friend_name = input(prompt = "2. What is the name of your friend that is joining you on this journey? - ")
    
    global University
    University = input(prompt = "3. What university did you OR are you currently attending? - ")
    
    global Professor
    Professor = input(prompt = "4. Who is OR was your favourite professor in school? - ")
    
    #capitilize these inputs
    Player_name = Player_name.capitalize()
    Friend_name = Friend_name.capitalize()
    University = University.title()
    Professor = Professor.capitalize()
    
    #setting up current date
    today = date.today()

    #delay the response 
    time.sleep(1)
    
    # Introduction text
    print(f"""
    {'-'*60}

Imagine the following: 

It is {today} and the city is just waking from its slumber as you prepare to \n go to the class at {OKBLUE + University + ENDC} in Cambridge, MA.
The Boston blue skys give way to the most unnatural of greys as you approach {OKBLUE + University + ENDC}. 

The balmy day is suddenly bitingly cold on the verge of snow fall. 
You look up, waiting for the snowflakes..... 
""")
    
    #continue the game
    enter = input(prompt = "Enter to continue")
    
    print(f"""
{'-'*60}
Instead, a Letter falls out of the sky with your name on it: 

          ________________________
         |\                      /|
               {OKBLUE + Player_name + ENDC}     
         | /\__________________/\ | 
         |/                      \| 
         |________________________| 

{'-'*60} 
""") 
    
    #going to section 2
    letter_decision()

#Section 2: letter_decision - first decision
def letter_decision(): 
    # set colors for  formatting
    OKBLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
    #creating a list 
    decision1 = []
    
    #continue the game
    enter = input(prompt = "Enter to continue")
    
    #printing the choices
    print(f"""
It lands perfectly into your hands. The python lecture starts in a few minutes.
    """)
    print(BOLD + f""" What do you do? """ + ENDC)
    print(f"""
    1) Open the letter, you are too curious! 
    2) Put it in your backpack so that you don't miss class. 
    3) You throw it in the bin because it is not real.  
    4) You will wait to show it later to {OKBLUE + Friend_name + ENDC}!
        """)
    
    #using a while loop to determine what to do with the input of choice    
    while True: 
        #asking the user for an input
        first_choice = str(input(prompt ="What is your choice?  - "))
        #making sure that all the inputs are lower case
        first_choice = first_choice.lower()
        #transform the input into a list
        splitted_first_choice = first_choice.split()
        
        #defining possible keywords in a list for each option
        option_1_1 = ['1','open','letter','are','too','curious', 'a']
        option_1_2 = ['2','put','backpack',"don't",'dont','miss','class', 'b']
        option_1_3 = ['3','throw','bin','is','not','because','real', 'c']
        option_1_4 = ['4','will','wait','show','later', 'd']
        option_1_4.append(Friend_name.lower())

        #checking if any of these elements match with the user input
        check_option1_1 = any(elem in splitted_first_choice for elem in option_1_1)
        check_option1_2 = any(elem in splitted_first_choice for elem in option_1_2)
        check_option1_3 = any(elem in splitted_first_choice for elem in option_1_3)
        check_option1_4 = any(elem in splitted_first_choice for elem in option_1_4)

        #checks the first option: if met, it breaks and prints + adding the choice to a list
        if check_option1_1:
            decision1.append(1)
            print(f"""
{'-'*60}
Alright! Let's open the letter. You call {OKBLUE + Friend_name + ENDC} over, who was waiting for you in the hall. 
You rip the letter open and....""")
            break

        #checks the second option: if met, it breaks and prints + adding the choice to a list    
        elif check_option1_2:
            decision1.append(2)
            python_class_subject = input(prompt="Hold on.. What are we learning in class today? Enter a python subject - ")
            print(f"""
{'-'*60}
Class turned ou to be boring. Professor {OKBLUE + Professor + ENDC} is talking about "{OKBLUE + python_class_subject + ENDC}" AGAIN. 
When there was a break you and {OKBLUE + Friend_name + ENDC} could finally open the letter...""")
            break

        #checks the third option: if met, it breaks and prints + adding the choice to a list
        elif check_option1_3:
            decision1.append(3)
            print(f"""
{'-'*60}
So throw it in the bin and you enter the {OKBLUE + University + ENDC} building approaching {OKBLUE + Friend_name + ENDC} but then... 

The next moment, thirty or forty letters came pelting out of the door from outside like bullets. 
You ducked, but {OKBLUE + Friend_name + ENDC} leapt into the air trying to catch one.""")
            break

        #checks the fourth option: if met, it breaks and prints + adding the choice to a list
        elif check_option1_4:
            decision1.append(4)
            print(f"""
{'-'*60}
You rush inside the building where {OKBLUE + Friend_name + ENDC } is waiting for you. You show {OKBLUE + Friend_name + ENDC} the letter. """) 
            break 

        #checks all other characters entered: if met, it ask user for input again.     
        else:
            print(f"""
{'-'*60}

THAT IS NOT A VALID INPUT! 

Hmmm... Perhaps it is easier to use one of the numbers (1, 2, 3 or 4). 

    Here are the options again: 
        1) Open the letter, you are too curious! 
        2) Put it in your backpack so that you don't miss class. 
        3) You throw it in the bin because it is not real.  
        4) You will wait to show it later to {OKBLUE + Friend_name + ENDC}!""")
            
    #outro
    print(f"""
While you and {OKBLUE + Friend_name + ENDC} read the letter, you walk towards the elevator..""")
    
# going to section 3 + pass decision
    opening_letter(decision1)

#Section 3: Opening letter & start the quest
def opening_letter(decision1):
    # set colors for  formatting
    OKBLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
    #empty list for decisions + mention decision 1 to pass. 
    decision3 = []
    decision1
    
    #continue story
    enter = input(prompt = "enter to continue")
    #dialog of story
    print(BOLD + f"""
{'-'*60}
         _________________________________
        |                                 |
           CONGRATULATIONS {OKBLUE + Player_name + ENDC}, 
        |                                 |
        |  You got accepted into:         |
        |                                 |
        |  Ilvermorny School of           |
        |  Witchcraft and Wizardry,       |
        |  the greatest North American    |
        |  school of magic.               |
        |                                 |
        |  Please get to our school       |
        |  at Mount Greylock in           |
        |  in Massachusetts.              |
        |                                 |
        |  Kind Regards,                  |
        |                                 |
        |  Headmaster,                    |
        |                                 |
        |  Agilbert Fontaine              |
        |_________________________________|
 
{'-'*60}
    """+ ENDC)
    #continue story
    enter = input(prompt = "enter to continue")
    print(f"""
**PING* The elevator arrives. As you step in, the door forcefully collides behind you as the elevator plummets
through the depths of the building at warp speed.""")
    
    #continue story
    enter = input(prompt = "enter to continue")
    
    print(f"""
{'-'*60}
In an instant before you can comprehend the situation, you and {OKBLUE + Friend_name + ENDC} 
are spit out of the elevator.... """)
    print(BOLD + f""" 
    Are you ok? """ + ENDC)
    
    #input after elevator crash. 
    while True:
        second_choice = input(prompt = f"""
    1. Yes
    2. No  - """)
        
        second_choice = second_choice.lower()

        if second_choice == "yes" or second_choice == "y" or second_choice == "yup" or second_choice == "1" or second_choice == "a":
            print(f"""
How is this possible to be in a FOREST!! It must be magic. ""{OKBLUE + Friend_name + ENDC}", are you ok? 
Your friend stands up and nods yes..""")
            break 

        #check option No
        elif second_choice == "no" or second_choice == "n" or second_choice == "nope" or second_choice == "2" or second_choice == "b":
            print(f"""
How is this possible to be in a FOREST!!

A wave of nausea hits and... BLEURP... Your breakfast came out. {OKBLUE + Friend_name + ENDC} asks "Are you ok?" 

"I guess now I am" """)
            break

        #checks all other characters entered: if met, it ask user for input again.   
        else:
            print(f"""
{'-'*60}

OOPS, THAT IS NOT A VALID INPUT! 
Try again. Just a simple yes or no will do.""")
    
    #continue story
    enter = input(prompt = "enter to continue")
    
    #continue story
    print(f"""
{'-'*60}
    
*Crack* A big GIANT Acromantula spider has appeared!""")
    
    #print spider sign               
    print(BOLD + r""" 
    
      / _ \
    \_\(_)/_/
     _//o\\_ 
      /   \
    """ + ENDC) 
    
    #continue story
    enter = input(prompt = "enter to continue")
    
    print(f"""
{'-'*60}
You grab your backpack and confusingly, you grab a WAND out of your pocket? 

{OKBLUE + Friend_name + ENDC} says " TheMagical Congress of the United States of America"
does not allow us to have a wand before being trained!" """)
    
     #continue story
    enter = input(prompt = "enter to continue")
    
    print(f"""
{'-'*60}
The Acromantula STARTED TO SCREAM!!
You answer" Well we can probably use it now at least".....""") 
    
    #Presenting options for next decisions
    print(BOLD + f"""
    You have the following choices:"""+ ENDC)
    print(f"""
        1) There are too many options, so you try 7 spells. 
        2) Think logically and say "Immobulus".
        3) Run towards the creature and mumble something random.
        4) Stand in front of {OKBLUE + Friend_name + ENDC} and cast a protection charm!
        5) Do nothing and pee your pants.""") 
    
    #using a while loop to determine what to do with the input of choice    
    while True: 
        #asking the user for an input
        third_choice = str(input(prompt ="What is your choice?  - "))
        #making sure that all the inputs are lower case
        third_choice = third_choice.lower()
        #transform the input into a list
        splitted_third_choice = third_choice.split()

        #defining possible keywords in a list for each option
        option_3_1 = ['1','7','there','are','too','many','options','try','spell','spells', 'a']
        option_3_2 = ['2','think','logically','say','immobulus','b']
        option_3_3 = ['3','run','towards','creature','mumble','something','random', 'c']
        option_3_4 = ['4','stand','in','front','of','cast','protection','charm', 'd']
        option_3_5 = ['5','do','nothing','pee','your','pants', 'e']
        option_3_4.append(Friend_name.lower())

        #checking if any of these elements match with the user input
        check_option3_1 = any(elem in splitted_third_choice for elem in option_3_1)
        check_option3_2 = any(elem in splitted_third_choice for elem in option_3_2)
        check_option3_3 = any(elem in splitted_third_choice for elem in option_3_3)
        check_option3_4 = any(elem in splitted_third_choice for elem in option_3_4)
        check_option3_5 = any(elem in splitted_third_choice for elem in option_3_5)

        #checks the first option: if met, it breaks and prints
        if check_option3_1:
            decision3.append(1)
            print(f"""
{'-'*60}
You and {OKBLUE + Friend_name + ENDC} get pushed towards the ground and your wand flies into the air.. 
Did it work?""")
            break

        #checks the second option: if met, it breaks and prints      
        elif check_option3_2:
            decision3.append(2)
            print(f"""
{'-'*60}
The Acromantula freezes and was not able to move! 
In surprise, you drop the wand. The spell worked!""")
            break

        #checks the third option: if met, it breaks and prints 
        elif check_option3_3:
            decision3.append(3)
            print(f"""
{'-'*60}
The Acromantula attacks and you fly into the air, landing on top of {OKBLUE + Friend_name + ENDC}. 
Where did the wand go?""")
            break

        #checks the fourth option: if met, it breaks and prints 
        elif check_option3_4:
            decision3.append(4)
            print(f"""
{'-'*60}
The Acromantula approaches but something blocks his way. 
In surprise, you drop the wand. The protection charm worked!""") 
            break 

        elif check_option3_5: 
            print(f"""
{'-'*60}
The Acromantula approaches you and stabs his long leg right through your chest. You bleed out....""") 
            fail()
            break  
            
        #checks all other characters entered: if met, it ask user for input again.     
        else:
            print(f"""
{'-'*60}

OOPS, THAT IS NOT A VALID INPUT! This Python Game can in most cases identify what you try to say. 
Hmmm... Perhaps it is easier to use one of the numbers this time? (1, 2, 3 or 4)

    Here are the options again: 
        1) There are too many options, so you try 7 spells. 
        2) Think logically and say "Immobulus".
        3) Run towards the creature and mumble something random.
        4) Stand in front of {OKBLUE + Friend_name + ENDC} and cast a protection charm!
        5) Do nothing and pee your pants.""")

# Going to section 4
    getting_to_castle(decision1, decision3)

#Section 4: Opening)letter & start quest - second decision            
def getting_to_castle(decision1, decision3):
    # set colors for  formatting
    OKBLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
    #continue story
    enter = input(prompt = "enter to continue")
    #dialog of story
    print(f"""
{'-'*60}

"WHAT ARE YOU DOING HERE IN MY FOREST!" 
    
You and {OKBLUE + Friend_name + ENDC} look up. The Acromantula could speak! 
     
"We were just trying to get to Ilvermorny", you replied. 
"We received an acception letter" added {OKBLUE + Friend_name + ENDC} quickly. 
      """)
    
    #continue story
    enter = input(prompt = "enter to continue")
    
    print(f"""
{'-'*60}
    
"If I get you to the school, do you promise to leave my forest alone?" says the Acromantula.""")
    print(BOLD + f"""
    What will you answer?""" + ENDC)
          
    #decision 3: will you promise? 
    #using a while loop to determine what to do with the input of choice
    while True: 
        fourth_choice = str(input(prompt =f""" 
        Yes or No? - """))
        fourth_choice = fourth_choice.lower()
        
        #check option yes
        if fourth_choice == "yes" or fourth_choice == "y" or fourth_choice == "yup" or fourth_choice == "j" or fourth_choice == "a":
            print(f"""
{'-'*60}
HMMM... Do I believe you? Alright then! """)
            break 
        
        #check option no
        elif fourth_choice == "no" or fourth_choice == "n" or fourth_choice == "nope" or fourth_choice == "b":
            print(f"""
WRONG CHOICE! 

The Acromantula approaches you and stabs his long leg right through your chest. You bleed out....""")
            fail()
            break
        
        #checks all other characters entered: if met, it ask user for input again.  
        else:
            print(f"""
{'-'*60}

OOPS, THAT IS NOT A VALID INPUT! 
Try again. Just a simple yes or no will do""")
    
    #mention decision to pass over 
    decision1
    decision3
    
   #going to section 5 
    choosing_object(decision1, decision3)
    
#Section 5: Choosing an object to determine legency. 
def choosing_object(decision1, decision3): 
    # set colors for  formatting
    OKBLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
    # empty list for decision 5 + mention other lists: decision1 and decision3
    decision5 = []
    decision1
    decision3
    
    #continue story
    enter = input(prompt = "enter to continue")
    
    #dialog of story
    print(f"""
{'-'*60}
    
The Acromantula magically openend a portal. 
Within the portal you could see the castle on top of the hill!! """)
    print(r"""                          
                        |>>>      _  _ _  _         |>>>
                        |         |;| |;| |;|       |
                    _  _|_  _    \\.    .  /    _  _|_  _
                   |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|
                   \\..      /    ||;   . |    \\.    .  /
                    \\.  ,  /     ||:  .  |     \\:  .  /
                     ||:   |_   _ ||_ . _ | _   _||:   |
                     ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                     ||:   ||.    .     .      . ||:  .|
                     ||: . || .     . .   .  ,   ||:   |       \
                     ||:   ||:  ,  _______   .   ||: , |            /`\
                     ||:   || .   /+++++++\    . ||:   |
                     ||:   ||.    |+++++++| .    ||: . |
                  __ ||: . ||: ,  |+++++++|.  . _||_   |""")
   
    #continue story
    enter = input(prompt = "enter to continue")
    print(f"""
{'-'*60}
    
You both enter into the portal and arrived at the school! 
"Can you believe {OKBLUE + Friend_name + ENDC} that we are finally here?" 
    
As you together proceed to the entrance of the building, you get seperated from {OKBLUE + Friend_name + ENDC}.""")
    
    #continue story
    enter = input(prompt = "enter to continue")
    print(f"""
{'-'*60}
We are asked to enter a dark room and pick one of the four items to determine your destiny.""")
    
    print(BOLD + f""" 
    What will you choose? """ + ENDC)
    
    print(f"""
        1) A rustic box forgotten by time. 
        2) An ancient spell book locked by a skeleton hand. 
        3) A handcrafted dagger with a hilt of gold. 
        4) A silver ring with a Rose Quartz stone.""")
    
    #using a while loop to determine what to do with the input of choice    
    while True: 
        #asking the user for an input
        fifth_choice = str(input(prompt ="What is your choice?  - "))
        #making sure that all the inputs are lower case
        fifth_choice = fifth_choice.lower()
        #transform the input into a list
        splitted_fifth_choice = fifth_choice.split()

        #defining possible keywords in a list for each option
        option_5_1 = ['1','rustic','box','forgotten','by','time','a']
        option_5_2 = ['2','ancient','spell','book','locked','by','skeleton','hand','b']
        option_5_3 = ['3','handcrafted','dagger','hint','gold','c']
        option_5_4 = ['4','silver','ring','rose','Quartz','stone','d']

        #checking if any of these elements match with the user input
        check_option5_1 = any(elem in splitted_fifth_choice for elem in option_5_1)
        check_option5_2 = any(elem in splitted_fifth_choice for elem in option_5_2)
        check_option5_3 = any(elem in splitted_fifth_choice for elem in option_5_3)
        check_option5_4 = any(elem in splitted_fifth_choice for elem in option_5_4)
    

        #checks the first option: if met, it breaks and prints
        if check_option5_1:
            decision5.append(1)
            print(f"""
{'-'*60}
Now that you have chosen, let's go to sorting ceremony. Here you will be sorted into your house""")
            break

        #checks the second option: if met, it breaks and prints      
        elif check_option5_2:
            decision5.append(2)
            print(f"""
{'-'*60}
Now that you have chosen, let's go to sorting ceremony. Here you will be sorted into your house""")
            break

        #checks the third option: if met, it breaks and prints 
        elif check_option5_3:
            decision5.append(3)
            print(f"""
{'-'*60}
Now that you have chosen, let's go to sorting ceremony. Here you will be sorted into your house""")
            break

        #checks the fourth option: if met, it breaks and prints 
        elif check_option5_4:
            decision5.append(4)
            print(f"""
{'-'*60}
Now that you have chosen, let's go to sorting ceremony. Here you will be sorted into your house.""")
            break
            
        #checks all other characters entered: if met, it ask user for input again.     
        else:
            print(f"""
{'-'*60}

OOPS, THAT IS NOT A VALID INPUT! Hmmm... 
Perhaps it is easier to use one of the numbers this time? (1, 2, 3 or 4)

    You have the following choices: 
        1) A rustic box forgotten by time. 
        2) An ancient spell book locked by a skeleton hand. 
        3) A handcrafted dagger with a hilt of gold. 
        4) A silver ring with a Rose Quartz stone.""")

    #moving on to last section 
    sorting_ceremony(decision1, decision3, decision5)
    
#Section 5: determine which house the player gets sorted into. 
def sorting_ceremony(decision1, decision3, decision5):
    # set colors for  formatting
    OKBLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
    #aggregating all lists
    decision = []
    decision.extend(decision1)
    decision.extend(decision3)
    decision.extend(decision5)
    
    #continue story
    enter = input(prompt = "enter to continue")
    
    #dialog of story
    print(f"""

The Gordian Knot symbol in the ground determines which house you belong to. 
You get in line waiting to for when your name get called out. """)
    
    enter = input(prompt = "enter to continue")
    
    print(f"""
{'-'*60}
    
{OKBLUE + Player_name + ENDC} It is your turn.

In silence you wait for the the enchanted carvings to react....

{'-'*60}
"Your house is....""")
    
    time.sleep(2)
    
    # defining possible outcomes & belonning needed variables 
    Thunderbird = "Thunderbird"
    outcome1_1 = [1,1,1]
    outcome1_2 = [1,1,2]
    outcome1_3 = [1,2,1]
    outcome1_4 = [2,1,1]
    outcome1_5 = [1,1,3]
    outcome1_6 = [1,3,1]
    outcome1_7 = [3,1,1]
    outcome1_8 = [1,1,4]
    outcome1_9 = [1,4,1]
    outcome1_10 = [4,1,1]
    
    Horned_Serpent = "Horned Serpent"
    outcome2_1 = [2,2,2]
    outcome2_2 = [2,2,1] 
    outcome2_3 = [2,2,3]
    outcome2_4 = [2,2,4]
    outcome2_5 = [2,1,2] 
    outcome2_6 = [1,2,2]
    outcome2_7 = [2,3,2]
    outcome2_8 = [3,2,2]
    outcome2_9 = [2,4,2]
    outcome2_10 = [4,2,2]
    
    Wampus = "Wampus"
    outcome3_1 = [3,3,3]
    outcome3_2 = [3,3,1]
    outcome3_3 = [3,1,3]
    outcome3_4 = [1,3,3]
    outcome3_5 = [3,3,2]
    outcome3_6 = [3,2,3]
    outcome3_7 = [2,3,3]
    outcome3_8 = [3,3,4]
    outcome3_9 = [3,4,3]
    outcome3_10 = [4,3,3]

    Pukwudgie = "Pukwudgie"
    outcome4_1 = [4,4,4]
    outcome4_2 = [4,4,1]
    outcome4_3 = [4,1,4]
    outcome4_4 = [1,4,4]
    outcome4_5 = [4,4,2]
    outcome4_6 = [4,2,4]
    outcome4_7 = [2,4,4]
    outcome4_8 = [4,4,3]
    outcome4_9 = [4,3,4]
    outcome4_10 =[3,4,4]
    
    Special = "Special"
    Outcome5_1 = [1,2,3]
    Outcome5_2 = [1,3,4]
    Outcome5_3 = [1,4,2]
    Outcome5_4 = [1,3,2]
    Outcome5_5 = [1,4,3]
    Outcome5_6 = [1,2,4]
    Outcome5_7 = [2,3,4]
    Outcome5_8 = [2,3,1]
    Outcome5_9 = [2,4,1]
    Outcome5_10 = [2,4,3]
    Outcome5_11 = [2,1,4]
    Outcome5_12 = [2,1,3]
    Outcome5_11 = [3,1,2]
    Outcome5_12 = [3,1,4]
    Outcome5_13 = [3,2,1]
    Outcome5_14 = [3,2,4]
    Outcome5_15 = [3,4,1]
    Outcome5_16 = [3,4,2]
    Outcome5_17 = [4,1,2]
    Outcome5_18 = [4,1,3]
    Outcome5_19 = [4,2,3]
    Outcome5_20 = [4,2,1]
    Outcome5_21 = [4,3,1]
    Outcome5_22 = [4,3,2]

    #If statement to determine which house
    #if the list matches with the first set of outcomes, the house is Thunderbird
    if decision == outcome1_1 or decision == outcome1_2 or decision == outcome1_3 or decision == outcome1_4 or decision == outcome1_5 or decision == outcome1_6 or decision == outcome1_7 or decision == outcome1_8 or decision == outcome1_9 or decision == outcome1_10: 
        print(f"""       
{BOLD + OKBLUE + Thunderbird + ENDC}! 
        
"Glitter powder was shooted into the air!"
        
The Thunderbird is the “soul” and “favors adventurers,” has the power to bring storms. 
So it’s no wonder that you are associated with the soul!
{OKBLUE + Friend_name + ENDC} got sorted into {OKBLUE + Thunderbird + ENDC} as well!""")
        
    #if the list matches with the second set of outcomes, the house is Horned Serpent
    elif decision == outcome2_1 or decision == outcome2_2 or decision == outcome2_3 or decision == outcome2_4 or decision == outcome2_5 or decision == outcome2_6 or decision == outcome2_7 or decision == outcome2_8 or decision == outcome2_9 or decision == outcome2_10:
        print(f"""
{BOLD + OKBLUE + Horned_Serpent + ENDC}! 
        
The crystal set into the floor lit up! 
        
The Horned Serpent is said to represent the mind of a wizard, and favors scholars. 
So it’s no wonder that you are associated with the mind!
{OKBLUE + Friend_name + ENDC} got sorted into {OKBLUE + Horned_Serpent + ENDC} as well!""")
        ending()
        
    #if the list matches with the second set of outcomes, the house is Wampus   
    elif decision == outcome3_1 or decision == outcome3_2 or decision == outcome3_3 or decision == outcome3_4 or decision == outcome3_5 or decision == outcome3_6 or decision == outcome3_7 or decision == outcome3_8 or decision == outcome3_9 or decision == outcome3_10:    
        print(f"""    
{OKBLUE + Wampus + ENDC}!
    
A loud roar appeared! 
        
Wampus represents the body of a wizard and favors warriors in all shapes and sizes.  
So it’s no wonder that you are associated with the body!
{BOLD + OKBLUE + Friend_name + ENDC} got sorted into {OKBLUE + Wampus + ENDC} as well!""")
        ending()

    #if the list matches with the second set of outcomes, the house is Pukwudgie   
    elif decision == outcome4_1 or decision == outcome4_2 or decision == outcome4_3 or decision == outcome4_4 or decision == outcome4_5 or decision == outcome4_6 or decision == outcome4_7 or decision == outcome4_8 or decision == outcome4_9 or decision == outcome4_10:    
        print(f"""
{BOLD + OKBLUE + Pukwudgie + ENDC}!
    
An arrow flew into the sky! 
        
The Pukwudgie, represents the heart of a wizard, and favors healers. 
So it’s no wonder that you are associated with the mind! 
{OKBLUE + Friend_name + ENDC} got sorted into {OKBLUE + Pukwudgie + ENDC} as well!""")
        ending()
    
    #if the list matches with the second set of outcomes, the house is special
    elif decision == Outcome5_1 or decision == Outcome5_2 or decision == Outcome5_3 or decision == Outcome5_4 or decision == Outcome5_5 or decision == Outcome5_6 or decision == Outcome5_7 or decision == Outcome5_8 or decision == Outcome5_9 or decision == Outcome5_10 or decision == Outcome5_11 or decision == Outcome5_12 or decision == Outcome5_13 or decision == Outcome5_14 or decision == Outcome5_15 or decision == Outcome5_16 or decision == Outcome5_17 or decision == Outcome5_18 or decision == Outcome5_19 or decision == Outcome5_20 or decision == Outcome5_21 or decision == Outcome5_22:
        print(f"""     
Ohhh.. 

You are {BOLD + OKBLUE + Special + ENDC}!
        
Only once in a 100 years, someone like you appears, someone that has all qualities: the body, the mind, the soul, and the heart. 
You get to be your own house! """)
        ending()
    
    #IF THERE IS A MISTAKE SOMEHOW WHEN LISTS DO NOT MATCH (OR) IF YOU TRIED TO BREAK MY CODE.   
    else:
        print(f"""
Oops, something went wrong with the game? Did you perhaps try to break my code??
If so, it is not appreciated. Please play the game correctly. 

Did you enter something weird instead? No problem. play the game again and see let's determine your house!""")
        #go to fail function
        fail()
        
start_game()


# In[ ]:





# In[ ]:




