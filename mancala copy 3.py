def createBoard():
	board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
	return board

#prints out the currentboard
def printBoard(board):
	print('\n')
	print('  13 12 11 10  9  8  7')
	print('\n')
	secondLine = ''
	for x in range(8, 14):
		secondLine = '  ' + str(board[x]) + secondLine
	secondLine = ' ' + secondLine 
	print(secondLine)
	if board[0] > 9:
		print(str(board[0]) + '                   ' + str(board[7]))
	else:
		print(str(board[0]) + '                    ' + str(board[7]))
	fourthLine = '   '
	for x in range(1,7):
		if board[x] > 9:
			fourthLine += str(board[x]) + ' '
		else:
			fourthLine += str(board[x]) + '  '
	print(fourthLine)
	print('\n')
	print('0  1  2  3  4  5  6 ')
	print('\n')
	return board
	#nice
	
def legalMove(board, position, player):
	#checks if the inputted number is a legal move for that player.
	#player is a number
	if board[int(position)] == 0:
		return False
	else:
		if player == 1:
			if int(position) >= 1 and int(position) <= 6:
				return True
			else:
				return False
		elif player == 2:
			if int(position) >= 8 and int(position) <= 13:
				return True
			else:
				return False
	
def doMove(board, position, player):
	#do the move from the board on the inputted position, with the inputted player
	#check player status by either oddCount or evenCount
	#even count must match the position selected. 8-13 is player 2. 1-6 is player 1.
	# print(board)
	if player == 1:		
		addSwitch = False
		for x in range(board[position]):
			#for x in the range of the position's number, add 1 to each consecutive pocket
			#if this number becomes higher than 13, revert back to 0
			#fix
			#fix!!!!
			index = position + 1 + x
			if (index) > 13:
			# 	board[index] += 1
			# else:
				index -= 14
			if addSwitch == False:
				if index == 0:
					addSwitch == True
					# for y in range(position-x):
					# 	if (index) > 13:
					# 		index -= 14
					# 	board[index + 1 + y] += 1
					# break
					# print(x-position-1)
					#fix next line.
					
					# inverse relationship, when the position is 10 add 2, when 9 add 1, when 8 add none
					# print(index)
					# print(x-position)
					# print(board[position])
					# print(position)
					#figure out a less arbitrary number than 
					#must factor distance from the spot, then the actual number of beads, and which spot is chosen.
					#...
					#each spot is a certain distance 0, and the board[position], just adds a little more as it gets bigger
					#values of 9 can only start adding from the 5th spot, but values of 10 can start adding from the 4th, and values of 11, from the 3rd, and so on.
					
					
					
					#8 in the 6th spot, board[1] += 1    | lowest-level
					
					#9 in the 5th spot, board[1] += 1
					#9 in the 6th spot, board[2] += 1
					
					
					#10 in the 4th spot, board[1] += 1
					#10 in the 5th spot, board[2] += 1
					#10 in the 6th spot, board[3] += 1
					
					#11 in the 3rd spot, board[1] += 1
					#11 in the 4th spot, board[2] += 1
					#11 in the 5th spot, board[3] += 1
					
					
					#12 in the 4th spot, board[3] += 1
					#12 in the 5th spot, board[4] += 1
					
					#13 in the 1st spot, board[1] += 1
					#13 in the 2nd spot, board[2] += 1
					#13 in the 3rd spot, board[3] += 1
					#13 in the 4th spot, board[4] += 1
					
					#14 in the 1st spot, board[2] += 1
					#14 in the 2nd spot, board[3] += 1
					#14 in the 3rd spot, board[4] += 1
					#14 in the 4th spot, board[5] += 1
					
					if (board[position]+position) >= 14:
						 board[(board[position]+position)-13]+= 1
					# print(board[position]+position)
					
					# board[(board[position]-(position)] += 1
					# board[-((position+1)-(board[position]))]
				else:
					board[index]+= 1
			else:
				if index == 7:
					addSwitch == False
					# board[index+1] += 1
				else:
					board[index+1]+= 1
		board[position] = 0
	elif player == 2:
		#store a count, if the cuont is greater than 7, skip. if index at beginning within player's range, then don't add.
		#if position 
		for x in range(board[position]):
			#for x in the range of the position's number, add 1 to each consecutive pocket
			#if this number becomes higher than 13, revert back to 0
			index = position + 1 + x
			if (index) > 13:
			# 	board[index] += 1
			# else:
				index -= 14
			if index == 7:
				# print(x)
				# still buggy.
				if (board[position]+position) >= 14:
					board[(board[position]+position)-13]+= 1
				# board[index+(x-position)] += 1
			else:
				board[index]+= 1
		board[position] = 0
	# print(board)
	return board

