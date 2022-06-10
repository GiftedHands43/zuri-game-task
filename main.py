import random
options = ["R", "P", "S"];
options_descriptions = ["Rock", "Paper", "Scissors"];
options_dict = dict(zip(options, options_descriptions));

while True:
   try:
       user_action = input("Enter your choice (R, P, S): ")
       possible_actions = ["R", "P", "S"]
       computer_action = random.choice(possible_actions)
       print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
       
       if user action not in options:
           print("Invalid choice!\nEnter a valid option\n")
           continue

       else:
           if user_action == computer_action:
               print(f"Both players selected {user_action}. It's a tie!")

           elif user_action == "R":
               if computer_action == "S":
                   print("Rock smashes scissors! You win!")

               else:
                   print("Paper covers rock! You lose.")

           elif user_action == "P":
               if computer_action == "R":
                   print("Paper covers rock! You win!")

               else:
                   print("Scissors cuts paper! You lose.")

           elif user_action == "S":
               if computer_action == "P":
                   print("Scissors cuts paper! You win!")

               else:
                   print("Rock smashes scissors! You lose.")

       play_again = input("Play again? (y/n): ")
       if play_again.lower() != "y":
           break

   except options:
       print("Invalid choice!")

       play_again = input("Play again? (y/n): ")
       if play_again.lower() != "y":
           break





