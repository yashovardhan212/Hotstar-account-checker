def ln_validation(line):
	validators = ["@gmail.com","@hotmail.com" , "@yahoo.com" , "password"  ]
	for vds in validators:
		if vds in line:
			return True
	return False


def init_file():
	with open("final_data.txt","w") as file:
		file.write("data\n")

def writer(line):
	with open("final_data.txt","a") as file:
		file.write(str(line))	
def checker():
	with open("desc.txt","r") as file:
		for line in file:
			if ln_validation(line):
				writer(line)
			

def main():
	init_file()
	checker()


main()
				
		


		
