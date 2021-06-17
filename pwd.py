import sys, pyperclip, os 

def find(account):
	file = open("pwds.txt", 'r')
	for line in file:
		l = line.split(' : ')
		if l[0] == account:
			file.close()
			return 1
	file.close()
	return 0

def retrieve(account): 
	file = open("pwds.txt", 'r')
	for line in file:
		l = line.split(' : ')
		s = l[1].rstrip()
		if l[0] == account:
			pyperclip.copy(s) 
			print("Password :", s, "for", account, "account has been copied to your clipboard!") 
			break
	else: 
		print("No such account record exists!") 
	file.close()

def add(account, pwd):

	file = open("pwds.txt", 'r')
	record = {}
	for line in file:
		l = line.split(' : ')
		record[l[0]] = l[1].rstrip()
	file.close()

	record[account] = pwd
	new = open("tempFile.txt", 'w')
	for acc in record.keys():
		s = acc + ' : ' + record[acc] + '\n'
		new.write(s)
	new.close()

	os.remove("pwds.txt")
	os.rename("tempFile.txt", "pwds.txt")


def delete(account):
	file = open("pwds.txt", 'r')
	record = {}
	for line in file:
		l = line.split(' : ')
		record[l[0]] = l[1].rstrip()
	file.close()

	del record[account] 
	new = open("tempFile.txt", 'w')
	for acc in record.keys():
		s = acc + ' : ' + record[acc] + '\n'
		new.write(s)
	new.close()

	os.remove("pwds.txt")
	os.rename("tempFile.txt", "pwds.txt")


if __name__ == "__main__": 

	length = len(sys.argv)

	if length == 2:
		account = sys.argv[1]
		retrieve(account)

	elif length == 3:
		operation = sys.argv[1]
		account = sys.argv[2]

		if operation == 'add':
			if find(account):
				print("Account already exists!")
			else:
				pwd = input("Enter Password : ")
				add(account, pwd)
				print('Account added successfully!')

		elif operation == 'update':
			if not find(account):
				print("Account doesn't exist!")
			else:
				newPwd = input("Enter new Password : ")
				add(account, newPwd)
				print('Account updated successfully!')

		elif operation == 'delete':
			if not find(account):
				print("Account doesn't exist!")
			else:
				delete(account)
				print('Account deleted successfully!')

		else:
			print("Enter valid operation!")

	elif length != 1:
		print("Enter valid details!")