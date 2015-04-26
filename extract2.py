# EXTRACTING SETTLEMENTS
# Taking in the WikipediaDump, this code
# splits the name, latitude, and longitude
# of each settlement
# CREATED BY BINIT & NITICON

import re, os, sys, string, json, datetime
from sys import argv

#script, "filename.txt" = argv

WIKI_DUMPS = "new.txt"

# FUNCTIONS
# Function: to siginify when to search for settlements
def start_info(line):
	if ("{{Infobox" in line or "{{ Infobox" in line):
		return True
	return False

def get_name(line):
	if ("=" not in line):
		return line
	out = line.partition('= ')[2]
	out = re.sub("\n", "", out)
	return out

# Function: to find between a string
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

# Function: finds the latitude of the settlement
def get_latd(line):
	# CASE IF IT SAYS LATITUDE (SHORT LINE)
	if ("latitude" in line):
		line = get_name(line)
	else:
		if ("latm" not in line):
			line = get_name(line)
		else:
			line = same_line_latd(line)
	return line


# Function: finds the longitiude of the settlement
def get_long(line):
	if ("longitude" in line):
		line = get_name(line)
	else:
		if ("longm" not in line):
			line = get_name(line)
		else:
			line = same_line_long(line)

	return line


# Function: find the latitiude and longitude, if they are in the same line
def same_line_long(line):
	if ("longm" in line):
		pos_lon = True
		if ("EW=E" in line or "EW = E" in line):
			pos_lon = False
		lon = find_between(line, "longd", "longm")
		try:		
			lon = int(re.search(r'\d+', lon).group())
		except AttributeError:
			pass

		try:
			if pos_lon == True:
				lon = -(lon)
		except TypeError:
			pass 

		return lon

# Function: find the latitiude and longitude, if they are in the same line
def same_line_latd(line):
	if ("latm" in line):
		pos_lat = True
		if ("NS=N" in line or "NS = N" in line):
			pos_lat = False
		lat = find_between(line, "latd", "latm")
		try:		
			lat = int(re.search(r'\d+', lat).group())
		except AttributeError:
			pass

		try:
			if pos_lat == True:
				lat = -(lat)
		except TypeError:
			pass 
			
		return lat


target = open("filename.txt", 'w')

# MAIN
with open(WIKI_DUMPS, "r", encoding="utf-8") as f:
	#csv = []
	infobox = False
	count = 0
	#fo = open("exp.txt")
	for line in f:
		if start_info(line):
			infobox = True
			has_latd = False
			has_longd = False

		if (infobox == True):
			if (count == 1):
				name = get_name(line)
			if ("latd" in line or "latitude" in line):
				latd = line
				has_latd = True
			if ("longd" in line or "longitude" in line):
				longd = line
				has_longd = True
			count = count + 1

			if line == '\n':
				if (has_latd == True and has_longd == True):
					lat = "lat"
					if (latd == longd):
						longd = same_line_long(longd)
						latd = same_line_latd(latd)
						target.write(str(name))
						target.write("\t")
						target.write(str(longd))
						target.write("\t")
						target.write(str(latd))
						target.write("\n")
					else:
						latd = get_latd(latd)
						longd = get_long(longd)
						target.write(str(name))
						target.write("\t")
						target.write(str(longd))
						target.write("\t")
						target.write(str(latd))
						target.write("\n")
						#fo.write(name)
						#fo.write(latd)
						#fo.write(longd)
				infobox = False
				has_longd = False
				has_latd = False
				count = 0
				#csv = "".join(csv)
	#with open("file.txt","w",encoding="utf-8") as f:
	#	f.write(csv)
