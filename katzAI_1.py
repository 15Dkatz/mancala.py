def computerMove(board, player):
	boardCopy = board[:]
	maxMove = 1
	bestDifference = -999
	if player == 1:
		for checkMove in range(1,7):
			boardCopy = board[:]
			if legalMove(boardCopy, checkMove, player) == True:
				boardCopyChecked = doMove(boardCopy, checkMove, player)
				difference = boardCopyChecked[7] - board[7]
				if difference > bestDifference:
					bestDifference = difference
					maxMove = checkMove
	else:
		for checkMove in range(8,14):
			boardCopy = board[:]
			if legalMove(boardCopy, checkMove, player) == True:
				boardCopyChecked = doMove(boardCopy, checkMove, player)
				difference = boardCopyChecked[0] - board[0]
				if difference > bestDifference:
					bestDifference = difference
					maxMove = checkMove
	print("Computer moved at position", str(maxMove))
	return maxMove
	
	
def legalMove(board, position, player):
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
	boardPairs = {6: 8, 5:9, 4:10, 3: 11, 2: 12, 1: 13, 8:6, 9:5, 10:4, 11:3, 12:2, 13: 1, 0:0, 7:0}
	if player == 1:		
		addSwitch = False
		for x in range(board[position]):
			index = position + 1 + x
			if index > 13:
				index -= 14
			print(index, 'gamgee')
			if x == (board[position]-1) and board[index] == 0:
				pair = boardPairs[index]
				if index <= 6:			
					board[7] += board[pair]
					board[pair] = 0	
			if addSwitch == False:
				if index == 0:
					addSwitch == True
					if (board[position]+position) >= 14:
						 board[(board[position]+position)-13]+= 1
				else:
					board[index]+= 1
			else:
				if index == 7:
					addSwitch == False
				else:
					board[index+1]+= 1
		board[position] = 0
	elif player == 2:
		for x in range(board[position]):
			index = position + 1 + x			
			#needs to reloop twice
			if index > 13:
				index -= 14
			if x == (board[position] - 1) and board[index] == 0:
				pair = boardPairs[index]
				print(pair, 'p')
				print(index, 'current')
				if index >= 8:
				
					board[0] += board[pair]
					board[pair] = 0
			print(index, 'fish')
			if index == 7:
				board[index+(board[position]-7)] += 1
			else:
				board[index]+= 1
		board[position] = 0
	return board
	
	
	

	

#start improving the A.I.
#setup Captures.
#A.I. checks difference twoMoves ahead for the combination of Moves possible, and return the max Combo, otherwise simply does the best possible first move or capture

