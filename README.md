# Election_Analysis

## Project Overview

This election audit aims to certify the recent colorado congressional elections. Using election results from mail-in-ballots, punch cards, and direct recording electronics, this audit using python to automate the process of calculating votes cast in the Colordado congressional district election. In additioin to providing a formal examination of voting results, this audit aims to provide an automated python auditing system to be used for future congressional districts as well as senatorial districts and local elections. 

This audit completed the following tasks to provide the Colorado Board of Elections with an formal examination of the voting results for the recent Colorado congressional election:

1. The total number of votes cast
2. A complete list of counties that participated in the election
3. The total number of votes each county cast
4. the percentage of votes each county cast
5. the county with the largest number of votes cast
6. A complete list of the candidates who recived votes
7. The total number of votes each candidate recieved
8. The percentage of votes each candidate won
9. The winner of the election based on popular vote

![PyPoll_Challenge_Txt_File](/Resources/PyPoll_Challenge_Txt_File.png)


## Resources

The following resources were used to complete this audit:

- Data Source: election_results.csv

- Software: Python 3.9.1, Visual Studio Code, 1.38.1

## Audit Results

How many votes were cast in this congressional election?
Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
Which county had the largest number of votes?
Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

The analysis of the election shows that:

- There were 369,711 total votes cast in the congressional election.

![PyPoll_Challenge_Total_Votes](/Resources/PyPoll_Challenge_Total_Votes.png)


- Three counties made up the congressional election district and the county results were:
- Jefferson county cast 10.5% of the vote and 38,855 total number of votes
- Denver county cast 82.8% of the vote and 306,055 total number of votes
- Arapahoe county cast 6.7% of the vote and 24,801 total number of votes

![PyPoll_Challenge_Total_Votes](/Resources/PyPoll_Challenge_County_Vote.png)

- Denver county had the largest turn out with the largest number of votes cast of 306,055

![PyPoll_Challenge_Total_Votes](/Resources/Py_Poll_Challenge_Largest_County.png)


- The candidate results were:
  - Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of votes
  - Diana DeGette recieved 73.8% of the vote and 272,892 number of votes
  - Raymond Anthony Doane recieved 3.1% of the vote and 11,606 number of votes
  
  ![PyPoll_Challenge_Total_Votes](/Resources/PyPol_Challenge_Candidate_Results.png)
 
- The winner of the election was:
  - Diana DeGette, who recieved 73.8% of the vote and 272,892 number of votes

  ![PyPoll_Challenge_Total_Votes](/Resources/PyPol_Challenge_Winner.png)
