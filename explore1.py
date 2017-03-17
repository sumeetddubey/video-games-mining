games={}
genres=set()
publishers=set()

with open('dataset/games.csv', 'r', encoding = "ISO-8859-1") as ip:
	for line in ip:
		line=line.strip()
		line=line.split(',')
		publishers.add(line[4])
		genres.add(line[3])
		if line[0] in games:
			# print(line[0])
			games[line[0]].extend(line)
		else:
			games[line[0]] = line

print('Number of unique games', len(games.keys()))
print('Number of genres', len(genres))
print('Number of publishers', len(publishers))