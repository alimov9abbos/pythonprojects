#OWNER: Abboskhon Alimov (Abbos)
#Project start date 12/13/19
#last edit made 12/14/19

import random
#prints the directions to launch the game
print('\nIf you would like to play a game please follow the directions.\n')
print('To play this game you must be in file interactive mode. ')
print('To be in interactive mode type: "py -i rps_game.py"')
print('Then type: rps_game()\n')

#function call
def rps_game():
#asks the user the number of games to run
    num_games=int(input("How many games would you like to play?: "))
#if user changes their mind and enters 0 return the following message
    if num_games==0:
        return "Okay, maybe you just don't have time right now. Have a good day!"
#if not, start the counter x
    x=0
#feedback is empty and setup points 
    feedback=''
    AI_points=0
    human_points=0 
#loop of games start
    while x < num_games:
#there is a list of possible choices
        choice_list=['rock','paper','scissors']
#Asks the user to make a choice
        user_choice=str(input("Rock, Paper, or Scissors?: "))
#lower-case the choice because the list only has lowercase options
        user_choice=user_choice.lower()
#if the choice is not in the list, then 
        if user_choice not in choice_list:
#print that the choice isnt the choice isn't in the list
            print("You did not choose an element in the game.")
#ask the user to try again
            feedback=str(input("Would you like to try again?: "))
#lowercase, then if yes, restart the game, if not, then just stop the game
            feedback=feedback.lower()
            if feedback=='yes':
                rps_game()
            else:
                break
            
#list all the outcomes and print the statement on who wins, and add the points
        else:    
            bot_choice=random.choice(choice_list)
            if bot_choice==user_choice:
                print("\n \n \n TIE! Go again! \n \n \n ")
            
            elif bot_choice == 'scissors' and user_choice== 'paper':
                AI_points+=1
                print("\n \n \n Bot Wins >:) . Go again. Bot points:"+ str(AI_points)+"\n \n \n")
            elif bot_choice == 'rock' and user_choice== 'scissors':
                AI_points+=1
                print("\n \n \n Bot Wins >:) . Go again. Bot points:"+ str(AI_points)+"\n \n \n")
            elif bot_choice == 'paper' and user_choice== 'rock':
                AI_points+=1
                print("\n \n \n Bot Wins >:) . Go again. Bot points:"+ str(AI_points)+"\n \n \n")
            
            
            elif user_choice == 'scissors' and bot_choice== 'paper':
                human_points+=1
                print("\n \n \n YOU WIN! >:) . Go again. YOUR points:"+ str(human_points)+"\n \n \n")
            elif user_choice == 'rock' and bot_choice== 'scissors':
                human_points+=1
                print("\n \n \n YOU WIN! >:) . Go again. YOUR points:"+ str(human_points)+"\n \n \n")
            elif user_choice == 'paper' and bot_choice== 'rock':
                human_points+=1
                print("\n \n \n YOU WIN! >:) . Go again. YOUR points:"+ str(human_points)+"\n \n \n")            
            
            
            
        
        
#that is one game so add 1 to the counter   
        
        x+=1
#then calculate the difference
    difference=abs(AI_points-human_points)


#list all the possible outcomes of the games, print who wins and by how much
#then asks the user if they want to play again    
    if AI_points > human_points:
        print ('\nBOT WINS BY ' + str(difference)+' points! \n')
        feedback=str(input("Would you like to play again?: "))
        feedback=feedback.lower()
        if feedback=='yes':
            rps_game()
        else:
            pass
    elif AI_points < human_points:
        print ('\n YOU WIN BY '+ str(difference)+' points! \n')
        feedback=str(input("Would you like to play again?: "))
        feedback=feedback.lower()
        if feedback=='yes':
            rps_game()
        else:
            pass
    elif human_points==AI_points:
        print ('\n TIE! \n')
        feedback=str(input("Would you like to play again?: "))
        feedback=feedback.lower()
        if feedback=='yes':
            rps_game()
        else:
            pass