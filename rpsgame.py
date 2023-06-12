import random
#rock paper scisor game
def get_choices():
  game = ["rock", "paper", "scissor"]
  player_choice = input("enter the player choice, [ rock, paper, scissor]")
  computer_choice = random.choice(game)
  choices = {"player": player_choice, "computer": computer_choice}
  
  return choices
  
def check_win(player, computer):
    print(f"you chose {player} , computer chose  {computer}")
    if player == computer:
      return "its a tie!"
    elif player == "rock":
      if computer == "scissor":
        return "rock smashes the scissors, YOU WON!!"
      else :
        return "paper covers the rock, YOU LOST!!"
     
    elif player == "paper":
      if computer == "rock":
        return "paper covers rock, YOU WON!!"
      else :
        return "scissor cuts paper, YOU LOST!!"

    elif player == "scissor":
      if computer == "rock":
        return "rock smashes scissor, YOU LOST!!"
      else :
        return "scissor cuts paper, YOU WON!!"
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)