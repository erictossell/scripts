import datetime
import requests
import csv
from bs4 import BeautifulSoup

date = datetime.datetime.today()
date = date.strftime('%Y-%m-%d_%H-%M-%S')
exportFile = 'yellow_pages_ON_Unions'+str(date)+'.csv'
headers = ['Name', 'Address', 'Description', 'Phone','2nd Phone', 'Website']
pageNumber = 1
with open (exportFile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    
    while pageNumber < 28:
        url = 'https://www.yellowpages.ca/search/si/'+str(pageNumber)+'/Unions+%26+Labour+Organizations/Ontario+ON'
        print(url)
        response = requests.get(url)   

        soup = BeautifulSoup(response.text, 'html.parser')

        listings = soup.find_all('div', class_='listing__content__wrapper')

        for listing in listings: 
            newRow = [] 
            name = listing.find('a', {'class': 'listing__name--link listing__link jsListingName'}).text
            newRow.append(name)
            #print(f'Name: {name}')
            if listing.find('div', {'class': 'listing__address'}):
                street_address = listing.find('div', {'class': 'listing__address'}).text.strip()
                #print(f'Address: {street_address}')
                index = street_address.find('\n')
                sliced_address = street_address[:index]
                newRow.append(sliced_address)
                
            descriptionDiv = listing.find('div', {'class': 'listing__detailss'})
            if descriptionDiv != None:
                description = descriptionDiv.find('article', {'class': 'listing__details__teaser'}).text.strip()
                #print(f'Description:  {description}')
                newRow.append(description)
            else:
                newRow.append('No description')
            
                
            mailer = listing.find('div', {'class': 'listing__mlr__root'})  
            
            phoneCounter = 0
            for phone in mailer.find_all('ul', {'class': 'mlr__submenu'}):
                for number in phone.find_all('li', {'class': 'mlr__submenu__item'}):
                    if phoneCounter == 0:
                        index = number.text.find('\n')
                        sliced_number = number.text[:index]
                        newRow.append(sliced_number)
                        #print(f'Phone:  {number.text}')
                    elif phoneCounter == 1:
                        index = number.text.find('\n')
                        sliced_number = number.text[:index]
                        newRow.append(sliced_number)                
                    
                    phoneCounter += 1
            if phoneCounter == 1:
                newRow.append('No second phone number')    
            website = mailer.find('li', {'class': 'mlr__item mlr__item--website'})
            if website:
                siteURL = website.find('a', {'class': 'mlr__item__cta'}).get('href')
                #print(f'Website: {siteURL}')
                
                index = siteURL.find('%2F')
                sliced_siteURL = siteURL[index+3:]
                surl = sliced_siteURL[3:-3]
                newRow.append(surl)
            else:
                newRow.append('No website')
            #print(newRow)
            #print('---------------------------------')
            writer.writerow(newRow)           
        pageNumber += 1