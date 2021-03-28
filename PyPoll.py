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

#Initialize total_votes counter
total_votes=0

#Initialize candidate_options list
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file using a with statment
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to total_votes count
        total_votes += 1
        
        #print the canidate name from each row
        candidate_name=row[2]
        
        #if candidate does not match any existing candidate
        if candidate_name not in candidate_options:
        #Add candidate_name to candidate_options list 
            candidate_options.append(candidate_name)
            
            #track that candidate's vote count
            candidate_votes[candidate_name] = 0
            
        #Add vote to that candidates' counter   
        candidate_votes[candidate_name] += 1
        
        
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate options list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # print out each candidate's name, vote count, and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  print out the winning candidate, vote count and percentage to terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
    
#Print the candidate vote dictionary.        
print(candidate_votes)
        
#print candidates_options list
print(candidate_options)

# print the total votes    
print(total_votes)
        

# Using txzhe open() function with the "w" mode we will write data to the file.
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("---------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    