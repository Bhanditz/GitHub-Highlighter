import re
from sys import argv

regex = re.compile(r'#([0-9a-f]{3}){1,2}', re.IGNORECASE)
table = str.maketrans('0123456789abcdef', 'fedcba9876543210')

def invert(content):
	return content.group().lower().translate(table)

for filename in argv[1:]:
	with open(filename,'r') as file:
		content = regex.sub(invert, file.read())
		with open(filename[:-4] + '-inverted.css','w') as out:
			out.write(content)