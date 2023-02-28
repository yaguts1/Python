from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pickle
from restaurant import Restaurant
from os import system

DRIVER_PATH = 'C:/Users/dell/Downloads/chromedriver_win32/chromedriver.exe'
options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# Import the constructor from restaurant.py

# To create an object I need the info to pass as arguments to the constructor.
#Let's get some of this info.
restaurant_names = []
distances = []
reviews = []
links = []
delivery_expected_times = []
delivery_fees = []
food_categories = []
# Creating a counter to help iterate through the cards's divs that contais the data on the website
cnt = 1

# Now that I have some lists to store the data let's get the data by scraping.
driver.get("https://www.ifood.com.br/inicio")
sleep(5)

# Click the button to access my current location 
driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/button').click()
sleep(10)

# Add a way of expanding the restaurant options by clicking the more button
break_ = False
times_pressed_button = 0
#######################################################################
#######################################################################
#######################################################################
MAXIMUM = 0
#######################################################################
#######################################################################
#######################################################################
while break_ == False and times_pressed_button < MAXIMUM:
    try:
        print("I am trying to locate the button to check if it is clickable...")
        driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/main/div/div[2]/section/article[2]/section[2]/div/button').click()
        print("It is clickable...")
        times_pressed_button += 1
        sleep(10)    
    except:
        break_ = True

# Iterate through every card that hava a different restaurant info
for i in driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/main/div/div[2]/section/article[2]/section[1]/div/div[2]/div[*]'): 
    name = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/main/div/div[2]/section/article[2]/section[1]/div/div[2]/div['+ str(cnt) +']/a/div/div[2]/h3/div[1]/span').text
    dirty_res_data = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/main/div/div[2]/section/article[2]/section[1]/div/div[2]/div['+ str(cnt) +']/a/div/div[2]/h3/div[2]').text
    dirty_delivery_data = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/main/div/div[2]/section/article[2]/section[1]/div/div[2]/div['+ str(cnt) +']/a/div/div[2]/div').text
    link = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/main/div/div[2]/section/article[2]/section[1]/div/div[2]/div['+ str(cnt) +']/a').get_attribute('href')
    time = dirty_delivery_data.split('\n')[0]
    delivery_fee = dirty_delivery_data.split('\n')[2]
    review = dirty_res_data.split('\n')[0]
    category = dirty_res_data.split('\n')[2]
    try:
        distance = dirty_res_data.split('\n')[4]
    except:
        break
    restaurant_names.append(name.encode('UTF-8'))
    food_categories.append(category)
    reviews.append(review)
    distances.append(distance)
    delivery_expected_times.append(time)
    delivery_fees.append(delivery_fee)
    links.append(link)
    cnt += 1 

# Create the objects using the constructor
restaurant_object_list = []
for i in range(len(restaurant_names)):
    restaurant_object_list.append(Restaurant(restaurant_names[i],distances[i],reviews[i],links[i],delivery_expected_times[i],delivery_fees[i],food_categories[i]))
    # restaurant_object_list[i].display()
    print(i)
#Need to learn how to use pickle to save this objects. Also see if I am able to save a list of the objects. 
# It is possible
outfile = open('data/restaurants.pkl','wb')
my_pickled_restaurant_object_list = pickle.dump(restaurant_object_list,outfile) # Pickling the object
print(f'This is my pickled object:\n{my_pickled_restaurant_object_list}\n')
outfile.close()

infile = open('data/restaurants.pkl','rb')
my_unpickled_restaurant_object_list = pickle.load(infile)
infile.close()

# print(f'This is my unpickled object:\n{my_unpickled_restaurant_object_list[0].name.decode("UTF-8")}\n')

system("menu.py 1")
sleep(2)
system("dataframes.py 1")

