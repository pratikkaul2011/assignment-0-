#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''Note: 

* Before writing any code remember that this assigment is for helping you understand the basics of file
handling in csv file. 

* This project is designed to have a work flow such that everyone is in same page for this purpose the variables are
given a strict name which should not be changed or modified according to your convinience

* Few of new functions like .head() .xticks().... and concepts may have been introduced in the assingment, so we encourage you
all to go through them without skipping.

*  functions which are to be used in the Your code sections are globally available so try to look for those where you have been prompted
'''

'''Its the data of a meal delivery company which operates in multiple cities. 
They have various fulfillment centers in these cities for dispatching meal orders to their customers.
train.csv: Historical data of demand for a product-center combination 
fulfilment_center_info.csv: Information for fulfillment center like center area, city information etc.
meal_info.csv: Product(Meal) features such as category, sub-category, current price and discount'''


'''START CODE'''

#Import necessary libraries: Numpy,pandas,matplotlib

'''************************Your code here**********************'''
'''************************************************************'''
import numpy as nd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#read meal_info.csv file from provided dataset into a df_meal named variable
#Note: Proper file directory should be provided

'''************************Your code here**********************'''

'''************************************************************'''
df_meal=pd.read_csv("C:\Users\Miskeen's\Desktop\meal_info.csv")

df_meal.head()'''This is for displaying first five data points'''

#read fulfilment_center_info.csv file from provided dataset
#Note: Proper file directory should be provided

'''************************Your code here**********************'''

'''************************************************************'''
df_center=pd.read_csv("C:\Users\Miskeen's\Desktop\fulfilment_center_info.csv")
df_center.head()'''This is for displaying first five data points'''

#read train.csv file from provided dataset
#Note: Proper file directory should be provided

'''************************Your code here**********************'''

'''************************************************************'''
df_food=pd.read_csv("C:\Users\Miskeen's\Desktop\train.csv")
df_food.head(5)

'''Since the provided information is in different files, your work here is to merge them.Look for the functions
in pandas library to do so'''

'''************************Your code here**********************'''
df=pd.merge(df_center,df_food,how='outer',on='center_id')
df=pd.merge(df,df_meal,how='outer',on='meal_id')

'''************************************************************'''

'''Here we have used pd.pivot_table() kindly go through the function and mention in comment what it does'''

table = pd.pivot_table(data=df,index='category',values='num_orders',aggfunc=np.sum)



'''Graph tweaking
************************
Plot a bar graph with title 'Most popular food' for category(x-axis) vs number-of-orders(y-axis)

give x label 'Food items'
give y label 'Quantity sold'


'''

'''************Yourcode*********************'''

#bar graph
graph=plt.figure()

#xticks 
plt.xticks(rotation=70) '''Write on comment what you feel this function does'''

#x-axis labels 

plt.xlabel('food items')
#y-axis labels 
plt.xlabel('quantity sold')

#plot title 

plt.title('most popular food')
#save plot 


#display 
plt.show()

'''************************************************'''


'''Comparison of weekly and monthly sales
 Create a new column
* named 'revenue' where each element is product of checkout_price and num_orders 
** named 'month' by using ['week'] column (week column value divided by 4 gives month value)'''



'''**************************Your code******************************'''



'''******************************************************************'''
'''Here we have created two list month and month_order ,
store month number in month list and revenue of each month in month_order'''
#list to store month-wise revenue 
month=[] 
month_order=[] 

'''***********************************Your code***********************'''

    
'''*********************************************************************'''
'''Here we have created two list week and week_order ,you need to store in them mapping the monthly orders'''    
#list to store week-wise revenue 
week=[] 
week_order=[] 

'''***********************************Your code***********************'''


'''*********************************************************************'''
''' Plot two subplots in the same space : one for weekly revenue and other for monthly revenue.
For weekly : Title(Weekly income),x_label(week),y_label(revenue); similarly for monthly revenue.
'''

'''************Yourcode*********************'''



''' Display the plot'''


# In[2]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# In[7]:


df_meal=pd.read_csv('C:\data\meal_info.csv')

df_meal[:9]


# In[12]:


df_center=pd.read_csv(r'C:\data\fulfilment_center_info.csv')

df_center.head(5)


# In[11]:


df_food=pd.read_csv(r'C:\data\train.csv')
df_food.head(9)


# In[13]:


df=pd.merge(df_center,df_food,how='outer',on='center_id')
df=pd.merge(df,df_meal,how='outer',on='meal_id')

df


# In[15]:


table = pd.pivot_table(data=df,index='category',values='num_orders',aggfunc=sum)


# In[16]:


table.plot(kind='bar')
plt.xtics(rotation=70)
plt.xlabel('food items')
plt.ylabel('quantity sold')
plt.title('faviourate food')
plt.savefig('most_popular_food.png')
plt.show()


# In[73]:


df['revenue']=df['checkout_price']*df['num_orders']
df['month']=df['week']//4
df


# In[77]:


week=[]
week.append(df['week'])

df['week_order']=(df['revenue'])


# In[78]:


month=[]
month.append(df['month'])
df['month_order']=df['revenue']
df


# In[79]:


pv = pd.pivot_table(df, index='week',values='revenue',aggfunc='sum')
pa = pd.pivot_table(data=df, index='month', values='month_order', aggfunc='sum')
pv.plot()
pa.plot()


# In[ ]:





# In[ ]:





# In[ ]:




