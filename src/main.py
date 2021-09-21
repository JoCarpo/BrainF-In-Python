from interpreter import run, lexer, lstNum
import sys

code = sys.argv[1]

with open(code, 'r') as file:
	lexed, loops = lexer(file)

cells, currentCell = run(lexed, loops)
cells = lstNum(cells, currentCell)
print(f'\n\033[1;32m=> {cells}\033[0m')
