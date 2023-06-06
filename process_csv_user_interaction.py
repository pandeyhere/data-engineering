import pandas as pd
import sys
path_to_data = sys.argv[1]
output_path_to_data=sys.argv[2]
# read the csv data using pd.read_csv function
data = pd.read_csv(path_to_data)
df=pd.DataFrame(data)
#Total Interactions
interations=df[df.columns[0]].count()
#Total Unique Users
unique_users=df['user_id'].nunique()
#Most Visited URL
most_visited_url=df['url'].value_counts().idxmax()
# print(df['url'].value_counts()[df['url'].value_counts() == df['url'].value_counts().max()])
#Average Time Spent on Each URL
avg_time_spent_on_each_url=df['page_view_duration'].aggregate('sum')/df['user_id'].nunique()

dict = {'Total Interactions': [interations], 'Total Unique Users': [unique_users], 'Most Visited URL': [most_visited_url], 'Average Time Spent on Each URL': [avg_time_spent_on_each_url]}
df = pd.DataFrame(dict)
print(df)
df.to_csv(output_path_to_data,index=False,sep=',')