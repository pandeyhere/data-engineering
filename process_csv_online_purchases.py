
import pandas as pd
import numpy as np
import sys
path_to_data = sys.argv[1]
output_path_to_data=sys.argv[2]

data = pd.read_csv(path_to_data)
df=pd.DataFrame(data)

df['timestamp']=pd.to_datetime(df["timestamp"])
df['Date']=df['timestamp'].dt.date
df['sales']=df['product_price']*df['quantity']
grp=df.groupby(['customer_id','Date'])
grp['sales'].aggregate([np.sum])


dict = {'date': df['Date'], 'customer_id': df['customer_id'], 'total_spent': df['sales']}
df = pd.DataFrame(dict)
print(df)
df.to_csv(output_path_to_data,index=False,sep=',')