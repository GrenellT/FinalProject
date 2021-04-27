import random
import time

#Schnoz's Moves
def Gamble():
    print("Schnoz chooses to gamble on his attack!")
    x = random.randint(1,2)
    time.sleep(2)
    if x == 1:
        print("The odds were rigged against Schnoz!")
        print("Schnoz misses his attack!")
        damage = 0
    if x == 2:
        print("The odds were in Schnoz's favor!")
        a = random.randint(0,20)
        damage = 50 + a
        time.sleep(2)
        if damage <= 55:
            print("Weak attack.")
            print("Schnoz's attack did", damage, "damage!")
        elif 56 < damage <= 65:
            print("Average attack.")
            print("Schnoz's attack did", damage, "damage!")
        elif damage > 65:
            print("Strong attack!")
            print("Schnoz's attack did", damage, "damage!")
    return damage

def QuickCombo():
    print("Schnoz chooses to use his speed to his advantage!")
    total = 0
    time.sleep(2)
    for i in range(3):
        x = random.randint(0,15)
        damage = 10 + x
        total = total + damage
        print("On attack", i+1, "of the combo, Schnoz did", damage, "damage!")
        time.sleep(2)
    if total <= 30:
        print("Weak attack.")
        print("Schnoz's combo did a total of", total, "damage!")
    elif 30 < total <= 60:
        print("Average attack.")
        print("Schnoz's combo did a total of", total, "damage!")
    elif total > 60:
        print("Strong attack!")
        print("Schnoz's combo did a total of", total, "damage!")
    return total

def WeeMan():
    print("Schnoz releases the built up anger he has due to his height!")
    x = random.randint(1,10)
    time.sleep(2)
    if x <= 2:
        a = random.randint(0,20)
        damage = 10 + a
        print("Weak attack.")
        print("Schnoz's attack did", damage, "damage!")
    elif 2 < x < 7:
        a = random.randint(21,35)
        damage = 10 + a
        print("Average attack.")
        print("Schnoz's attack did", damage, "damage!")
    elif x >= 7:
        a = random.randint(36,50)
        damage = 10 + a
        print("Strong attack!")
        print("Schnoz's attack did", damage, "damage!")
    return damage

#Trundle's Moves

def Rest():
    print("Trundle stays in bed in order to regain health!")
    x = random.randint(0,35)
    health = 25 + x
    time.sleep(2)
    print("Trundle was able to regain", health, "health!")
    return health
    
def EggThrow():
    print("Trundle gets the urge to throw an egg at his opponent!")
    x = random.randint(1,5)
    time.sleep(2)
    if x == 1:
        y = random.randint(5,10)
        damage = 5 + y
        print("Weak attack.")
        print("Trundle's attack did", damage, "damage!")
    if x == 2 or x == 3:
        y = random.randint(11,25)
        damage = 5 + y
        print("Average attack.")
        print("Trundle's attack did", damage, "damage!")
    if x == 4 or x == 5:
        y = random.randint(26,40)
        damage = 5 + y
        print("Strong attack!")
        print("Trundle's attack did", damage, "damage!")
    return damage

def Tackle():
    print("Trundle tries to play rugby with his opponent!")
    x = random.randint(1,10)
    time.sleep(2)
    if x == 1 or x == 2 or x == 3 or x == 4:
        y = random.randint(0,10)
        damage = 20 + y
        print("Weak attack.")
        print("Trundle's attack did", damage, "damage!")
    if x == 5 or x == 6 or x == 7 or x == 8:
        y = random.randint(11,25)
        damage = 20 + y
        print("Average attack.")
        print("Trundle's attack did", damage, "damage!")
    if x == 9 or x == 10:
        y = random.randint(26, 40)
        damage = 20 + y
        print("Strong attack!")
        print("Trundle's attack did", damage, "damage!")
    return damage

#Fupa's Moves

def InvestPlayer():
    global OpponentHealth
    time.sleep(1)
    print("")
    print("Fupa decides to invest his energy into a big attack!")
    x = random.randint(0,10)
    damage = 10 + x
    time.sleep(1)
    print("Fupa's attack did", damage, "damage!")
    OpponentHealth = OpponentHealth - damage
    print(Opponent, "'s health is now at ", OpponentHealth, sep="")
    if OpponentHealth <= 0:
        damage = 0
        return damage
    else:
        CPUTurn(Opponent)
        if CharacterHealth <= 0:
            damage = 0
            return damage
        else:
            time.sleep(1)
            print("")
            print("Fupa continues to invest!")
            y = random.randint(0,15)
            damage = 30 + y
            time.sleep(1)
            print("Fupa's attack did", damage, "damage!")
            OpponentHealth = OpponentHealth - damage
            print(Opponent, "'s health is now at ", OpponentHealth, sep="")
            if OpponentHealth <= 0:
                damage = 0
                return damage
            else:
                CPUTurn(Opponent)
                if CharacterHealth <= 0:
                    damage = 0
                    return damage
                else:
                    time.sleep(1)
                    print("")
                    print("Fupa decides to cash out on a big attack!")
                    z = random.randint(0,25)
                    damage = 50 + z
                    time.sleep(1)
                    print("Fupa's attack did", damage, "damage!")
                    return damage

