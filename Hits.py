
def initial_pp():
	with open("Hits.txt","w") as  file:
		file.write("Email "+"		"+"Passwd" + "		" + " Status" + "\n")

def writer(line):
	with open("Hits.txt","a") as file:
		file.write(str(line.strip()) + "\n")
def line_checker(line):
	ll_ln = line.split()
	if "Maximum" in ll_ln or "Hit" in ll_ln:
		writer(str(line))



def main():
	initial_pp()
	with open("report.txt","r") as file:
		for line in file:
			line=line.strip()
			line_checker(line)

main()
