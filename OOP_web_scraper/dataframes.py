import pandas as pd
import pickle
item_name = []
item_price = []
item_description = []
restaurant_name = []
restaurant_link = []
restaurant_delivery_time = []
restaurant_delivery_fee = []
restaurant_distance = []
restaurant_review = []
restaurant_food_category = []
cnt = 0
data = []
# From now on I am just reading the objects that I've created
infile = open('data/menu_items.pkl','rb')
my_unpickled_index_list_for_menus = pickle.load(infile) 
infile.close()
for i in range(len(my_unpickled_index_list_for_menus)):
    for j in range(len(my_unpickled_index_list_for_menus[i])):
        item_name.append(my_unpickled_index_list_for_menus[i][j].item_name.decode())
        item_price.append(my_unpickled_index_list_for_menus[i][j].item_price)
        item_description.append(my_unpickled_index_list_for_menus[i][j].item_description)
        restaurant_name.append(my_unpickled_index_list_for_menus[i][j].restaurant.name.decode())
        restaurant_link.append(my_unpickled_index_list_for_menus[i][j].restaurant.link)
        restaurant_delivery_time.append(my_unpickled_index_list_for_menus[i][j].restaurant.delivery_time)
        restaurant_delivery_fee.append(my_unpickled_index_list_for_menus[i][j].restaurant.delivery_fee)
        restaurant_distance.append(my_unpickled_index_list_for_menus[i][j].restaurant.distance)
        restaurant_review.append(my_unpickled_index_list_for_menus[i][j].restaurant.review)
        restaurant_food_category.append(my_unpickled_index_list_for_menus[i][j].restaurant.food_category)
    
# Creating the dataframe based on the pickled objects
        data.append([
            item_name[cnt],
            item_price[cnt],
            item_description[cnt],
            restaurant_name[cnt],
            restaurant_link[cnt],
            restaurant_delivery_time[cnt],
            restaurant_delivery_fee[cnt],
            restaurant_distance[cnt],
            restaurant_review[cnt],
            restaurant_food_category[cnt]
        ])
        cnt += 1
# Making a dataframe and then saving it as a csv file
df = pd.DataFrame(data, columns=('Nome', 'Preço', 'Descrição', 'Restaurante','link','Tempo Entrega','Frete','Distância','Reviews','Categoria'))
df.to_csv('data/out.csv',encoding='utf-8-sig')

# Code to save the df as a pickle file
outfile = open('data/df.pkl','wb')
my_pickled_restaurant_object_list = pickle.dump(df,outfile) # Pickling the object
print(f'This is my pickled object:\n{my_pickled_restaurant_object_list}\n')
outfile.close()

# Code to unpickle and read the df 

# infile = open('data/df.pkl','rb')
# unpickled= pickle.load(infile)
# infile.close()
# print(unpickled)