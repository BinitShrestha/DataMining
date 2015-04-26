# EXTRACTING COMPANIES
# FOR AUTOMOBILE INDUSTRIES
# CREATED BY BINIT & NITICON

import re, os, sys, string, json

WIKI_DUMPS = "new.txt"

target = open("filename.txt", 'w')

# FUNCTIONS
# Function: to siginify when to search for settlements
def start_info(line):
	if ("{{Infobox company" in line or "{{ Infobox company" in line):
		return True
	return False

def get_name(line):
	if ("=" not in line):
		return line
	out = line.partition('= ')[2]
	out = re.sub("\n", "", out)
	return out

def get_loc(line):
	out = line.partition('= ')[2]
	out = re.sub('[[]', '', out)
	out = re.sub('[]]', '', out)
	out = re.sub("\n", "", out)
	return out

def get_date(line):
	out = int(re.search(r"[0-9]{4,7}", line).group())
	return out

# MAIN
with open(WIKI_DUMPS) as f:
	infobox = False
	count = 0
	for line in f:
		if start_info(line):
			infobox = True
			related = False

		if (infobox == True):
			if (count == 1):
				name = get_name(line)
			if ("location_city" in line):
				loc_city = get_loc(line)
			#if ("location_country" in line):
			#	loc_country = line
			if ("foundation" in line):
				date = get_date(line)
			if ("Automobile" in line or "Motors" in line):
				related = True
			count = count + 1

			if line == '\n':
				if (related == True):
					target.write(str(name))
					target.write("\t")
					target.write(str(date))
					target.write("\t")
					target.write(str(loc_city))
					target.write("\n")
				infobox = False
				related = False
				count = 0
