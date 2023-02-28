from selenium import webdriver # The webdriver is used to create objects to comunnicate properly with the browser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pickle
from restaurant import Restaurant
from menu_item import Item_menu


DRIVER_PATH = 'C:/Users/dell/Downloads/chromedriver_win32/chromedriver.exe'
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
links = []
index_list_for_menus = []
restaurant_number = 0
# Open the pickled object array and read the links for each menu
infile = open('data/restaurants.pkl','rb')
my_unpickled_restaurant_object_list = pickle.load(infile)
for i in (my_unpickled_restaurant_object_list):
        links.append(i.link)

def scrape_menu(link, restaurant_number):
    # Declaring some lists to store the significant items' values
    items_name = []
    items_price = []
    items_description = []
    cnt2 = 1
    cnt3 = 1 
    driver.get(link) 
    sleep(5)
    for j in driver.find_elements(By.XPATH,' /html/body/div[2]/div[1]/main/div[1]/div/div[2]/div[1]/div[*]'):

        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/main/div[1]/div/div[2]/div[1]/div['+ str(cnt2) +']/ul/li/div/a/div[1]/div/h3').text
            cnt3 = 1
            for k in driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/main/div[1]/div/div[2]/div[1]/div['+ str(cnt2) +']/ul/li/div/a/div[*]'):
                item_name =driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/main/div[1]/div/div[2]/div[1]/div['+ str(cnt2) +']/ul/li['+ str(cnt3)+']/div/a/div[1]/div/h3').text
                item_price =driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/main/div[1]/div/div[2]/div[1]/div['+ str(cnt2) +']/ul/li['+ str(cnt3)+']/div/a/div[1]/span').text.split('R$ ')[1]
                item_description =driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/main/div[1]/div/div[2]/div[1]/div['+ str(cnt2) +']/ul/li['+ str(cnt3)+']/div/a/div[1]/div/span').text

                # Populating the lists
                items_name.append(item_name.encode())
                items_price.append(item_price)
                items_description.append(item_description)
                cnt3 += 1

        except:
            cnt2 += 1
            continue
    
    items_menu_object_list = []
    for i in range(len(items_name)):
        items_menu_object_list.append(Item_menu(items_name[i],items_price[i],items_description[i],my_unpickled_restaurant_object=my_unpickled_restaurant_object_list[restaurant_number]))
    
    index_list_for_menus.append(items_menu_object_list)
    
    outfile = open('data/menu_items.pkl','wb')
    my_pickled_index_list_for_menus = pickle.dump(index_list_for_menus,outfile) # Pickling the object
    outfile.close()

    
for link in links:
    scrape_menu(link,restaurant_number)
    restaurant_number +=1
    sleep(5)
driver.quit()
infile.close()
exit()