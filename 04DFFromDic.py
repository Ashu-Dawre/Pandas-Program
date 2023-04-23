import pandas

dic={
    'filmnm':['sholay','pk','swades'],
    'relyear':[1975,2014,2004],
    'actor':['amitabh bachchan','amir khan','shah rukh khan'],
    'music':['r d burman','shantanu moitra','a r rahman']
}

df=pandas.DataFrame.from_dict(dic)
print(df)