def InvestCPU():
    global CharacterHealth
    print("Fupa decides to invest his energy into a big attack!")
    x = random.randint(0,10)
    damage = 10 + x
    print("Fupa's attack did", damage, "damage!")
    CharacterHealth = CharacterHealth - damage
    print(Character, "'s health is now at ", Character, sep="")
    if CharacterHealth <= 0:
        damage = 0
        return damage
    else:
        PlayerTurn(Character)
        if OpponentHealth <= 0:
            damage = 0
            return damage
        else:
            time.sleep(1)
            print("")
            print("Fupa continues to invest!")
            y = random.randint(0,15)
            damage = 30 + y
            print("Fupa's attack did", damage, "damage!")
            CharacterHealth = CharacterHealth - damage
            print(Character, "'s health is now at ", CharacterHealth, sep="")
            if CharacterHealth <= 0:
                damage = 0
                return damage
            else:
                PlayerTurn(Character)
                if OpponentHealth <= 0:
                    damage = 0
                    return damage
                else:
                    print("Fupa decides to cash out on a big attack!")
                    z = random.randint(0,25)
                    damage = 50 + z
                    print("Fupa's attack did", damage, "damage!")
                    return damage

def Pressed():
    print("Fupa gets mad because his ego got hurt!")
    x = random.randint(1,10)
    time.sleep(2)
    if x <= 4:
        a = random.randint(5,25)
        damage = 10 + a
        print("Weak attack.")
        print("Fupa's attack did", damage, "damage!")
    elif 4 < x < 9:
        a = random.randint(26,40)
        damage = 10 + a
        print("Average attack.")
        print("Fupa's attack did", damage, "damage!")
    elif x >= 9:
        a = random.randint(41,55)
        damage = 10 + a
        print("Strong attack!")
        print("Fupa's attack did", damage, "damage!")
    return damage

def Skullcrusher():
    print("Fupa decides to get a workout in by doing skullcrushers!")
    x = random.randint(1,5)
    time.sleep(1)
    print("Fupa begins to crush his opponent's skull!")
    damage = 0
    for i in range(x):
        time.sleep(1)
        print("Fupa continues to crush his opponent's skull, doing 15 damage.")
        damage = damage + 15
    time.sleep(1)
    print("Fupa stops crushing his opponent's skull.")
    print("Fupa's attack did", damage, "damage!")
    return damage
    

#Player Characters

def PlayerTrundle():
    global CharacterHealth
    global OpponentHealth
    time.sleep(3)
    print("")
    print("It is Trundle's turn to attack!")
    time.sleep(1)
    SelectMove(Character)
    if Move == "1":
        health = int(Rest())
        CharacterHealth = CharacterHealth + health
        print("Trundle's health is now at", CharacterHealth)
    if Move == "2":
        damage = int(EggThrow())
        OpponentHealth = OpponentHealth - damage
        print(Opponent, "'s health is now at ", OpponentHealth, sep="")
    if Move == "3":
        damage = int(Tackle())
        OpponentHealth = OpponentHealth - damage
        print(Opponent, "'s health is now at ", OpponentHealth, sep="")
        
def PlayerFupa():
    global CharacterHealth
    global OpponentHealth
    time.sleep(3)
    print("")
    print("It is Fupa's turn to attack!")
    time.sleep(1)
    SelectMove(Character)
    if Move == "1":
        if CharacterHealth <= 0 or OpponentHealth <= 0:
            return
        else:
            damage = int(InvestPlayer())
            OpponentHealth = OpponentHealth - damage
            print(Opponent, "'s health is now at ", OpponentHealth, sep="")
    if Move == "2":
        damage = int(Pressed())
        OpponentHealth = OpponentHealth - damage
        print(Opponent, "'s health is now at ", OpponentHealth, sep="")
    if Move == "3":
        damage = int(Skullcrusher())
        OpponentHealth = OpponentHealth - damage
        print(Opponent, "'s health is now at ", OpponentHealth, sep="")


        
