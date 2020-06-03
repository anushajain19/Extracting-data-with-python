'''
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_589717.xml (Sum ends with 12)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

from bs4 import BeautifulSoup
import requests

url = 'http://py4e-data.dr-chuck.net/comments_589717.xml'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
count = soup.find_all('count')
total =  sum(int(i.text) for i in count)
print(f'The sum of all count in doc are: {total}')
