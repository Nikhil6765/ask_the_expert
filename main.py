from tkinter import Tk, simpledialog,messagebox

# reading data from the text file

def read_from_file():
    with open('ques_ans.txt') as file:
        for line in file:
            line=line.rstrip('\n') # removes new line character
            country,city=line.split('/') # Country stores the word before "/" and 
                                         # City stores the word after "/"

# creating function to add new country and new city to the text file 

def write_to_file(country_name,city_name):
    with open('ques_ans.txt', 'a') as file: # here a means "append" , add new information to the file
        file.write('\n' + country_name + '/' + city_name) 





print("Ask The Expert - Capital cities of the World")

root=Tk() # creates an empty Tkinter Window

root.withdraw()  # Hide Tkinter Window 
the_world={}
read_from_file()

while True:
    query_country=simpledialog.askstring('country','Type The Name of the Country') # the first parameter is the title , the second parameter tells the user what to do
    if query_country in the_world:
        result=the_world[query_country]
        messagebox.showinfo('Answer ', 'The Capital of ' + query_country + 'is' + result +'!')


root.mainloop()