def PlayerSchnoz():
    global CharacterHealth
    global OpponentHealth
    time.sleep(3)
    print("")
    print("It is Schnoz's turn to attack!")
    time.sleep(1)
    SelectMove(Character)
    if Move == "1":
        damage = int(Gamble())
        OpponentHealth = OpponentHealth - damage
        print(Opponent, "'s health is now at ", OpponentHealth, sep="")
    if Move == "2":
        damage = int(QuickCombo())
        OpponentHealth = OpponentHealth - damage
        print(Opponent, "'s health is now at ", OpponentHealth, sep="")
    if Move == "3":
        damage = int(WeeMan())
        OpponentHealth = OpponentHealth - damage
        print(Opponent, "'s health is now at ", OpponentHealth, sep="")

#CPU Characters

def CPUTrundle():
    global CharacterHealth
    global OpponentHealth
    time.sleep(3)
    print("")
    print("It is Trundle's turn to attack!")
    time.sleep(1)
    CPUMove(Opponent)
    if MoveCPU == "1":
        health = int(Rest())
        OpponentHealth = OpponentHealth + health
        print("Trundle's health is now at", OpponentHealth)
    if MoveCPU == "2":
        damage = int(EggThrow())
        CharacterHealth = CharacterHealth - damage
        print(Character, "'s health is now at ", CharacterHealth, sep="")
    if MoveCPU == "3":
        damage = int(Tackle())
        CharacterHealth = CharacterHealth - damage
        print(Character, "'s health is now at ", CharacterHealth, sep="")
        
def CPUFupa():
    global CharacterHealth
    global OpponentHealth
    time.sleep(3)
    print("")
    print("It is Fupa's turn to attack!")
    time.sleep(1)
    CPUMove(Opponent)
    if Move == "1":
        if CharacterHealth <= 0 or OpponentHealth <= 0:
            return
        else:
            damage = int(InvestPlayer())
            CharacterHealth = CharacterHealth - damage
            print(Character, "'s health is now at ", CharacterHealth, sep="")
    if Move == "2":
        damage = int(Pressed())
        CharacterHealth = CharacterHealth - damage
        print(Character, "'s health is now at ", CharacterHealth, sep="")
    if Move == "3":
        damage = int(Skullcrusher())
        CharacterHealth = CharacterHealth - damage
        print(Character, "'s health is now at ", CharacterHealth, sep="")

def CPUSchnoz():
    global CharacterHealth
    global OpponentHealth
    time.sleep(3)
    print("")
    print("It is Schnoz's turn to attack!")
    time.sleep(1)
    CPUMove(Opponent)
    if MoveCPU == "1":
        damage = int(Gamble())
        CharacterHealth = CharacterHealth - damage
        print(Character, "'s health is now at ", CharacterHealth, sep="")
    if MoveCPU == "2":
        damage = int(QuickCombo())
        CharacterHealth = CharacterHealth - damage
        print(Character, "'s health is now at ", CharacterHealth, sep="")
    if MoveCPU == "3":
        damage = int(WeeMan())
        CharacterHealth = CharacterHealth - damage
        print(Character, "'s health is now at ", CharacterHealth, sep="")

#Game Functions

def CharacterSelect():
    CharacterSelected = False
    global isTrundle
    global isFupa
    global isSchnoz
    isTrundle = False
    isFupa = False
    isSchnoz = False
    while CharacterSelected == False:
        print("Select Your Character!")
        print("Which character would you like to view?", "Enter:", "'T' for Trundle", "'F' for Fupa", "'S' for Schnoz", sep="\n")
        x = input()
        if x == "T" or x == "t":
            print("")
            print("Trundle:")
            print("")
            print("Health: 300")
            print("")
            print("Attack: Weak")
            print("")
            print("Moves:", "",
                  "Rest - Allows Trundle to regain health.",
                  "EggThrow - A weaker attack that has potential to be a high damaging critical attack.",
                  "Tackle - A stronger attack with a lower chance of a critical hit.", sep="\n")
            print("")
            time.sleep(1)
            print("To select, enter 'Y'")
            response = input("Enter anything else to go back.")
            if response == "Y" or response == "y":
                CharacterSelected = True
                isTrundle = True
                return
            else:
                CharacterSelected = False
                print("")
        elif x == "F" or x == "f":
            print("")
            print("Fupa:")
            print("")
            print("Health: 275")
            print("")
            print("Attack: Strong")
            print("")
            print("Moves:", "",
                  "Invest - Three round attack. The damage increases with each round of the attack.",
                  "Pressed - A powerful attack that can only be used after a round where a lot of damage is received",
                  "Skullcrusher - This attack does 15 damage per second with a random chance for the attack to continue", sep="\n")
            print("")
            time.sleep(1)
            print("To select, enter 'Y'")
            response = input("Enter anything else to go back.")
            if response == "Y" or response == "y":
                CharacterSelected = True
                isFupa = True
                return
            else:
                CharacterSelected = False
                print("")
        elif x == "S" or x == "s":
            print("")
            print("Schnoz:")
            print("")
            print("Health: 250")
            print("")
            print("Attack: Average")
            print("")
            print("Moves:", "",
                  "Gamble - There is a 50/50 chance that there will be a high damage attack, or a missed attack",
                  "Quick Combo - Three rapid attacks, each with differing damage",
                  "Wee Man - A weaker attack that has potential to be a high damaging critical attack", sep="\n")
            print("")
            time.sleep(1)
            print("To select, enter 'Y'")
            response = input("Enter anything else to go back.")
            if response == "Y" or response == "y":
                CharacterSelected = True
                isSchnoz = True
                return
            else:
                CharacterSelected = False
                print("")
        else:
            print("Input is not valid.")
            CharacterSelected = False
            print("")

