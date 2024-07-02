import random
from coolconsole import Fore, Back, Style, Clear
score =0
oscore = 0 
def play_call_list(play_type):
    play_type = play_type.lower()
    if play_type == "pass":
        pass_list = ["slants", "hail marry", "te attack", "y-curl hb", "post corner", "mesh"]
        return pass_list  
    elif play_type == "run":
        run_list = ["inside", "qb", "outside", "pitch", "option", "draw"]
        return run_list  

def opscore(difficulty, oscore):
    difficulty = difficulty.lower()
    if difficulty == "easy":
        rs = random.randint(1,6)
    if difficulty == "hard":
        rs = random.randint(1,3)
    if rs == 1:
        oscore = oscore + 7
        print( "The oppenent scored a " +Style.BOLD + Fore.RED + "TOUCHDOWN"+ Style.RESET)
        return(oscore)
    elif rs == 2:
        oscore = oscore + 3
        print("The oppenent scored a "+ Style.BOLD + Fore.RED+  "field goal" + Style.RESET)
        return(oscore)
    else:
        oscore =oscore
        print("The oppenent didn't score")
        return(oscore)


def yards_pplay(play_type):
    play_type = play_type.lower()
    if play_type == "pass":
        pass_yards = [random.randint(10,30), random.randint(50, 75), random.randint(15,30), random.randint(1,20), random.randint(10,20), random.randint(1,15)]
        return pass_yards
    elif play_type == "run":
        run_yards = [random.randint(1,20), random.randint(1,20), random.randint(5,30), random.randint(1,40), random.randint(10,30), random.randint(1,30)]
        return run_yards


def play_ball(difficulty, score):
    count = 1
    total_yards = 75
    difficulty = difficulty.lower()
    difficulty_list= ["easy", "hard"]
    play_list=[ "pass", "run"]
    if difficulty in difficulty_list:
        pass
    else:
        return (" 'YOU CAN ONLY PLAY EASY OR HARD' ")
    if difficulty == "easy":
        turnover = [1,2]
        succes_rate= [65, 10, 85, 45, 25, 78]
        
    if difficulty == "hard":
        turnover = [1,2,3,4,5]
        succes_rate=[45, 6, 65, 25, 10, 58]
    while count!= 4:
        if total_yards <=0:
            score = score + 7
            print(Style.BOLD + Fore.GREEN + "TOUCHDOWN!!!!!" + Style.RESET)
            return(score) 
        if count == 1:
            yards = 0 
            past_yards = 0 
            print("It's first down!")
            play_type = input("pass or run: ")
            while play_type not in play_list:
                print("DELAY OF GAME, Your team didn't know what to run. You lost 5 yards")
                total_yards = total_yards + 5
                past_yards = past_yards - 5
                play_type = input("pass or run: ")
            print(play_call_list(play_type))
            listc = play_call_list(play_type)
            listy= yards_pplay(play_type)
            play = input("Whats the call(from list)?: ")
            if play in listc:
                ind = listc.index(play)
                index = succes_rate[ind]
                rand = random.randint(1,100)
                if rand <= index:
                    yards = listy[ind]
                    if yards in turnover:
                        if play_type == "pass":
                            print("YOUVE THROWN A PICK")
                            return(score)
                        else:
                            print("YOU HAVE FUMBLED")
                            return(score)
                    else:
                        print("You have gained " + str(yards) + " yards.")
                        total_yards = total_yards - yards
                        past_yards = past_yards + yards 
                        if past_yards >= 10:
                            count = 1

                        else:
                            count = count + 1
                else:
                    print("You didn't gain any yards")
                    count = count + 1 
            else: 
                if play_type == "pass":
                    print("You've been sacked")
                else:
                    print("You have been tackled for loss")
                los = random.randint(5,15)
                print("You have lost " + str(los) + " yards")
                total_yards = total_yards + los
                past_yards = past_yards - los
                count = count + 1
        
        if count == 2:
            print("It's second down!")
            play_type = input("pass or run: ")
            while play_type not in play_list:
                print("DELAY OF GAME, Your team didn't know what to run. You lost 5 yards")
                total_yards = total_yards + 5
                past_yards = past_yards - 5
                play_type = input("pass or run: ")
            print(play_call_list(play_type))
            listc = play_call_list(play_type)
            listy= yards_pplay(play_type)
            play = input("Whats the call(from list)?: ")
            if play in listc:
                ind = listc.index(play)
                index = succes_rate[ind]
                rand = random.randint(1,100)
                if rand <= index:
                    yards = listy[ind]
                    if yards in turnover:
                        if play_type == "pass":
                            print("YOUVE THROWN A PICK")
                            return(score)
                        else:
                            print("YOU HAVE FUMBLED")
                            return(score)
                    else:
                        print("You have gained " + str(yards) + " yards.")
                        total_yards = total_yards - yards
                        past_yards = past_yards + yards 
                        if past_yards >= 10:
                            count = 1

                        else:
                            count = count + 1
                else:
                    print("You didn't gain any yards")
                    count = count + 1 
            else: 
                if play_type == "pass":
                    print("You've been sacked")
                else:
                    print("You have been tackled for loss")
                los = random.randint(5,15)
                print("You have lost " + str(los) + " yards")
                total_yards = total_yards + los
                past_yards = past_yards - los
                count = count + 1
        
        if count == 3:
            print("It's third down!")
            play_type = input("pass or run: ")
            while play_type not in play_list:
                print("DELAY OF GAME, Your team didn't know what to run. You lost 5 yards")
                total_yards = total_yards + 5
                past_yards = past_yards - 5
                play_type = input("pass or run: ")
            print(play_call_list(play_type))
            listc = play_call_list(play_type)
            listy= yards_pplay(play_type)
            play = input("Whats the call(from list)?: ")
            if play in listc:
                ind = listc.index(play)
                index = succes_rate[ind]
                rand = random.randint(1,100)
                if rand <= index:
                    yards = listy[ind]
                    if yards in turnover:
                        if play_type == "pass":
                            print("YOUVE THROWN A PICK")
                            return(score)
                        else:
                            print("YOU HAVE FUMBLED")
                            return(score)
                    else:
                        print("You have gained " + str(yards) + " yards.")
                        total_yards = total_yards - yards
                        past_yards = past_yards + yards 
                        if past_yards >= 10:
                            count = 1

                        else:
                            count = count + 1
                else:
                    print("You didn't gain any yards")
                    count = count + 1 
            else: 
                if play_type == "pass":
                    print("You've been sacked")
                else:
                    print("You have been tackled for loss")
                los = random.randint(5,15)
                print("You have lost " + str(los) + " yards")
                total_yards = total_yards + los
                past_yards = past_yards - los
                count = count + 1
        if count == 4:
            print("It's fourth down!")
            play_type = input("pass or run: ")
            while play_type not in play_list:
                print("DELAY OF GAME, Your team didn't know what to run. You lost 5 yards")
                total_yards = total_yards + 5
                past_yards = past_yards - 5
                play_type = input("pass or run: ")
            print(play_call_list(play_type))
            listc = play_call_list(play_type)
            listy= yards_pplay(play_type)
            play = input("Whats the call(from list)?: ")
            if play in listc:
                ind = listc.index(play)
                index = succes_rate[ind]
                rand = random.randint(1,100)
                if rand <= index:
                    yards = listy[ind]
                    if yards in turnover:
                        if play_type == "pass":
                            print("YOUVE THROWN A PICK")
                            return(score)
                        else:
                            print("YOU HAVE FUMBLED")
                            return(score)
                    else:
                        print("You have gained " + str(yards) + " yards.")
                        total_yards = total_yards - yards
                        past_yards = past_yards + yards 
                        if past_yards >= 10:
                            count = 1

                        else:
                            print("turn over on downs!")
                            return(score)
                else:
                    print("You didn't gain any yards")
                    print("turn over on downs!")
                    return(score)
            else: 
                if play_type == "pass":
                    print("You've been sacked")
                else:
                    print("You have been tackled for loss")
                los = random.randint(5,15)
                print("You have lost " + str(los) + " yards")
                total_yards = total_yards + los
                past_yards = past_yards - los
                print("turn over on downs!")
                return(score)
    

    

