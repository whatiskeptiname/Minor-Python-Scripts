import csv
import requests
from bs4 import BeautifulSoup
import time



url = "https://www.nrb.org.np/forex" #url of nrb forex

class Fetch_forex: # class to manage Scrapping Process (but not necessary ;))

    def scrape(self, url):
        
        response = requests.get(url, timeout=10) 
        soup = BeautifulSoup(response.content, 'html.parser') #constructing the soup object

        table = soup.find_all('table')[1] # find all the table tag

        rows = table.select('tbody > tr') # find tr tag inside tbody tag
        i = 0
        for _ in rows: #looping for all the td to store each td data
            data = [td.text.rstrip() for td in rows[i].find_all('td')]

            print(data) #Uncomment to see the forex data 

            # open the file in the append mode
            with open('./forex_data.csv', 'a', encoding='UTF8') as f:
                # create the csv writer
                writer = csv.writer(f)
                # write a data to the csv file
                writer.writerow(data)
                i = i+1

fetch_todays_data = Fetch_forex() # fetch_todays_data object creation

while(True):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    print(current_time) #uncomment to see the current time

    if(current_time == "10:00:00"): # at exact 10 AM the data is fetched and stored in csv format 
        fetch_todays_data.scrape(url) #calling the method
        time.sleep(1) # sleep for 1 sec to prevent from multiple write