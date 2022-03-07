> # Norman PD Incidents Summary
### Author : Aditya K Kasturi 

__About:__
- This project uses Python, Linux, and Unix commadline, Git, SQLite3, CSV or PDF data which utilizes PDF or CSV data from websites and process the data and store it into database for further analysis. For this project I have used Norman Police Department Daily Incidents Summary Data. The URL is mentioned below in Running the Porgram section. 

__Libraries and Packages Used:__
- os
- sys
- urlib
- sqlite3
- pytest
- re
- argparse

> ### Description

__Running the Program:__
- The program can be run by utilizing the commandline.
- To run the program, navigate to the project0 folder and run the main.py file 
- The main.py can be run by using the following command: 
  ```
  pipenv run python main.py --incidents url 
  ``` 
- At the place of "url" , you can paste any daily incidents summary url from the normanpd database. 
- I have used the following url: 
  url = https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf
  
__Result:__
- Printing out all the nature of incidents and their frequncy of occurance
  
__Functions:__

- In the main.py file, There are six functions:

0. __main.py__ :  The main.py file calls all the functions from project0.py and executes the flow of the project.
                  The main.py has all different funtions imported from the project0.py, it contains the following functions
                  ```
                  
                  fetch_incidents()
                  
                  extract_incidents(incident_data)
                  
                  createdb()
                  
                  populatedb(db,incidents)
                  
                  statusdb()
                  ```
1. __fetch_incidents()__ : The fetch_incidents() funtion takes the url string and utilizes the python library urllib, and reads the data into the byte stream format.
2. __extract_incidents(incident_data)__: extract_incidents(incident_data) takes theincident_data returned using the fetch_incidets() funtion. Here, The use of PyPDF2, which fetches the data, organizes it into the form of tuples and each field is separated by \n. 
3. __createdb()__: Initially it does not take any input paraments,  it creates a table called incidents and it calls the funtions "db" here. The database is creted using sqlite3
                  ```
                  db = 'normanpd.db'
                  ```
4. __populatedb(db,incidents)__:  The function takes db and incident_data as an input and inserts them to the database table named incidents.
5. __statusdb()__: This function takes input statements and fetches the summary of the data. 
        
  
