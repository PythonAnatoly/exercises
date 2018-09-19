# Python 3.4
# Tasks from http://www.checkio.org/

# SOLUTIONS FOR "XS AND OS REFEREE"
# My solution
'''
game_result1 = [
    ".4.",
    "44.",
    "X4."]
game_result2 = [
    "OO.",
    "XOX",
    "XOX"]
game_result3 = [
    "OOX",
    "XXO",
    "OXX"]

def checkio(game_result):
	
	def func(lst):
		for n in lst:
			if n[0] == n[1] == n[2] and n[0] != '.': 
				return (n[0][0])
				break
			else:
				False
				
	def func2(lst):
		a = 0
		while a < 3:
			if lst[0][a] == lst[1][a] == lst[2][a] and lst[0][a] != '.':
				return (lst[0][a])
				break
			a += 1
	
	while True:
		if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.':
			return (game_result[0][0])
			break
			
		elif game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2] != '.':
			return (game_result[0][2])
			break
			
		elif func(game_result):
			return (func(game_result))
			break
			
		elif func2(game_result):	
			return (func2(game_result))
			break
		
		else:
			return ('D')
			break	
print (checkio(game_result1))
'''
# Solution from other user  http://www.checkio.org/mission/x-o-referee/publications/gyahun_dash/python-3/second/?ordering=most_voted
'''
def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
'''
# Solution from other user
'''
def checkio(board):
    # First we put everything together into a single string
    x = "".join(board)
    
    # Next we outline the 8 possible winning combinations. 
    combos = ["012", "345", "678", "036", "147", "258", "048", "246"]
    
    # We go through all the winning combos 1 by 1 to see if there are any
    # all Xs or all Os in the combos
    for i in combos:
        if x[int(i[0])] == x[int(i[1])] == x[int(i[2])] and x[int(i[0])] in "XO":
            return x[int(i[0])]
    return "D" 
'''
# END


# SOLUTIONS FOR "THE MOST WANTED LETTER"
# my solution
'''
def checkio(text):
	a = 'abcdefghijklmnoprstuvwxyz'
	dic = {}
	for letter in a:
		if letter in text:
			n = text.count(letter)
			dic[letter] = n

	lst = sorted(dic.items(), key=lambda x: x[1])
	m = max(lst, key=lambda x: x[1])[1]

	new_lst =[]
	for n in lst:
		if n[1] == m:
			new_lst.append(n)

	new_lst = sorted(new_lst, key=lambda x: x[0])
	return new_lst[0][0]
	#return 'The most frequent letter is ', '"'+new_lst[0][0]+'"', '=', new_lst[0][1], 'times'

print (checkio(text = input('Any text: ').lower()))
'''

# Solution from site
'''
from collections import Counter
def checkio():
	while True:
		try:
			text = input("Enter text: ")
			count = Counter([x for x in text.lower() if x.isalpha()])
			m = max(count.values())
			return sorted([x for (x, y) in count.items() if y == m])[0]
			break
		except ValueError as err:
			pass
			continue
print (checkio())
'''

# Solution from other user
'''
def checkio(text):
    text = text.lower()  
    d = {k:text.count(k) for k in text if k.isalpha()}  
    return max(sorted(d.keys()), key = lambda k: d[k])
print (checkio(input('Type any text: ')))
'''

# solutin 3 (from other user)
'''
def checkio(text):
    s = sorted([c for c in text.lower() if c.isalpha()])
    return min((-s.count(c), c) for c in s)[1]
print (checkio('Hello'))
'''
# END
