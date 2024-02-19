import requests
from bs4 import BeautifulSoup

class Leaderboard():
    """
    This class is used to scrape the Deep Space Airships leaderboards
    """
    def __init__(self) -> None:
        pass

    def fetch_ships(self,url:str,limit=None):
        """
        Multiplies two numbers and returns the result.
    
        Args:
            url (str): The leaderboard URL to scrape.
            limit (int): Limit of how many ships to retrieve from the page.
    
        Returns:
            dict: Dictonary of ships, the key is the hexcode followed by a dict containing name (str), rank (str), and score (str).
        """
        ship_info={}
        if "ship" in url:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            ships = soup.find("tbody").find_all("tr",limit=limit)
            for ship in ships:
                rawData=ship.find_all("td")
                data=[i.text.strip() for i in rawData]
                hexcode=data[2].replace("{","").replace("}","")
                ship_info.update({hexcode:{"name":data[1],"rank":data[0],"score":data[3].split(" ")[0]}})
            #print(ship_info)
        elif "pilot" in url:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            ships = soup.find("tbody").find_all("tr",limit=limit)
            for ship in ships:
                rawData=ship.find_all("td")
                data=[i.text.strip() for i in rawData]
                name=data[1]
                ship_info.update({name:{"rank":data[0],"score":data[3].split(" ")[0]}})
        elif "clan" in url:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            ships = soup.find("tbody").find_all("tr",limit=limit)
            for ship in ships:
                rawData=ship.find_all("td")
                data=[i.text.strip() for i in rawData]
                clan=data[1]
                ship_info.update({clan:{"rank":data[0],"score":data[3].split(" ")[0]}})
        else:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            ships = soup.find("tbody").find_all("tr",limit=limit)
            for ship in ships:
                rawData=ship.find_all("td")
                data=[i.text.strip() for i in rawData]
                hexcode=data[2].replace("{","").replace("}","")
                ship_info.update({hexcode:{"name":data[1],"rank":data[0],"score":data[3].split(" ")[0]}})
        return ship_info