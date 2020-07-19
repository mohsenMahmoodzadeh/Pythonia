'''
ali hasan,mammad hossein
porteghal,sib holoo
amoo zanjir baff,
'''

def splitter(filename):
	file = open(file=filename, mode='r')
	content = file.readlines()
	file.close()
	ans = ""


	line_fragments = []
	candidate = []
	for line in content:
		line_fragments = line.split()
		for fragment in line_fragments:
			if ',' in fragment:
				candidate = fragment.split(',')
				s = ','.join(candidate)
				s += '\n'
				ans += s
				
	        
	return ans


filename = input()
ans = splitter(filename)

ans_file = open('answer.txt', 'w')
ans_file.write(ans)
ans_file.close()

ans_file = open('answer.txt', 'r')
print(ans_file.read())
