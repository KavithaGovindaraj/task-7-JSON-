import requests

class BreweriesInfo:
    def __init__(self, base_url, states):
        self.base_url = base_url
        self.states = states

    def fetch_breweries(self, state):
        response = requests.get(f"{self.base_url}?by_state={state}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def list_breweries(self):
        for state in self.states:
            breweries = self.fetch_breweries(state)
            print(f"Breweries in {state}:")
            for brewery in breweries:
                print(brewery['name'])

    def count_breweries(self):
        for state in self.states:
            breweries = self.fetch_breweries(state)
            print(f"Number of breweries in {state}: {len(breweries)}")

    def count_brewery_types(self):
        for state in self.states:
            breweries = self.fetch_breweries(state)
            city_brewery_types = {}
            for brewery in breweries:
                city = brewery['city']
                brewery_type = brewery['brewery_type']
                if city not in city_brewery_types:
                    city_brewery_types[city] = {}
                if brewery_type not in city_brewery_types[city]:
                    city_brewery_types[city][brewery_type] = 0
                city_brewery_types[city][brewery_type] += 1

            print(f"Brewery types in cities of {state}:")
            for city, types in city_brewery_types.items():
                print(f"City: {city}")
                for brewery_type, count in types.items():
                    print(f"  {brewery_type}: {count}")

    def count_breweries_with_websites(self):
        for state in self.states:
            breweries = self.fetch_breweries(state)
            breweries_with_websites = [brewery for brewery in breweries if brewery.get('website_url')]
            print(f"Number of breweries with websites in {state}: {len(breweries_with_websites)}")
            for brewery in breweries_with_websites:
                print(brewery['name'], brewery['website_url'])

if __name__ == "__main__":
    base_url = "https://api.openbrewerydb.org/breweries"
    states = ["Alaska", "Maine", "New York"]
    breweries_info = BreweriesInfo(base_url, states)

    print("\nListing breweries in specific states:")
    breweries_info.list_breweries()

    print("\nCounting breweries in each state:")
    breweries_info.count_breweries()

    print("\nCounting brewery types in each city:")
    breweries_info.count_brewery_types()

    print("\nCounting breweries with websites in specific states:")
    breweries_info.count_breweries_with_websites()


"""    
Output:
Listing breweries in specific states:
Breweries in Alaska:
49th State Brewing Co
49th State Brewing Co - Anchorage
Alaskan Brewing Co.
Anchorage Brewing Co
Arkose Brewery
Baleen Brewing Co.
Baranof Island Brewing Co
Barnaby Brewing Company
Bawden Street Brewing Company
Bearpaw River Brewing Co
Bleeding Heart Brewery
Broken Tooth Brewing Co
Cooper Landing Brewing Company
Cynosure Brewing
Denali Brewing Company
Devil's Club Brewing
Faults Brewing
Forbidden Peak Brewery
Gakona Brewing Company
Girdwood Brewing Company
Glacier Brewhouse
Grace Ridge Brewing
Growler Bay Brewing Co
Haines Brewing Co
Harbor Mountain Brewing Co
Homer Brewing Co
HooDoo Brewing Co
Humpy's Great Alaskan Alehouse
Icy Strait Brewery
Inside Passage Brewing Company LLC
Kassik's Brewery
Kenai River Brewing Co
King Street Brewing Co
Klondike Brewing Company
Kodiak Island Brewing Co
Last Frontier Brewing Company
Matanuska Brewing Company - Downtown Brewpub
Matanuska Brewing Company - Eagle River
Matanuska Brewing Company - Midtown Brewpub
Midnight Sun Brewing Co
Midnite Mine Brewpub
Odd Man Rush
Onsite Brewing Company
QUAKE! Brewing Company
Resolution Brewing Company
RoughWoods Inn
Seward Brewing
Silver Gulch Brewing Co
Skagway Brewing Co
St Elias Brewing Co
Breweries in Maine:
2 Feet Brewing Company
Airline Brewing Company
Allagash Brewing Co
Andrews Brewing Co
Atlantic Brewing Co
Atlantic Brewing Co / Bar Harbor Brewing
Austin Street Brewery
Bag and Kettle, The
Banded Brewing Company
Bangor Beer Co.
Barreled Souls Brewing Company LLC
Bath Brewing Company
Battery Steele Brewing
Baxter Brewing Co, LLC
Bear Bones Beer
Bear Bones Beer
Belfast Bay Brewing Co
Bigelow Brewing Company
Bissell Brothers Brewing
Black Bear Brewery
Blank Canvas Brewery
Boothbay Craft Brewery, Inc
Bunker Brewing Co
Cushnoc Brewing Company
D.L. Geary Brewing Co Inc.
DeepWater Brewing Company
Definitive Brewing Company
Dirigo Brewing Co.
Drumming Grouse Brewery, LLC
First Mile Brewing Company
Flight Deck Brewing
Fogtown Brewing Company
Fore River Brewing Company
Foulmouthed Brewing
Foundation Brewing Company
Friars' Brewhouse
Funky Bow Brewery & Beer Company
Gary's Olde Towne Tavern
Geaghan Brothers Brewing Co
Geaghan's Pub & Craft Brewery
Gneiss Brewing
Goodfire Brewing Company
Grateful Grain Brewing Company
Gritty McDuffs - Freeport
Gritty McDuffs - Lewiston/Auburn
Gritty McDuffs - Portland
Gruit Brewing
Hidden Cove Brewing Co
Inn On Peaks Island Brewery, The
Island Dog Brewing
Breweries in New York:
12 Gates Brewing Company
16 Stone Brewpub
1940's Brewing Company
2 Way Brewing Company
212 Brewing Company
42 North Brewing Company
6 Degrees of Separation
7 Sins Brewery
8th Ward Brewing Company
Abandon Brewing
Adirondack Pub and Brewery
Adirondack Toboggan Company Microbrewery
Akwesasne Mohawk Casino Resort
Alewife Brewing Company
Alphabet City Brewing Co
Amber Lantern Brewing Company
Andean Brewing
Anheuser-Busch Inc â Baldwinsville
Apex Brewery
Argyle Brewing Company
Arrowood Farms
Artisanal Brew Works
Aurora Ale & Lager
Ausable Brewing Co
B9 Beverages Inc
Bacchus Brewing
Bandwagon Brewery
BarkEater Craft Brewery
Barnshed Brewing
Barrage Brewing Co
Barrier Brewing Co
Battle Hill Brewing Company
Cooperstown Brewing Co
Beer Tree Brew Co
Bellport Brewing Company
Big Alice Brewing Company
Big Ditch Brewing Company
Big Inlet Brewing
Big Slide Brewery
Big Tupper Brewing
Binghamton Brewing Co
Birreria @ Eataly
Black Forest Brew Haus
Blind Bat Brewery LLC, The
Blue Collar Brewery, Inc.
Blue Line Brewery
Blue Point Brewing
Blue Point Brewing Co
Bolton Landing Brewing Co.
Boots Brewing Company, Inc.

Counting breweries in each state:
Number of breweries in Alaska: 50
Number of breweries in Maine: 50
Number of breweries in New York: 50

Counting brewery types in each city:
Brewery types in cities of Alaska:
City: Healy
  micro: 1
City: Anchorage
  brewpub: 6
  micro: 5
  planning: 1
  contract: 1
City: Juneau
  regional: 1
  micro: 2
  brewpub: 1
City: Palmer
  micro: 1
  closed: 1
City: Ketchikan
  micro: 2
  closed: 1
City: Sitka
  closed: 1
  micro: 1
City: Wasilla
  micro: 1
  brewpub: 1
  closed: 1
City: Cooper Landing
  micro: 1
City: Talkeetna
  micro: 1
City: Gakona
  micro: 1
City: Girdwood
  micro: 1
City: Homer
  micro: 2
City: Valdez
  planning: 1
City: Haines
  micro: 1
City: Fairbanks
  micro: 2
City: Hoonah
  micro: 1
City: Kenai
  micro: 1
City: Soldotna
  brewpub: 1
  micro: 1
City: Skagway
  brewpub: 2
City: Kodiak
  micro: 1
City: Eagle River
  brewpub: 1
  micro: 1
City: Nenana
  brewpub: 1
City: Seward
  brewpub: 1
City: Fox
  micro: 1
Brewery types in cities of Maine:
City: Bangor
  brewpub: 3
City: Amherst
  micro: 1
City: Portland
  regional: 1
  micro: 9
  brewpub: 1
City: Lincolnville
  micro: 1
City: Bar Harbor
  micro: 1
  brewpub: 1
City: Carrabassett Valley
  brewpub: 1
City: Biddeford
  micro: 2
City: Saco
  micro: 1
City: Bath
  brewpub: 1
City: Lewiston
  regional: 1
  micro: 1
City: Bridgton
  micro: 2
City: Belfast
  contract: 1
City: Skowhegan
  brewpub: 1
City: Orono
  micro: 1
City: Brewer
  micro: 2
City: Boothbay
  micro: 1
City: Augusta
  brewpub: 1
City: Blue Hill
  micro: 1
City: Fort Kent
  micro: 1
City: Brunswick
  micro: 1
City: Ellsworth
  micro: 1
City: South Portland
  micro: 2
  brewpub: 1
City: Bucksport
  micro: 1
City: Lyman
  micro: 1
City: Naples
  micro: 1
City: Limerick
  micro: 1
City: Monmouth
  micro: 1
City: Freeport
  brewpub: 1
City: Auburn
  brewpub: 1
City: Wells
  micro: 1
City: Peaks Island
  brewpub: 1
Brewery types in cities of New York:
City: Williamsville
  brewpub: 1
City: Holland Patent
  brewpub: 1
City: Holbrook
  micro: 1
City: Beacon
  brewpub: 1
City: Davenport
  contract: 1
City: East Aurora
  brewpub: 1
City: Ossining
  brewpub: 1
City: Ripley
  micro: 1
City: Poughkeepsie
  planning: 1
  brewpub: 1
City: Penn Yan
  micro: 1
City: Lake George
  micro: 1
City: Gouverneur
  micro: 1
City: Akwesasne
  planning: 1
City: Long Island City
  brewpub: 1
  micro: 1
City: New York
  contract: 2
  brewpub: 1
City: Warsaw
  brewpub: 1
City: Blauvelt
  micro: 1
City: Baldwinsville
  large: 1
City: Central Valley
  planning: 1
City: Greenwich
  micro: 1
City: Accord
  micro: 1
City: Saratoga Springs
  micro: 1
City: King Ferry
  micro: 1
City: Keeseville
  micro: 1
City: Dryden
  micro: 1
City: Interlaken
  micro: 1
City: Lowville
  proprietor: 1
City: Hicksville
  micro: 1
City: Farmingdale
  micro: 1
  brewpub: 1
City: Oceanside
  micro: 1
City: Fort Ann
  micro: 1
City: Oneonta
  proprietor: 1
City: Port Crane
  micro: 1
City: Rocky Point
  proprietor: 1
City: Buffalo
  micro: 1
City: Mayville
  planning: 1
City: Lake Placid
  brewpub: 1
City: Tupper Lake
  brewpub: 1
City: Johnson City
  micro: 1
City: Centerport
  micro: 1
City: Saranac Lake
  brewpub: 1
City: Patchogue
  large: 2
City: Bolton Landing
  micro: 1
City: Watertown
  micro: 1

Counting breweries with websites in specific states:
Number of breweries with websites in Alaska: 46
49th State Brewing Co https://www.49statebrewing.com/denali
49th State Brewing Co - Anchorage http://www.49statebrewing.com/
Alaskan Brewing Co. http://www.alaskanbeer.com
Anchorage Brewing Co http://www.anchoragebrewingcompany.com
Arkose Brewery http://www.arkosebrewery.com
Baleen Brewing Co. https://www.baleenbrewing.com
Baranof Island Brewing Co http://www.baranofislandbrewing.com
Barnaby Brewing Company http://www.barnabybrew.com
Bawden Street Brewing Company https://www.facebook.com/bawdenstreetbrewing
Bearpaw River Brewing Co http://bearpawriverbrewing.com
Bleeding Heart Brewery http://facebook.com/bleedingheartbrewery
Broken Tooth Brewing Co https://brokentoothbrewing.net
Cooper Landing Brewing Company http://www.cooperlandingbrewing.com
Cynosure Brewing https://www.cynosure.beer
Denali Brewing Company http://www.denalibrewing.com
Devil's Club Brewing http://www.devilsclubbrewing.com
Forbidden Peak Brewery https://forbiddenpeak.com
Gakona Brewing Company https://www.gakonabrewing.com
Girdwood Brewing Company http://www.girdwoodbrewing.com
Glacier Brewhouse http://www.glacierbrewhouse.com
Grace Ridge Brewing https://www.graceridgebrewing.com
Growler Bay Brewing Co https://growlerbaybrewing.com
Haines Brewing Co http://www.hainesbrewing.com
Harbor Mountain Brewing Co https://www.harbormountainbrewing.com/
Homer Brewing Co http://homerbrew.com
HooDoo Brewing Co http://www.hoodoobrew.com
Humpy's Great Alaskan Alehouse http://www.humpysalaska.com
Icy Strait Brewery http://icystraitbrewing.company
Kenai River Brewing Co http://www.kenairiverbrewing.com
King Street Brewing Co http://www.kingstreetbrewing.com
Klondike Brewing Company http://www.klondikebeer.com
Kodiak Island Brewing Co http://www.kodiakbrewery.com
Last Frontier Brewing Company https://lastfrontierbrew.com
Matanuska Brewing Company - Downtown Brewpub https://matanuskabrewingcompany.com
Matanuska Brewing Company - Eagle River https://matanuskabrewingcompany.com
Matanuska Brewing Company - Midtown Brewpub https://matanuskabrewingcompany.com
Midnight Sun Brewing Co http://www.midnightsunbrewing.com
Odd Man Rush http://www.oddmanrushbrewing.com
Onsite Brewing Company https://onsitebrewing.com
QUAKE! Brewing Company http://www.quakebrewingcompany.com
Resolution Brewing Company http://www.resolutionbeer.com
RoughWoods Inn http://www.roughwoodsinn.biz
Seward Brewing http://www.sewardbrewingcompany.com
Silver Gulch Brewing Co http://www.silvergulch.com
Skagway Brewing Co http://www.skagwaybrewing.com
St Elias Brewing Co http://steliasbrewingco.com
Number of breweries with websites in Maine: 45
2 Feet Brewing Company http://www.2feetbrewing.com
Airline Brewing Company http://www.abcmaine.beer
Allagash Brewing Co http://www.allagash.com
Atlantic Brewing Co http://atlanticbrewing.com
Atlantic Brewing Co / Bar Harbor Brewing http://www.barharborbrewing.com
Austin Street Brewery http://www.austinstreetbrewery.com
Bag and Kettle, The http://www.thebagandkettle.com
Banded Brewing Company http://www.bandedhorn.com
Bangor Beer Co. http://www.bangorbeerco.com
Barreled Souls Brewing Company LLC http://www.barreledsouls.com
Bath Brewing Company http://www.bathbrewing.com
Battery Steele Brewing http://www.batterysteele.com
Baxter Brewing Co, LLC http://www.baxterbrewing.com
Bear Bones Beer http://www.bearbonesbeer.com
Belfast Bay Brewing Co http://www.belfastbaybrewing.com
Bigelow Brewing Company http://www.bigelowbrewing.com
Bissell Brothers Brewing http://www.bissellbrothers.com
Black Bear Brewery http://www.blackbearmicrobrew.com
Blank Canvas Brewery http://www.blankcanvasbrewery.wordpress.com
Boothbay Craft Brewery, Inc http://www.boothbaycraftbrewery.com
Bunker Brewing Co http://www.bunkerbrewingco.com
Cushnoc Brewing Company http://www.cushnocbrewing.com
D.L. Geary Brewing Co Inc. http://www.gearybrewing.com
DeepWater Brewing Company http://www.arborvine.com
Definitive Brewing Company http://www.definitivebrewing.com
Dirigo Brewing Co. http://www.dirigobrewingcompany.com
Drumming Grouse Brewery, LLC http://www.drumminggrousebrewery.com
Flight Deck Brewing http://www.flightdeckbrewing.com
Fogtown Brewing Company http://www.fogtownbrewing.com
Fore River Brewing Company http://www.foreriverbrewing.com
Foulmouthed Brewing http://www.foulmouthedbrewing.com
Foundation Brewing Company http://www.foundationbrew.com
Funky Bow Brewery & Beer Company http://www.funkybowbeercompany.com
Gary's Olde Towne Tavern http://www.garysoldetownetavern.com
Geaghan Brothers Brewing Co http://www.geaghanspub.com
Geaghan's Pub & Craft Brewery http://www.geaghanspub.com
Gneiss Brewing http://www.gneissbeer.com
Goodfire Brewing Company http://www.goodfirebrewing.com
Grateful Grain Brewing Company http://www.gratefulgrainbrewing.com
Gritty McDuffs - Freeport http://www.grittys.com
Gritty McDuffs - Portland http://www.grittys.com
Gruit Brewing http://www.fermentory.com
Hidden Cove Brewing Co http://www.hiddencovebrewingcompany.com
Inn On Peaks Island Brewery, The http://www.innonpeaks.com
Island Dog Brewing http://www.islanddogbrewing.com
Number of breweries with websites in New York: 43
12 Gates Brewing Company http://www.12gatesbrewing.com
16 Stone Brewpub http://www.16stonebrewpub.com
1940's Brewing Company http://www.1940sbrewingcompany.com
2 Way Brewing Company http://www.2waybrewingcompany.com
42 North Brewing Company http://www.42northbrewing.com
6 Degrees of Separation http://www.6degreesbp.com
7 Sins Brewery http://www.7sinsbrewery.com
Abandon Brewing http://www.abandonbrewing.com
Adirondack Pub and Brewery http://www.adkpub.com
Adirondack Toboggan Company Microbrewery http://www.adktoboggan.net
Akwesasne Mohawk Casino Resort http://mohawkcasino.com
Alewife Brewing Company http://www.alewife.beer
Alphabet City Brewing Co http://www.acbnyc.com
Amber Lantern Brewing Company http://www.amberlanternbrewingcompany.com
Apex Brewery http://www.apexbeer.co
Argyle Brewing Company http://www.argylebrewing.com
Arrowood Farms http://www.arrowoodfarms.com
Artisanal Brew Works http://www.artisanalbrewworks.com
Aurora Ale & Lager http://www.brewaurora.com
Ausable Brewing Co http://ausablebrewing.tumblr.com
Bacchus Brewing http://www.bacchusbrewing.com
Bandwagon Brewery http://www.bandwagonbeer.com
BarkEater Craft Brewery http://www.barkeaterbrew.com
Barnshed Brewing http://www.barnshedbrewing.com
Barrage Brewing Co http://www.barragebrewing.com
Barrier Brewing Co http://www.barrierbrewing.com
Battle Hill Brewing Company http://www.battlehillbrewing.com
Beer Tree Brew Co http://www.beertreebrew.com
Bellport Brewing Company http://www.bellportbrewing.com
Big Alice Brewing Company http://www.bigalicebrewing.com
Big Ditch Brewing Company http://www.bigditchbrewing.com
Big Inlet Brewing http://www.biginletbrewing.com
Big Slide Brewery http://www.bigslidebrewery.com
Big Tupper Brewing http://www.bigtupperbrewing.com
Binghamton Brewing Co http://www.bingbrew.com
Birreria @ Eataly http://www.eatalyny.com
Black Forest Brew Haus http://www.blackforestbrewhaus.com
Blind Bat Brewery LLC, The http://www.BlindBatBrewery.com
Blue Collar Brewery, Inc. http://www.thebluecollarbrewery.com
Blue Line Brewery http://www.bluelinebrew.com
Blue Point Brewing Co http://www.bluepointbrewing.com
Bolton Landing Brewing Co. http://www.boltonlandingbrewing.com
Boots Brewing Company, Inc. http://www.bootsbrew.com

Process finished with exit code 0

"""