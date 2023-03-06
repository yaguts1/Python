# import pickle

# # From now on I am just reading the objects that I've created
# infile = open('menu_items.pkl','rb')
# my_unpickled_index_list_for_menus = pickle.load(infile) 
# infile.close()
# print(f'This is my unpickled object:\n{my_unpickled_index_list_for_menus[0][0].restaurant.distance}\n')
from os import system
system("OOP_web_scraper\menu.py 1")