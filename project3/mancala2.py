from katz import *
import sys

def createBoard():
	board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
	if len(sys.argv) == 4 and sys.argv[3].isdigit() == True:
		pitsNum = int(sys.argv[3])
		board = [0]
		pit = 0
		for pit in range(6):
			board.append(pitsNum)
		board.append(0)
		for pit in range(6):
			board.append(pitsNum)
	return board

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

def isGameOver(board, player):
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
	
	
def runGame(board, player, cpu):
	printBoard(board)
	if isGameOver(board, player) == False:
		if player == 1:
			if cpu == 1 or cpu == 3:
				cpuMove = computerMove(board, player)
				newBoard = doMove(board, cpuMove, player)
			else:
				position = input('Enter a move for player 1: ')
				while int(position) > 6 or int(position) < 1 or legalMove(board, position, player) == False:
					print('Sorry, the move ' + position + ' is invalid for player 1.')
					printBoard(board)
					position = input('Enter a move for player 1: ')
				if legalMove(board, position, player) == True:
					newBoard = doMove(board, int(position), player)
				
			runGame(newBoard, 2, cpu)
			
		elif player == 2:
			if cpu == 2 or cpu == 3:
				cpuMove2 = computerMove(board, player)
				newBoard = doMove(board, cpuMove2, player)
			else:
				position = input('Enter a move for player 2: ')
				while int(position) > 13 or int(position) < 8 or legalMove(board, position, player) == False:
					print('Sorry, the move ' + position + ' is invalid for player 2.')
					printBoard(board)
					position = input('Enter a move for player 2: ')
				if legalMove(board, position, player) == True:
					newBoard = doMove(board, int(position), player)
			
			runGame(newBoard, 1, cpu)
	else:
		if board[0] < board[7]:
			victory = 'Player 1 wins, ' + str(board[7]) + ' to ' + str(board[0])
		else:
			victory = 'Player 2 wins, ' + str(board[0]) + ' to ' + str(board[7])
		print(victory)


if __name__ == '__main__':
	cpu = 0

	if len(sys.argv) == 4:
		if sys.argv[1] == "computer" and sys.argv[2] != "computer":
			cpu = 1
		elif sys.argv[1] != "computer" and sys.argv[2] == "computer":
			cpu = 2
		elif sys.argv[1] == "computer" and sys.argv[2] == "computer":
			cpu = 3
	runGame(createBoard(), 1, cpu)