import requests
import json
import time
from bs4 import BeautifulSoup
import time
import pandas as pd

# loop that runs indefinitely with a 5 second delay between each iteration
while True:
    # read the HTML data from the URL and store it in a variable
    scrapped_data = pd.read_html('https://coinmarketcap.com')
    
    # convert the HTML data into a pandas dataframe
    df = pd.DataFrame(Scrapped_Data[0])
    
    # drop unnecessary columns from the dataframe
    df = df.drop(['#','Unnamed: 11', 'Last 7 Days'], axis=1)
    
    # Rename the columns as per the models
    df.rename(columns = {'Name':'name','Price':'price','1h %':'percent_1h', '24h %':'percent_24h',
                                '7d %':'percent_7d', 'Market Cap':'market_cap', 'Volume(24h)':'volume_24h','Circulating Supply':'circulating_supply'}, inplace = True)
    #Fill na values with string none
    df = df.fillna('none')
    # Sending request to the api for posting the scrapped data
    r = requests.post('http://127.0.0.1:8000/scrapApi/', json=df.to_dict('records'))
    print(r.status_code)
    
    if r.status_code == 201:
        print("complete")
    else:
        print("error")
    time.sleep(5)














# while True:
    
#     page = requests.get("https://coinmarketcap.com/")
#     soup = BeautifulSoup(page.content, "html.parser")
#     # Find all the rows in the table
#     rows = soup.find_all("tr")

#     # Loop through each row
#     f_data = {}
#     for row in rows:
#         # Find all the columns in the row
#         columns = row.find_all("td")
#         # print(columns)
        

#         # If the row contains 8 columns, it's a valid coin data
#         if len(columns) == 12:
#             # Extract the data from each colum
            
#             name = columns[2].text            
#             price = columns[3].text
#             h1 = columns[4].text
#             h24 = columns[5].text
#             d7 = columns[6].text
#             market_cap = columns[7].text
#             volume = columns[8].text
#             circulating_supply = columns[9].text
            

#             # Store the data in a dictionary
#             temp = {
#                 "name": name,
#                 "price": price,
#                 "percent_1h": h1,
#                 "percent_24h": h24,
#                 "percent_7d": d7,
#                 "market_cap": market_cap,
#                 "volume_24h": volume,
#                 "circulating_supply": circulating_supply
#             }
#             print(temp)
            
            
#             f_data[name] = temp    
        
#     r = requests.post('http://127.0.0.1:8000/scrapApi/', data=f_data)
#     if r.status_code == 201:
#         print("complete")
#     else:
        
#         print("error")
        
#     time.sleep(25)   
