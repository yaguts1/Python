import pickle
import pandas
import numpy as np
dfs = []
for i in range(1,6):
    infile = open('C:/Users/dell/Documents/GitHub/Python/OOP_web_scraper/test/Dados_coletados_ifood/' +str(i)+'/df.pkl','rb')
    unpickled= pickle.load(infile)
    infile.close()
    dfs.append(unpickled)

df = pandas.concat([dfs[0],dfs[1],dfs[2],dfs[3],dfs[4]]).drop_duplicates().reset_index(drop=True)
# print(df["Restaurante"].nunique())
# print(df.info())
price_list = list(df["Preço"])
delivery_list =(df["Frete"])
for price_index in range(len(price_list)):
    price_list[price_index] = price_list[price_index].replace(",",".")
    delivery_list[price_index] = delivery_list[price_index].replace("R$ ","")
    delivery_list[price_index] = delivery_list[price_index].replace("Grátis","0")
    delivery_list[price_index] = delivery_list[price_index].replace(",",".")
    delivery_list[price_index] = float(delivery_list[price_index])
df2 = df.copy()
df2["Preço"] = price_list
df2["Frete"] = delivery_list
print(df2.info())
# Code to save the df as a pickle file
outfile = open('OOP_web_scraper\data\df_final_decimal.pkl','wb')
pickle.dump(df2,outfile) # Pickling the object
outfile.close()
df2.to_csv('OOP_web_scraper/data/Ifood_data_final_decimal.csv',encoding='utf-8-sig')

# # Code to save the df as a pickle file
# outfile = open('OOP_web_scraper\data\df_final.pkl','wb')
# pickle.dump(df,outfile) # Pickling the object
# outfile.close()
# df.to_csv('OOP_web_scraper/data/Ifood_data_final.csv',encoding='utf-8-sig')