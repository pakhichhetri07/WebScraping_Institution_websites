# Web Scraping Script for College Courses Offered in Indian Institutions

## Description
This Python script aims to extract course offerings from Indian colleges. Users can input either a college name or it's website URL. The script then attempts to scrape the course information from the provided website.

If user has given college website homepage url, it directly hits the web browser and try to extract the required data by first extracting the url of courses offered page and thereby creating new url (termed as relative link) to extract the list of courses offered. 

If the user provides a college name, it first searches for the url in dictionary. If found, it extracts the data with same mechanism otherwise exits the code.

## Pre requisite:
Python version : Python 3.12.5
Required libraries : requests, BeautifulSoup, pandas

## TestCase
Daulat Ram College (https://www.dr.du.ac.in/) --> Delhi University

