from bs4 import BeautifulSoup
from urllib.request import urlopen
lk = "https://www.espncricinfo.com/live-cricket-score"
try:
    cric_site = urlopen(lk)
    soup_is_deliciuos = BeautifulSoup(cric_site, "html.parser")
    print(soup_is_deliciuos.prettify())
except Exception as e:
    print("how hard is just copy pasting a link my guy?")
 # we used prettify as we want only the important things to be shown and not jargon that we don't need.

# in my defense, scraping was a lot harder than I thought. how the hell is the this the 6th task this hard when I could do weather. Jesus
