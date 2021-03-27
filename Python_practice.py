#counties=["Arapahoe","Denver","Jefferson"]
#if counties[1]=="Denver":
    #print(counties[1])
#if "El Paso" in counties:
    #print("El Paso is in the list of counties") 
#else:
    #print("El Pase is not in the list of counties")  
#use the And operator
    #if "Arapahoe" in counties and "El Paso" in counties:
        #print("Arapahoe and El Paso are in the list of counties")
    #else:
        #print("Araoahoe or El Paso are not in the list of counties")
#use the or operator   
    #if "Arapahoe" in counties or "El Paso" in counties:
        #print("Arapahoe or El Paso are in the list of counties")
    #else:
    #   print("Arapahoe and El Paso are not in the list of counties")
 
#counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
#for county, voters in counties_dict.items():
 #   print(str(county)+" county has "+ str(voters)+ " registered voters.")
#voting_data=[{"county":"Arapahoe", "registered_voters":422829}, {"county":"Denver", "registered_voters":463353}, {"county":"Jefferson", "registered_voters": 432438}]

#Get each dictionary in the list of dictionaries
#for county_dict in voting_data:
#    print(county_dict)        

#Get each Dictionary in a list of dictionaries using the range() function
#for i in range(len(voting_data)):
#    print(voting_data[i])

#get the values from a list of dictionaries used nested loops
#for loop to retieve each dictionary
#for county_dict in voting_data:
    #nested for loop
    #for value in county_dict.values():
        #print(value)
#F string with the counties dictionary
#counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432582
#for county, voters in counties_dict.items():
 #   print(f"{county} county has {voters} registered voters.")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")
