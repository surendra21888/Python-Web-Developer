import requests,csv,json 
# extract data from source - rest api/cloud apis/database
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
products=product_data['products']

#load into beauty.csv and beauty.json

fp1 = open('beauty.csv','w',newline="")
csvwriter=csv.writer(fp1)
csvwriter.writerow(['PID','Name','Price','Category'])

for product in products:
    csvwriter.writerow([product['id'],product['title'],product['price'],product['category']])

print('New CSV File created successfully')

fp1.close()