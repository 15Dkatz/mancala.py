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
			if index > 13:
				index -= 14
			if x == (board[position] - 1) and board[index] == 0:
				pair = boardPairs[index]
				if index >= 8:
					board[0] += board[pair]
					board[pair] = 0
			if index == 7:
				board[index+(board[position]-7)] += 1
			else:
				board[index]+= 1
		board[position] = 0
	return board

def computerMove(board, player):
	boardPairs = {6: 8, 5:9, 4:10, 3: 11, 2: 12, 1: 13, 8:6, 9:5, 10:4, 11:3, 12:2, 13: 1, 0:0, 7:0}
	boardCopy = board[:]
	maxMoveOff = 1
	maxMoveDef = 1
	bestDifference = -999
	bestDifference1 = -999
	if player == 1:
		for checkMove0 in range(1,7):
			boardCopy = board[:]
			
#		OFFENSE
			if legalMove(boardCopy, checkMove0, player) == True:
				boardCopyChecked = doMove(boardCopy, checkMove0, player)
				difference0 = boardCopyChecked[7] - board[7]
				if difference0 > bestDifference:
					bestDifference = difference0
					maxMoveOff = checkMove0
					
#		DEFENSE
		for checkMove1 in range(8,14):
			boardCopy1 = board[:]
			if legalMove(boardCopy1, checkMove1, 2) == True:
				boardCopyChecked1 = doMove(boardCopy1, checkMove1, 2)
				difference1 = boardCopyChecked1[0] - board[0]
				if difference1 > bestDifference1:
					bestDifference1 = difference1
					maxMoveDef = checkMove1 + board[checkMove1]
					if maxMoveDef > 13:
						maxMoveDef -= 14	


	else:
		for checkMove in range(8,14):
			boardCopy = board[:]
			if legalMove(boardCopy, checkMove, player) == True:
				boardCopyChecked = doMove(boardCopy, checkMove, player)
				difference = boardCopyChecked[0] - board[0]
				if difference > bestDifference:
					bestDifference = difference
					maxMoveOff = checkMove
		for checkMove2 in range(1,7):
			boardCopy2 = board[:]
			if legalMove(boardCopy2, checkMove2, 1) == True:
				boardCopyChecked2 = doMove(boardCopy2, checkMove2, 1)
				difference2 = boardCopyChecked2[7] - board[7]
				if difference2 > bestDifference1:
					bestDifference1 = difference2
					maxMoveDef = checkMove2 + board[checkMove2]
					if maxMoveDef > 13:
						maxMoveDef -= 14			
	if bestDifference >= bestDifference1:
		maxMove = maxMoveOff
	else:
		maxMove = boardPairs[maxMoveDef]
		# print('comparing', 'D:', boardPairs[maxMoveDef], ',', bestDifference1, 'O:', maxMoveOff, ',',  bestDifference)
	print("Computer moved at position", str(maxMove))
	return maxMove
	

	
# A.I. Improvements:
#add least amount of stones added to player's side possible..?
#more defensive strategies? 
#Setup up captures?

#Rushing strategy:
	#get rid of as many stones as possible on side as quickly as possible.
	#Dont run this strategy as pitting stones in opponent's puts sets up great captures
	


#Question for Professor Galles:
#does the tournament run each A.I. as both the first player and the second player, because arguably the most ideal A.I. would always win in 'CAPTURE' given the chance to go first.

#make testboards

#If the A.I. could win if the enemy is running out, don't put stones onto enemy side.
#I.e. check if a win is coming up, and if so let the opponent kill himself.
#don't do a move if it would lead to a terrible capture

#advanced defense
#go with the inital defensive move, but if that defensive move would lead to a more dire case, then go with the preventative move for that one.