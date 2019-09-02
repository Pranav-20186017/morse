f = open("words.txt")
l = []
for x in f:
	l.append(x.strip("\n"))
l.sort()
f.close()
print(l)
w = open("sorted.txt","a")
for _ in l:
	w.write(_)
	w.write("\n")
w.close()
