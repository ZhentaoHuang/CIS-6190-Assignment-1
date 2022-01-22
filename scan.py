from sre_constants import JUMP
import ply.lex as lex
 
# List of token names, always needed
tokens = (
   'LABEL',
   'WORD',
   'NUMBER',
   'APOSTROPHIZED',
   'HYPHENATED',
   'DELIMITERS',
   'PUNCTUATION'
)

def t_LABEL(t): r'\$DOC.+|\$TITLE|\$TEXT'; return t  #LABEL must be exact "$TITLE", "$TEXT" or start with "$DOC"
t_WORD = r'[a-zA-Z]+'
t_NUMBER = r'[+|-]?\d+(\.\d+)?'	#Intergers and real numbers, with possible positive and negative signs
t_APOSTROPHIZED = r'[a-zA-Z]+(-[a-zA-Z]+)*\'[a-zA-Z]+(\'[a-zA-Z]+)*'
t_HYPHENATED = r'[a-zA-Z]+-[a-zA-Z]+(-[a-zA-Z]+)*'
t_DELIMITERS = r'[ \t]+'
t_PUNCTUATION = r'.'

# Error handling, always required
def t_error(t):
	print("Shouldn't get here")

# Build the lexer
lexer = lex.lex()

def scan(data):
	lexer.input(data)
	tok_list = []
	while True:
		tok = lexer.token()
		if not tok:
			break
		print(tok)
		tok_list.append(tok)
      # print(tok.type, tok.value, tok.lineno, tok.lexpos)
	return tok_list


input = open('samples.txt', 'r')
output = open('samples.tokenized', 'w')


lines = input.readlines()
count = 0
for line in lines:
   #print(line)
	token_list = scan(line[:-1])
	value_list = []
	for token in token_list:
		if(token.type != 'DELIMITERS'):
			value_list.append(token.value)
		#print(token.type)
	output.write(' '.join(value_list) + '\n')


	count = count + 1
	if(count == 5):
		break


input.close()
output.close()