def isGameOver(board, player):
	#checks the current player, and if the current player has no moves, perform a victory condition.
	#check for a list of zeros in the player's range.
	# use a sum funtion, and if the sum of the numbers is 0, return True.
	if player == 1:
		for x in range(1,7):
			if board[x] != 0:
				return False
		return True
	elif player == 2:
		for x in range(8,14):
			if board[x] != 0:
				return False
		return True
	
	
def runGame(board, player):
	# board = createBoard()
	printBoard(board)
	# currentPlayer = 1
	#wrap entire code in the isGameOver function, only run code if isGameOver == false...
	# position = input
	# can probably clean this
	if isGameOver(board, player) == False:
		if player == 1:
			#catch error, if inputted text is not a number, request a number, 'sorry the move {{input}} is invalid for player {{x}}'
			position = input('Enter a move for player 1: ')
			#do I need to convert to int, and check if convertable?
			#include legal move, then reprint
			while (int(position) > 6 or int(position) < 1) or legalMove(board, position, player) == False:
				print('Sorry, the move ' + position + ' is invalid for player 1.')
				printBoard(board)
				position = input('Enter a move for player 1: ')
			if legalMove(board, position, player) == True:
				newBoard = doMove(board, int(position), player)
				runGame(newBoard, 2)
			else:
				pass
		elif player == 2:
			position = input('Enter a move for player 2: ')
			while (int(position) > 13 or int(position) < 8) or legalMove(board, position, player) == False: 
				print('Sorry, the move ' + position + ' is invalid for player 2.')
				printBoard(board)
				position = input('Enter a move for player 2: ')
			if legalMove(board, position, player) == True:
				newBoard = doMove(board, int(position), player)
				runGame(newBoard, 1)			
	else:
		if board[0] < board[7]:
			victory = 'Player 1 wins, ' + str(board[7]) + ' to ' + str(board[0])
		else:
			victory = 'Player 2 wins, ' + str(board[0]) + ' to ' + str(board[7])
		print(victory)


	
runGame(createBoard(), 1)


#AI.

#how to pipe a series of numbers so that I can test my game?
# #test a exampleboard with the 1st player 0'd out, and then a second test with the 2nd player 0'd out.
# testboard1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# print(isGameOver(testboard1, 2))

#linux pipe command
#foo < file.txt. the pipe is the 'less than' symbol: '<'


#The A.I. hacking Mancala
# pick moves that equal the number of moves it takes to perfectly match to board[7] if player 1, or board[0] if player 2.
# or pick a move with a 0 on it if it would benefit player. 
# check which slots currently have more. 
# emergency mode, moderate mode, safe mode.
# moderate mode, make good decisions, 
# consider not allowing points to be added to the other side. As much as possible, don't let it go to the other side of the board.
# build a favorable block
# build a favorable position
# if nothing is a perfect match, create a perfect match, by building one by one.
# keep checking if no moves available. Go for a lead. If no moves available, and myStore is bigger, clear it out
# try not to give points to the opponent,
# give points to the opponent, if the opponent's store is all 0, and your store is less than
#	however, don't give beads to the opponent if the opponent's store is less than.
# if opponent picks a 0 option, looks for the 0 option as well. 
# keep going and ensure that at the end, once one member's board fully empties, and search to win the game.
# try not to use large numbers. dangerous. 
# give the opponent 1s on their first pocket