print("There are 2 choices...1 half(4 drives)....1 game(8 drives)")
amount_of_time = input("Whats the choice?(H or G) : ")
amount_of_time = amount_of_time.lower()
amount_of_time_list= ["g", "h"]
difficulty_list= ["easy", "hard"]
if amount_of_time in amount_of_time_list:
    difficulty = input("What difficulty do you want to play?(Easy or Hard):" )
    difficulty = difficulty.lower()

    if amount_of_time == "h":
        if difficulty in difficulty_list:
            for i in range(4):
                score = play_ball(difficulty, score)
                oscore= opscore(difficulty, oscore)
                print( "The score to the game is " + Style.BOLD +Back.CYAN+  str(score) + ":" + str(oscore) + Style.RESET)
                print("\n\n*Press 'ENTER' to start the next drive*")
                input()
                print(Clear.ALL)
                print( "The score to the game is " + Style.BOLD +Back.CYAN+  str(score) + ":" + str(oscore) + Style.RESET) 
            if score > oscore:
                print("CONGRATS YOU HAVE WON!! The final score was " + str(score) + ":" + str(oscore))
            elif score < oscore:
                print("YOU HAVE LOST!! The final score was " + str(score) + ":" + str(oscore))
            else:
                print("YOU HAVE TIED!! The final score was " + str(score) + ":" + str(oscore))
        else:
            print (" 'YOU CAN ONLY PLAY EASY OR HARD' ")
    if amount_of_time == "g":
        if difficulty in difficulty_list:
            for i in range(8):
                score = play_ball(difficulty, score)
                oscore= opscore(difficulty, oscore)
                print("The score to the game is " + Style.BOLD +Back.CYAN+  str(score) + ":" + str(oscore) + Style.RESET)
                print("\n\n*Press 'ENTER' to start the next drive*")
                input()
                print(Clear.ALL)
                print("The score to the game is "+ Style.BOLD +Back.CYAN + str(score) + ":" + str(oscore)+ Style.RESET) 
            if score > oscore:
                print("CONGRATS YOU HAVE WON!! The final score was " + str(score) + ":" + str(oscore))
            elif score < oscore:
                print("YOU HAVE LOST!! The final score was " + str(score) + ":" + str(oscore))
            else:
                print("YOU HAVE TIED!! The final score was " + str(score) + ":" + str(oscore))
        else:
            print (" 'YOU CAN ONLY PLAY EASY OR HARD' ")
else:
    print("PLEASE ONLY PRESS 'h' or 'g'")