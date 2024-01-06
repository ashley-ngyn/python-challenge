# python-challenge

For PyBank

Create a Python script that analyzes the records to calculate each of the following values:
    - The total number of months included in the dataset
    - The net total amount of "Profit/Losses" over the entire period
    - The changes in "Profit/Losses" over the entire period, and then the average of those changes
    - The greatest increase in profits (date and amount) over the entire period
    - The greatest decrease in profits (date and amount) over the entire period


For PyPoll

Your task is to create a Python script that analyzes the votes and calculates each of the following values:
    - The total number of votes cast
    - A complete list of candidates who received votes
    - The percentage of votes each candidate won
    - The total number of votes each candidate won
    - The winner of the election based on popular vote




list of sources used:
    - 01: lists_solution.py
    - 02: https://docs.python.org/3/library/csv.html
    - 03: write_solution.py
    - 04: cereal_solution.py
    - 05: lists_solution.py
    - 07: https://docs.python.org/3/library/stdtypes.html#range
    - 08: https://www.geeksforgeeks.org/how-to-round-numbers-in-python/
    - 09: https://www.pythontutorial.net/python-basics/python-write-text-file/
    - 10: https://stackoverflow.com/questions/26822336/how-to-add-to-an-already-existing-variable-in-python
    - 11: https://www.knowledgehut.com/blog/programming/python-rounding-numbers


    source 01 was used to create empty lists

        total_months = []
        total_amount = []
        total_change = []
        candidate_list = []


    sources 02 and 03 were used to locate and open a cvs file
    
        with open(cvspath, encoding="utf-8") as cvsfile:
        cvsreader = cvs.reader(cvsfile)


    source 04 was used to read any headers within the cvs file
        
        cvsheader = next(cvsfile)


    source 05 was used append() function which adds to the end of a list
        total_months.append(row[0])
        total_months.append(int(row[1]))
        candidate_list.append(row[2])


    source 06 was used for the len() function which returns the number of items in a list
        
        for i in range(len(total_amount)-1):
        print(f"Total Months: {len(total_months)}")


    source 07 was used for range(), it is important to note that -1 was added because the source noted that if there was no column value, then it equals 1 (this took a lot debugging for me)
        
        for i in range(len(total_amount)-1):


    source 08 was used for round() to round an integer to the second decimal place
        
        print(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")


    source 09 was used to export a test file of the analysis
    
        - how to create textfile and find the path
            filepath = os.path.join("analysis", "PyBank_analysis.txt")
            filepath = os.path.join("analysis", "PyPoll_analysis.txt")
            with open(filepath, 'w') as textfile:
        - how to write text in file, f.write() writes a list of text strings
            textfile.write("Financial Analysis")
            textfile.write("Election Results")
        - the command \n creates a new line
            textfile.write("\n----------------------------")
    

    source 10 was used to add the variables using +=
        
        if row[2] == "Charles Casper Stockham":
            charles +=1
        elif row[2] == "Diana DeGette":
            diana +=1
        elif row[2] == "Raymon Anthony Doane":
            raymon +=1
    
    source 11 was used to round to third decimal place round(x, 3)

        charles_percent = round(((charles/total_votes) * 100), 3)
        diana_percent = round(((diana/total_votes) * 100), 3)
        raymon_percent = round(((raymon/total_votes) * 100), 3) 

