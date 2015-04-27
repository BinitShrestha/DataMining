# PURPOSE:
# TO EXTRACT LOCATIONS AND GET THE
# LAT AND LONG COORDINATES

import re, os, sys, string, json


file_1 = 'file1.txt'
file_2 = 'file2.txt'
target = open("gps.txt", 'w')


def search(word):
	with open(file_2) as g:
		word = word.lower()
		#print(word)
		count = 0
		for line in g:
			line = line.lower()
			line = re.sub('[-]', ' ', line)
			line = re.sub('[,]', '', line)
			if word in line:
				#print(line)
				return line

def exact_search(word):
	with open(file_2) as i:
		for line in i:
			if word in line:
				return line



with open(file_1) as f:
	counter = 0
	for line in f:
		baby = True
		print(line)
		line = re.sub('\n', '', line)
		loc = line
		loc = exact_search(line)
		
		hell = "NO"
		if loc == None:
			baby = False
			line = re.sub('[,]', ' ', line)
			words = line.split()
			hell = "hi"
			for word in words:
				loc = search(word)
				if loc == None:
					break
				hell = loc
		if (baby == False):
			loc = hell
		
		target.write(str(loc))
		target.write("\n")
		
		counter = counter + 1
		print(loc)
		print(counter)


