import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def base_function():
    # Dictionary of college names and their corresponding URLs
    college_urls = {
        "Aryabhatta college": "https://aryabhattacollege.ac.in/",
        "Bhim Rao Ambedkar College ": "https://www.drbrambedkarcollege.ac.in/",
        "Daulat Ram College": "https://www.dr.du.ac.in/",
        "Deen Dayal Upadhyaya College": "https://dducollegedu.ac.in/",
        "Hans Raj College": "https://www.hansrajcollege.ac.in/",
    }
    
    user_input = input("Enter a URL or a college name: ").strip().lower()

    if user_input.startswith("http://") or user_input.startswith("https://"):
        return user_input
    else:
        lowercase_college_urls = {key.lower(): value for key, value in college_urls.items()}
        if user_input in lowercase_college_urls:
            return lowercase_college_urls[user_input]
        raise ValueError(f"College name '{user_input}' not found in the list.")

try:
    url = base_function()            
    print("Processed URL:", url)
except ValueError as e:
    print(e)

response = requests.get(url)    #scrape data from website home page
soup = BeautifulSoup(response.text, 'html.parser')

link_tag = soup.find('a', string ="Undergraduate courses")   #extarcting course page link
link_tag

if link_tag:
    relative_link = link_tag['href']
    courses_url = urljoin(url, relative_link)
    print("Courses URL:", courses_url)
else:
    print("Link not found")
    exit()

response = requests.get(courses_url)     #fetching provided courses list
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')   #extract table

if table:
    headers = [header.text.strip() for header in table.find_all('th')]
    rows = table.find_all('tr')

    table_data = []         #list to append the output
    
    for row in rows:
        cells = row.find_all('td')
        if cells:
            cell_data = [cell.text.strip() for cell in cells]
            table_data.append(cell_data)
            print(table_data)
else:
    print("Table not found")

#output file 
df = pd.DataFrame(table_data, columns=headers)
df.to_csv('C:/Users/hp/Desktop/images/Test_case1.csv', index=False)
print(f"Courses offered has been saved to 'Test_case1.csv'")



