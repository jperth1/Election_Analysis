#data we need to retrieve
#total number of votes cast
#complete list of candidates who recieved votes
#total number of votes each candidate recieved 
#percentage of cotes each candidate won
#the winnder of the election based on popular vote

#Assign a variable for the file to load and the path
#file_to_load= 'Resources/election_results.csv'
#Open the election results and read the file using a with statment.
#with open(file_to_load) as election_data:
    
    #to do: perform analysis.
    #print(election_data)
    
#Use the csv and os modules to open a file from an indirect path
#import csv and os modules
import csv
import os
#assign a variable for the file to load and the path
file_to_load =os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#open the election results and read the file using a with statment
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
        

# Using the open() function with the "w" mode we will write data to the file.
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("---------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    