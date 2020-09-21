import mechanicalsoup
import sys

print(sys.argv[1])
br = mechanicalsoup.StatefulBrowser()

br.open(sys.argv[1])

cont = str(br.get_current_page().find_all(['textarea'])[0])

with open("pastebin_data.txt","w") as file:
	file.write(cont)
with open("pastebin_data.txt","r") as fl:
	for ln in fl:
		ln = ln.split()
		newstr = str(ln[0])+str(ln[1])
		with open("pastebin_combos.txt","a") as fll:
			fll.write(newstr + "\n")
