def lstNum(lst, current):
	long = False

	for i in range(len(lst)):
		if i == current:
			lst[i] = str(f'[{lst[i]}]')
		else:
			lst[i] = str(lst[i])
	
	if len(lst) > 11:
		length = len(lst)
		lst = lst[length-11:]
		long = True
	
	lst = " ".join(lst)
	if long:
		lst = f'...{lst}'
	return lst

def lexer(code):
	lexed = []
	loops = []
	oneLoop = []
	loop = False

	for line in code:
		for char in line:
			if char in ['+', '-', '>', '<', '.', ',', '[', ']']:
				if char == ']':
					loop = False
					loops.append(oneLoop)
					lexed.append(char)
					oneLoop = []
				elif loop:
					oneLoop.append(char)
				elif char == '[':
					lexed.append(char)
					loop = True
				else:
					lexed.append(char)
	return lexed, loops

def run(lexed, loops, cells=[0], currentCell=0):
	currentLoop = 0

	for char in lexed:
		if char == '+':
			cells[currentCell] += 1
		elif char == '-':
			if cells[currentCell] != 0:
				cells[currentCell] -= 1
		elif char == '.':
			print(chr(cells[currentCell]), end="")
		elif char == ',':
			cells[currentCell] = ord(input('')[0])
		elif char == '>':
			if len(cells) > currentCell+1:
				currentCell += 1
			else:
				cells.append(0)
				currentCell += 1
		elif char == '<':
			if currentCell != 0:
				currentCell -= 1
		elif char == '[':
			cells, currentCell = loop(loops[currentLoop], cells, currentCell)
		elif char == ']':
			currentLoop += 1
	
	return cells, currentCell

def loop(loops, cells, current):
	while 1:
		cells, current = run(loops, [], cells, current)
		if cells[current] == 0:
			return cells, current

if __name__ == '__main__':
	code = input('BrainF >> ')
	lexed = lexer(code)
	run(lexed)
