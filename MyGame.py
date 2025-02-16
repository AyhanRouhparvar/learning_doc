print("Rock...")
print("Paper...")
print("Scissors...")

player_1 = input("player_1 , make your move : ")
player_2 = input("player_2 , make your move : ")

if player_1 == player_2:
    print("that a tie") 
elif player_1 == "Rock":
    if player_2 == "Scissors":
        print("player_1 wins!....")
    elif player_2 == "Paper":
        print("player_2 wins!....")
elif player_1 == "Paper":
    if player_2 == "Rock":
        print("player_1 wins!....")
    elif player_2 == "Scissors":
        print("player_2 wins!....")
elif player_1 == "Scissors":
    if player_2 == "Paper":
        print("player_1 wins!....")
    elif player_2 == "Rock":
        print("player_2 wins!....")        
else:
    print("somthing went wrong ....")  
    
       
# if player_1 == "Rock" and player_2 == "Scissors":
#     print("player_1 wins!....")
# elif player_1 == "Rock" and player_2 == "Paper":
#     print("player_2 wins!....")    
# elif player_1 == "Paper" and player_2 == "Rock":
#     print("player_1 wins!....")
# elif player_1 == "Paper" and player_2 == "Scissors":
#     print("player_2 wins!....")    
# elif player_1 == "Scissors" and player_2 == "Paper":
#     print("player_1 wins!....")
# elif player_1 == "Scissors" and player_2 == "Rock":   
#     print("player_2 wins!....")  
# elif player_1 == player_2:
#     print("that a tie") 
# else:
#     print("somthing went wrong ....")    