def OpponentSelect():
    print("")
    global Character
    global Opponent
    if isTrundle == True:
        Character = "Trundle"
        print("You have selected Trundle.")
        print("")
        time.sleep(1)
        print("Your opponent will be...")
        time.sleep(1)
        opp = random.randint(1,2)
        if opp == 1:
            print("Fupa!")
            Opponent = "Fupa"
        if opp == 2:
            print("Schnoz!")
            Opponent = "Schnoz"
    if isSchnoz == True:
        Character = "Schnoz"
        print("You have selected Schnoz.")
        print("")
        time.sleep(1)
        print("Your opponent will be...")
        time.sleep(1)
        opp = random.randint(1,2)
        if opp == 1:
            print("Fupa!")
            Opponent = "Fupa"
        if opp == 2:
            print("Trundle!")
            Opponent = "Trundle"
    if isFupa == True:
        Character = "Fupa"
        print("You have selected Fupa.")
        print("")
        time.sleep(1)
        print("Your opponent will be...")
        time.sleep(1)
        opp = random.randint(1,2)
        if opp == 1:
            print("Trundle!")
            Opponent = "Trundle"
        if opp == 2:
            print("Schnoz!")
            Opponent = "Schnoz"

def MatchSetup(Character, Opponent):
    print("")
    time.sleep(1)
    global CharacterHealth
    global OpponentHealth
    global AttackFirst
    if Character == "Trundle":
        if Opponent == "Fupa":
            CharacterHealth = int(300)
            OpponentHealth = int(275)
            Start = random.randint(1,2)
            if Start == 1:
                AttackFirst = "Yes"
                print("Trundle will attack first!")
            else:
                AttackFirst = "No"
                print("Fupa will attack first!")
        if Opponent == "Schnoz":
            CharacterHealth = int(300)
            OpponentHealth = int(250)
            Start = random.randint(1,2)
            if Start == 1:
                AttackFirst = "Yes"
                print("Trundle will attack first!")
            else:
                AttackFirst = "No"
                print("Schnoz will attack first!")
    if Character == "Schnoz":
        if Opponent == "Fupa":
            CharacterHealth = int(250)
            OpponentHealth = int(275)
            Start = random.randint(1,2)
            if Start == 1:
                AttackFirst = "Yes"
                print("Schnoz will attack first!")
            else:
                AttackFirst = "No"
                print("Fupa will attack first!")
        if Opponent == "Trundle":
            CharacterHealth = int(250)
            OpponentHealth = int(300)
            Start = random.randint(1,2)
            if Start == 1:
                AttackFirst = "Yes"
                print("Schnoz will attack first!")
            else:
                AttackFirst = "No"
                print("Trundle will attack first!")
    if Character == "Fupa":
        if Opponent == "Trundle":
            CharacterHealth = int(275)
            OpponentHealth = int(300)
            Start = random.randint(1,2)
            if Start == 1:
                AttackFirst = "Yes"
                print("Fupa will attack first!")
            else:
                AttackFirst = "No"
                print("Trundle will attack first!")
        if Opponent == "Schnoz":
            CharacterHealth = int(275)
            OpponentHealth = int(250)
            Start = random.randint(1,2)
            if Start == 1:
                AttackFirst = "Yes"
                print("Fupa will attack first!")
            else:
                AttackFirst = "No"
                print("Schnoz will attack first!")

