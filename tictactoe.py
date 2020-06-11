def printboard():
	global ttt

	print ('{}|{}|{}'.format(ttt[0],ttt[1],ttt[2]))
	print ('{}|{}|{}'.format(ttt[3],ttt[4],ttt[5]))
	print ('{}|{}|{}\n'.format(ttt[6],ttt[7],ttt[8]))

def playertoplay():
	global ttt, typ

	print('Player {} your turn!\n'.format(typ))
	position = int(input('Where do you want to place {}? '.format(typ)))

	if ttt[position-1] == ' ':
		ttt[position-1] = typ
		printboard()
	else:
		print('This position is already taken. Please choose another.')
		playertoplay()

def checkboard():
	global ttt, typ

	notwin = True

	for i in (1, 2, 3, 4, 7):
		if ttt[i-1:i-1+3:1] == [typ,typ,typ] and i in (1, 4, 7):
			notwin = False 
		if ttt[i-1:i-1+7:3] == [typ,typ,typ] and i in (1, 2, 3):
			notwin = False 
		if ttt[i-1:i-1+9:4] == [typ,typ,typ] and i == 1:
			notwin = False 
		if ttt[i-1:i-1+5:2] == [typ,typ,typ] and i == 3:
			notwin = False 

	return notwin

def boardfull():
	global ttt

	notfull = True
	empty = ' ' 

	if empty not in ttt:
		notfull = False

	return notfull

	
###############################################################

ttt = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

printboard()

check = True
whichplayer = 1

while check:
	if whichplayer % 2 != 0:
		typ = 'X'
	else:
		typ = 'O'
	playertoplay()
	if not checkboard():
		check = False
		print('Player {} has won!'.format(typ))
		break
	elif not boardfull():
		check = False
		print('There is no winner. Feel free to start again.')
		break
	whichplayer += 1

