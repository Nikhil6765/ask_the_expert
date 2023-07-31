from tkinter import Tk, simpledialog,messagebox

# reading data from the text file

def read_from_file():
    with open('ques_ans.txt') as file:
        for line in file:
            line=line.rstrip('\n') # removes new line character
            country,city=line.split('/')
            


print("Ask The Expert - Capital cities of the World")

root=Tk() # creates an empty Tkinter Window

root.withdraw()  # Hide Tkinter Window 
the_world={}

root.mainloop()