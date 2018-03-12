import pandas as pd
def my_max_min(tag_name, df):
    m_df = df[df['Tag Code'] ==tag_name]
    return m_df['RSSI'].max(),m_df['RSSI'].min()
def moving_list(df):
    df_filtered_1 = df.loc[df['Mux'] == 1]
    df_filtered_2 = df.loc[df['Mux'] == 2]
    df_filtered_3 = df.loc[df['Mux'] == 3]
    df_filtered_4 = df.loc[df['Mux'] == 4]

    m_list = []
    count =0
    for row in df.itertuples():
        max_1,min_1 = my_max_min(row[1],df_filtered_1)
        max_2, min_2 = my_max_min(row[1], df_filtered_2)
        max_3, min_3 = my_max_min(row[1], df_filtered_3)
        max_4, min_4 = my_max_min(row[1], df_filtered_4)
        if ((max_1-min_1 >=4 or max_4-min_4 >=4 )or (max_2-min_2 >=2 or max_3 -min_3 >=2)):
            m_list.insert(count,row[1])
            count = count +1
    return sorted(list(set(m_list)))

df = pd.read_csv('data_9th_Run.csv')
df = df[['Tag Code','Reader','Mux','RSSI','Time']]


#filter by antenna 1, 2, 3,4
#check for which one has +-4, at least 2 flags must up
#that one is the moving item





my_list=moving_list(df)
for item in my_list:
    print(item +'\n')
