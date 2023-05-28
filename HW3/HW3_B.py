#Elias Caceres
#cacer019
#CSCI 1133 Homework 3 Problem B
#Rock Paper Scissors
#This was reaaaaaaaly hard

def rock_paper_scissors(player_1, player_2):															   #rock paper scissors function 
	if (player_1 == player_2):
		game = "It's a tie, nobody wins"
		return game
	elif (player_1 == "R") and (player_2 == "P"):
		game = "Player 2 wins!"
		return game
	elif (player_1 == "P") and (player_2 == "R"):
		game = "Player 1 wins!"
		return game
	elif (player_1 == "R") and (player_2 == "S"):
		game = "Player 1 wins!"
		return game
	elif (player_1 == "S") and (player_2 == "R"):
		game = "Player 2 wins!"
		return game
	elif (player_1 == "P") and (player_2 == "S"):
		game = "Player 2 wins!"
		return game
	elif (player_1 == "S") and (player_2 == "P"):
		game = "Player 1 wins!"
		return game 


def main():
	gameno = 1																								#defining count values to use in while loop
	rounds = 0 				
	onewins = 0
	twowins = 0
	p1win = "Final Determination: Player 1 won this round."
	p2win = "Final Determination: Player 2 won this round."
	tie = "Final Determination: It is a tie! No one won this round."

	while (rounds <= 3) or (onewins < 3) or (twowins < 3):
		sentence = 'Game {}:'.format(gameno)									#while loop to run game multiple times
		player_1 = input("Rock (R), Paper (P), or Scissors (S)? ")
		player_2 = input("Rock (R), Paper (P), or Scissors (S)? ")
		result = rock_paper_scissors(player_1, player_2)
		print(sentence)
		print("Player 1: ", player_1)
		print("Player 2: ", player_2)
		print(result)
		p1win = "Final Determination: Player 1 won this round."
		p2win = "Final Determination: Player 2 won this round."
		tie = "Final Determination: It is a tie! No one won this round."
		if (result == "It's a tie, nobody wins"):
			rounds = rounds + 1
			gameno = gameno + 1
			if (rounds == 3):
				break
		elif (result == "Player 1 wins!"):
			rounds = rounds + 1
			onewins = onewins + 1
			gameno = gameno + 1
			if (rounds == 3):
				break
			elif (onewins == 2):
				break
		elif (result == "Player 2 wins!"):
			rounds = rounds + 1
			twowins = twowins + 1
			gameno = gameno + 1
			if (rounds == 3):
				break
			elif (twowins == 2):
				break
	if (onewins == 1) and (twowins == 1) and (rounds == 3):													#print functions for final determination
		print(tie)
	elif (onewins == 2):
		print(p1win)
	elif (twowins == 2):
		print(p2win)

if __name__ == "__main__":
    main()
