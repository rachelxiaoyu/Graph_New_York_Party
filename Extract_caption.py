%matplotlib inline
import matplotlib
import seaborn as sns
matplotlib.rcParams['savefig.dpi'] = 2 * matplotlib.rcParams['savefig.dpi']
import requests

def iter_flatten(target):
    """iter_flatten(list_of_lists) -> flat list"""
    depth = 0
    targets = [iter(target)]
    accumulator = list()
    while True:
        try:
            element = next(targets[depth])
        except StopIteration:
            if depth == 0: return accumulator
            else:
                depth -= 1
                targets.pop()
        else:
            if hasattr(element,"__iter__"):
                targets.append(iter(element))
                depth += 1
            else: accumulator.append(element)
                
url = "http://www.newyorksocialdiary.com/party-pictures"
from bs4 import BeautifulSoup
parent_div = []
for i in range(28):
    if i == 0:
        response = requests.get(url)
    else:
        response = requests.get(url, params={"page": i})
        #print response.url
        #http://www.newyorksocialdiary.com/party-pictures?page=9
    soup = BeautifulSoup(response.text)
        #print soup.prettify()
        #parent_div = soup.find_all('span', attrs={'class': 'field-content'}) #Find (at most) *one*
    parent_div.append(soup.find_all('span', attrs={'class': 'field-content'}))
parent_div = list(iter_flatten(parent_div))

pages = parent_div[0:(len(parent_div)-1):2]
dates = parent_div[1:(len(parent_div)-1):2]
pages_ht = []
for i in range(len(pages)):
    pages_ht.append(pages[i])
dates_ht = []
for i in range(len(dates)):
    dates_ht.append(dates[i])
#We want photos from parties before December 1st, 2014
pages_ht =  pages_ht[dates_ht.index("Monday, November 24, 2014"):]
dates_ht=   dates_ht[dates_ht.index("Monday, November 24, 2014"):]
pages_ht=   pages_ht[0:(len(pages_ht)-1)]

from string import punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation or c =="-")
caption=[]
for i in range(len(pages_ht)):
#for i in range(10): 
#for x in range(1):
   pages_ht[i] = pages_ht[i].encode('ascii', 'ignore').decode('ascii')
   if " " in str(pages_ht[i]):
      url_string=str(pages_ht[i]).replace(" ", "-")     
   else:
      url_string=str(pages_ht[i])
        
   url_string=strip_punctuation(url_string)
#   print url_string
   year_temp=dates_ht[i]
   date_len=len(year_temp)
   year=str(year_temp[date_len-4:date_len])
   url = "http://www.newyorksocialdiary.com/party-pictures/"+ year+ "/"+ url_string
#   print url
   response = requests.get(url)
   soup = BeautifulSoup(response.text)
   blob1 = soup.find_all("div", {'align': 'center', 'class': 'photocaption'}, text=True)
   blob2 = soup.find_all("td", {'valign': 'top', 'class': 'photocaption'}, text=True)
   blob3 = soup.find_all("td", {'valign': 'top', 'class': 'photocaption', 'style': 'background-color:#faf9ee'}, text=True)
	# For pages older than Sept 4
   blob4 = soup.find_all("font", {'size': 1, 'face': 'Verdana, Arial, Helvetica, sans-serif'}, text=True)
   caption=caption+blob1+blob2+blob3+blob4
   #print i
   #print len(caption)
df = pd.DataFrame(caption, columns=["colummn"])
df.to_csv('list.csv', index=False)
