# Election_Analysis

## Project Overview

This election audit aims to certify the recent Colorado congressional elections. Using election results from mail-in-ballots, punch cards, and direct recording electronics this audit using python to automate the process of calculating votes cast in the Colorado congressional district election. In addition to providing a formal examination of voting results, this audit aims to provide an automated python auditing system to be used for future congressional districts as well as senatorial districts and local elections.

This audit completed the following tasks to provide the Colorado Board of Elections with a formal examination of the voting results for the recent Colorado congressional election:

1.	The total number of votes cast
2.	A complete list of counties that participated in the election
3.	The total number of votes each county cast
4.	the percentage of votes each county cast
5.	the county with the largest number of votes cast
6.	A complete list of the candidates who received votes
7.	The total number of votes each candidate received
8.	The percentage of votes each candidate won
9.	The winner of the election based on popular vote

![PyPoll_Challenge_Txt_File](/Resources/PyPoll_Challenge_Txt_File.png)


## Resources

The following resources were used to complete this audit:

- Data Source: election_results.csv

- Software: Python 3.9.1, Visual Studio Code, 1.38.1

## Audit Results

### The analysis of the election shows that:

- There were 369,711 total votes cast in the congressional election.

![PyPoll_Challenge_Total_Votes](/Resources/PyPoll_Challenge_Total_Votes.png)

### The county results were:

- Jefferson county cast 10.5% of the vote and 38,855 total number of votes
- Denver county cast 82.8% of the vote and 306,055 total number of votes
- Arapahoe county cast 6.7% of the vote and 24,801 total number of votes
- Denver county had the largest turn out with the largest number of votes cast of 306,055


![PyPoll_Challenge_Total_Votes](/Resources/PyPoll_Challenge_County_Vote.png)


### The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes
  - Raymond Anthony Doane received 3.1% of the vote and 11,606 number of votes

  
![PyPoll_Challenge_Total_Votes](/Resources/PyPol_Challenge_Candidate_Results.png)
 
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

![PyPoll_Challenge_Total_Votes](/Resources/PyPol_Challenge_Winner.png)
  

## Audit Summary

The Colorado Election Commission is currently seeking a qualified team to create an automated process to audit and certify the results of congressional, senatorial, and local elections. The priority of the Colorado Election Commission is applicability of this audit system to future congressional, senatorial, and local elections. This code can be modified to do that. 

This code has already proven its ability to audit congressional elections, however it can be modified further to present voting results based on voters’ district instead of county, as congressional representatives are elected by constituents from their specific district. 

Additionally, for senatorial election, which are chosen by direct popular statewide elections, this code can be modified to present senatorial voting results based on various voter demographic data including district, county, gender and age. To do this, the code can be edited to iterate through lists and dictionaries of demographic voter data to retrieve the specific demographic data of interest, whether that be voters’ district, county, gender or age. 

Moreover, this code can be modified to audit local elections as well. City council, district attorney and mayors are elected in different ways based on the local city or town laws. In this way, the code can be modified to retrieve precise voter data that is pertinent to the local election being audited, whether that be a voters’ residential address, county, or district. This can be accomplished by iterating through lists and dictionaries of voter data to retrieve the exact data elements of interest for specific elections. 

Overall, this code can be modified in a variety of ways to be applied to future congressional, senatorial, and local elections in Colorado and the Colorado Election Commission should choose this code to be the auditing system for elections.
