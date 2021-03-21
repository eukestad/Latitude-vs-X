import os
import csv

#create a table object and initialize a row element

table = "<table class='table table-bordered table-striped'>\n<thead class='thead-dark'>"
table+= "\n<tr>"


#Get csv file path
'''---------------'''
cities_path = os.path.join(".", "resources", "cities.csv")

#Open cities csv file
'''----------------------'''
with open(cities_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #seperate header
    header = next(csvreader)
    
    #add header values to table header <th>
    for name in header:
        table = table + '\n' + f"<th>{name}</th>"
    table+='\n</tr>\n</thead>\n<tbody>'

    # add values to the table body <td>
    #read rows
    for row in csvreader:
        table+='<tr>'
        for i in range(len(row)):
            table+='\n' + f"<td>{row[i]}</td>"
        table+='\n</tr>\n'
    
    table+='</tbody>\n</table>'
 
#5 save the table in html format.
'''------------------------------------------------'''
#set file path
file_path = os.path.join("Resources", "data.html")   
    # Open file in "write" mode ('w') .
with open(file_path, 'w') as html_file:

    # write lines into the file
    html_file.write('''<pre>Note: Open this file in an HTML editor, add bootstrap links and classes to make 
                        it pretty and responsive. Save as a separate HTML file to use in web-dev homework.
                        Warning: If not, running python script again will overwrite your work.<pre>\n''')
    html_file.write(table)
  
