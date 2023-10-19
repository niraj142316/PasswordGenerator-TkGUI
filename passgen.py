from tkinter import *         #importing the * from tkinter module
import random                 #importing the random module

root = Tk()                    #creating a window 
root.title('PassGenApp')       #set the title for the application
root.geometry("600x250")       #set the geometry
passwrd = StringVar()          #creating the variable to store the generated password
passlen = IntVar()             #creating variable to store the length of password
passlen.set(0)


def passwordgenerate():        # creating function to generate the password
	pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
			'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
			'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
			'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
			'9', '0', ' ', '!', '@', '?', '>', '%', '^', '&',
			'*', '(', ')','+','-','/','#','$','<',',','.','~','`']
	password = ""
	for x in range(passlen.get()):
		password = password + random.choice(pass1)
	passwrd.set(password)

#labels for the text

Label(root, text="Password Generator", bg='orange', fg='black', font="ariel 25 bold").pack()
Label(root, text="Enter the length of password", font="ariel 15 bold").pack(pady=3)

#creating an entry where you can enter the length of password 
Entry(root, textvariable=passlen).pack(pady=3)

#creating a button for call the passwordgenerate function 
Button(root, text="Generate Password",font="ariel 20 bold", bg='blue', command=passwordgenerate).pack(pady=7)

#creating this entry to display the generated password after calling the passwordgenerate function
Entry(root, textvariable=passwrd, font="ariel 25 bold", bg='black', fg='red', width=20).pack(pady=3)
root.mainloop()
