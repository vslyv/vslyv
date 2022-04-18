'''
Author: Vincent Sylvester
Date: Mar 15, 2022
Board Class


'''


from numpy import random as r
import networkx as nx
import numpy as np
import math
class Board():
    __edgeList = [(1,2),(1,3),(1,26),(2,3),(2,4),(2,7),(3,4),(3,6),(4,5),(4,6),(4,7),(4,8),(5,6),(5,8),(6,38),(7,8),(7,9),(8,9),
       (9,10),(10,11),(10,13),(11,12),(11,13),(12,13),(13,14),(14,34),(14,33),(14,19),(14,18),(14,15),(15,18),(15,16),(16,17),
       (16,18),(17,18),(18,19),(18,20),(19,33),(19,20),(20,33),(20,32),(20,31),(20,21),(21,31),(21,22),(21,23),(22,23),(22,39),
        (39,40),(39,42),(40,41),(41,42),(40,42),(23,31),(23,29),(23,24),(24,25),(24,27),(24,26),(24,29),(25,26),(26,27),(26,28),
        (27,29),(27,28),(28,29),(29,30),(30,31),(30,32),(31,32),(32,33),(32,36),(32,37),(33,34),(33,36),(34,35),(34,36),
        (35,38),(35,37),(35,36),(36,37),(37,38)]

    def __init__(self, numPlay):
        "set up initial board configuration"
        self.elist = [(1,2),(1,3),(1,26),(2,3),(2,4),(2,7),(3,4),(3,6),(4,5),(4,6),(4,7),(4,8),(5,6),(5,8),(6,38),(7,8),(7,9),(8,9),
       (9,10),(10,11),(10,13),(11,12),(11,13),(12,13),(13,14),(14,34),(14,33),(14,19),(14,18),(14,15),(15,18),(15,16),(16,17),
       (16,18),(17,18),(18,19),(18,20),(19,33),(19,20),(20,33),(20,32),(20,31),(20,21),(21,31),(21,22),(21,23),(22,23),(22,39),
        (39,40),(39,42),(40,41),(41,42),(40,42),(23,31),(23,29),(23,24),(24,25),(24,27),(24,26),(24,29),(25,26),(26,27),(26,28),
        (27,29),(27,28),(28,29),(29,30),(30,31),(30,32),(31,32),(32,33),(32,36),(32,37),(33,34),(33,36),(34,35),(34,36),
        (35,38),(35,37),(35,36),(36,37),(37,38)]
        self.numPlay = numPlay

        self.countries = {1: 'Alaska', 2: 'Alberta',3:'Northwest Territory',4:'Ontario',5:'Quebec',6:'Greenland',\
              7:'Western US',8: 'Eastern US', 9:'Central America', 10:'Venezuela',11:'Peru',12:'Argentina',13:'Uruguay',14:'North Africa',\
             15: 'Congo', 16:'South Africa',17:'Madagascar', 18: 'East Africa', 19:'Egypt',20:'Levant', 21: 'India', 22:'Southeast Asia',\
              23: 'China',24:'Mongolia', 25:'Japan', 26: 'Kamchatka', 27: 'Irktusk', 28: 'Yakursk',29:'Siberia',30:'Ural',31:'Afghanistan',32:'Ukraine',\
             33: 'Southern Europe', 34:'Western Europe',35:'Great Britain',36:'Northern Europe',37:'Scandinavia',38:'Iceland',\
             39: 'Indonesia',40:'Western Australia', 41:'Eastern Australia',42:'New Guinea'
        }

        self.G = nx.Graph()
        self.rng = r.default_rng()

        self.G.add_edges_from(self.elist)
        nx.set_node_attributes(self.G, self.countries, 'Country')


        
        ### randomly order countries
        country_nums = list(range(1,43))
        r.shuffle(country_nums)

        # assign each country to one of the players, possibly extras
        country_assignment = list(range(1,numPlay + 1)) * math.ceil(42/numPlay)
        country_assignment = country_assignment[:42]

        self.country_dict = dict(zip(country_nums, country_assignment))
        
        
        nx.set_node_attributes(self.G, self.country_dict, 'ownership')


        ### will be dictionary with 
        self.player_holdings = {}
        for country, player in self.country_dict.items():
            self.player_holdings.setdefault(player,[]).append(country)
        #### randomly assign units to countries
        match self.numPlay:
            case 2:
                totTroops = 40
                
            case 3:
                totTroops = 35
            case 4:
                totTroops = 30
            case 5:
                totTroops = 25

            case 6:
                totTroops = 20

        ###Assign troops to countries in dictionary as uniformly as possible    
        troopDict = {}
        for i in self.player_holdings:
            numHoldings = len(self.player_holdings[i])
            n = totTroops // numHoldings
            extra = totTroops % numHoldings
            counter = 0
            
            for j in range(numHoldings):
                country = self.player_holdings[i][j]
        
                if counter < extra:
                    troopDict[country] = n + 1
                    counter += 1
                else:
                    troopDict[country] = n

        # take dictionary and set it to the nx graph
        nx.set_node_attributes(self.G, troopDict, 'troops')

    def __getitem__(self, index):
        return self.G[index]

        
         
                