def SelectMove(Character):
    global Move
    if Character == "Trundle":
        SelectMove = False    
        while SelectMove == False:
            print("For Rest: Enter 1.",
                  "For EggThrow: Enter 2.",
                  "For Tackle: Enter 3.",
                  "To view move descriptions: Enter anything else.",
                  sep="\n")
            Move = input()
            if Move == "1":
                SelectMove = True
            elif Move == "2":
                SelectMove = True
            elif Move == "3":
                SelectMove = True
            else:
                print("Moves:", "",
                      "Rest - Allows Trundle to regain health.",
                      "EggThrow - A weaker attack that has potential to be a high damaging critical attack.",
                      "Tackle - A stronger attack with a lower chance of a critical hit.", sep="\n")
            print("")
            time.sleep(1)
    if Character == "Schnoz":
        SelectMove = False
        while SelectMove == False:
            print("For Gamble: Enter 1.",
                  "For Quick Combo: Enter 2.",
                  "For Wee Man: Enter 3.",
                  "To view move descriptions: Enter anything else.",
                  sep="\n")
            Move = input()
            if Move == "1":
                SelectMove = True
            elif Move == "2":
                SelectMove = True
            elif Move == "3":
                SelectMove = True
            else:
                print("Moves:", "",
                      "Gamble - There is a 50/50 chance that there will be a high damage attack, or a missed attack",
                      "Quick Combo - Three rapid attacks, each with differing damage",
                      "Wee Man - A weaker attack that has potential to be a high damaging critical attack", sep="\n")
            print("")
            time.sleep(1)
    if Character == "Fupa":
        SelectMove = False
        while SelectMove == False:
            print("For Invest: Enter 1.",
                  "For Pressed: Enter 2.",
                  "For Skullcrusher: Enter 3.",
                  "To view move descriptions: Enter anything else.",
                  sep="\n")
            Move = input()
            if Move == "1":
                SelectMove = True
            elif Move == "2":
                SelectMove = True
            elif Move == "3":
                SelectMove = True
            else:
                print("Moves:", "",
                      "Invest - Three round attack. The damage increases with each round of the attack.",
                      "Pressed - A powerful attack that can only be used after a round where a lot of damage is received",
                      "Skullcrusher - This attack does 15 damage per second with a random chance for the attack to continue", sep="\n")
            print("")
            time.sleep(1)
            
def CPUMove(Opponent):
    global MoveCPU
    if Opponent == "Trundle":
        if OpponentHealth < (CharacterHealth - 15):
            x = random.randint(1,5)
            if x == 1:
                MoveCPU = "2"
            elif x == 2:
                MoveCPU = "3"
            else:
                MoveCPU = "1"
        else:
            x = random.randint(1,5)
            if x == 1:
                MoveCPU = "1"
            if x == 2 or x == 3:
                MoveCPU = "2"
            if x == 4 or x == 5:
                MoveCPU = "3"
    if Opponent == "Schnoz":
        x = random.randint(1,3)
        if x == 1:
            MoveCPU = "1"
        if x == 2:
            MoveCPU = "2"
        if x == 3:
            MoveCPU = "3"
    if Opponent == "Fupa":
        x = random.randint(1,3)
        if x == 1:
            MoveCPU = "1"
        if x == 2:
            MoveCPU = "2"
        if x == 3:
            MoveCPU = "3"
    
                
def PlayerTurn(Character):
    if CharacterHealth <= 0 or OpponentHealth <= 0:
        return
    else:
        if Character == "Trundle":
            PlayerTrundle()
        if Character == "Schnoz":
            PlayerSchnoz()
        if Character == "Fupa":
            PlayerFupa()

def CPUTurn(Opponent):
    if CharacterHealth <= 0 or OpponentHealth <= 0:
        return
    else:
        if Opponent == "Trundle":
            CPUTrundle()
        if Opponent == "Schnoz":
            CPUSchnoz()
        if Opponent == "Fupa":
            CPUFupa()
    

#Game

def Game():
    ContinueGame = True
    CharacterSelect()
    OpponentSelect()
    MatchSetup(Character, Opponent)
    if AttackFirst == "Yes":
        while ContinueGame == True:
            PlayerTurn(Character)
            CPUTurn(Opponent)
            if CharacterHealth <= 0 or OpponentHealth <= 0:
                ContinueGame = False
    else:
        while ContinueGame == True:
            CPUTurn(Opponent)
            PlayerTurn(Character)
            if CharacterHealth <= 0 or OpponentHealth <= 0:
                ContinueGame = False
    print("")
    print("")
    time.sleep(2)
    if CharacterHealth > OpponentHealth:
        print(Character, "Wins!")
    else:
        print(Opponent, "Wins!")
        print("You Lose!")
           
Game()
    

    

        
    


