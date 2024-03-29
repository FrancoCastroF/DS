# -*- coding: utf-8 -*-
"""Assignment+2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XOXR6OiFdFbtvJERSCqqQb1I_MhDQGXJ

---

_You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._

---

# Assignment 2 - Pandas Introduction
All questions are weighted the same in this assignment.
## Part 1
The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry on [All Time Olympic Games Medals](https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table), and does some basic data cleaning. 

The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals, total # number of games, total # of medals. Use this dataset to answer the questions below.
"""

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # dividir indice por '('

df.index = names_ids.str[0] # el elemento en la posicion [0] es el nombre del pais (idex nuevo) 
df['ID'] = names_ids.str[1].str[:3] # el elemento [1] es el ID (toma los primeros 3 caracteres para ello)

df = df.drop('Totals')
df.head()

"""### Question 0 (Example)

What is the first country in df?

*This function should return a Series.*
"""

# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero()

"""### Question 1
Which country has won the most gold medals in summer games?

*This function should return a single string value.*
"""

df.head()

def answer_one():
  r1=df.loc[:,'Gold'].sort_values( ascending=False)
  r1=r1.reset_index()
  return r1.iloc[0][0]

type(answer_one())
answer_one()

"""### Question 2
Which country had the biggest difference between their summer and winter gold medal counts?

*This function should return a single string value.*
"""

def answer_two():
  dif=df['Gold']-df['Gold.1']
  dif=dif.sort_values(ascending=False).to_frame()
  dif=dif.reset_index()
  return dif.iloc[0,0]

type(answer_two())

"""### Question 3
Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count? 

$$\frac{Summer~Gold - Winter~Gold}{Total~Gold}$$

Only include countries that have won at least 1 gold in both summer and winter.

*This function should return a single string value.*
"""

def answer_three():
  # x=df[(df['Gold']>0)&(df['Gold.1']>0)]
  # x=x.dropna()
  # Gres=(x['Gold']-x['Gold.1']).abs()
  # Gsum=x['Gold.2']
  # div=Gres/Gsum
  # div=div.sort_values(ascending=False).to_frame()
  # div=div.reset_index()
  
  df['Gold'].sort_values(ascending=False)
  x=df.where((df['Gold']>0)&(df['Gold.1']>0)&(df['Gold.2']>1))
  x=x.dropna()
  Gsum= (x['Gold']+x['Gold.1']+x['Gold.2']).abs()
  Gres=(x['Gold']-x['Gold.1']).abs()
  div=Gres/Gsum
  div=div.sort_values(ascending=False).to_frame()
  div=div.reset_index()

  return div.iloc[0,0]

answer_three()

"""### Question 4
Write a function that creates a Series called "Points" which is a weighted value where each gold medal (`Gold.2`) counts for 3 points, silver medals (`Silver.2`) for 2 points, and bronze medals (`Bronze.2`) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.

*This function should return a Series named `Points` of length 146*
"""

def answer_four():
  df.loc[:,'Gold.2':'Bronze.2']
  g=df['Gold.2'].where(df['Gold.2'].lt(1),df['Gold.2']*3,axis=0)
  s=df['Silver.2'].where(df['Silver.2'].lt(1),df['Silver.2']*2,axis=0)
  b=df['Bronze.2'].where(df['Bronze.2'].lt(1),df['Bronze.2']*1,axis=0)
  Tsum=(g+s+b)
  return Tsum

answer_four()

"""## Part 2
For the next set of questions, we will be using census data from the [United States Census Bureau](http://www.census.gov). Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. [See this document](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2015/co-est2015-alldata.pdf) for a description of the variable names.

The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.

### Question 5
Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)

*This function should return a single string value.*
"""

import pandas as pd

census_df = pd.read_csv('census.csv')
census_df

def answer_five():
  MS=census_df.groupby(['STNAME'])[['STATE']].sum().sort_values(by='STATE')
  MS=MS.reset_index()

  return MS.iloc[-1,0]

answer_five()

"""### Question 6
**Only looking at the three most populous counties for each state**, what are the three most populous states (in order of highest population to lowest population)? Use `CENSUS2010POP`.

*This function should return a list of string values.*
"""

def answer_six():
  df1 = pd.DataFrame(census_df.where(census_df['SUMLEV'] == 50).groupby(['STNAME'])['CENSUS2010POP'].nlargest(3))
  df1 = df1.reset_index()
  return list(df1.groupby(['STNAME']).sum()['CENSUS2010POP'].nlargest(3).index)

 nd= census_df[census_df.SUMLEV==50]
  # MP=nd.groupby(['CTYNAME'])[['CENSUS2010POP']].sum().sort_values(by='CENSUS2010POP',ascending=False)
  # nv=MP.iloc[0:3]
  # nv=nv.reset_index()
  
  #return nv

answer_six()

"""### Question 7
Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)

e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.

*This function should return a single string value.*
"""

def answer_seven():
    # d = census_df[census_df.SUMLEV==50].copy()
    # d['max'] = d[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)
    # d['min'] = d[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)
    # d['diff'] = d['max'] - d['min']
    # return d[d['diff'] == d['diff'].max()].iloc[0]['CTYNAME']

  nv= census_df[census_df.SUMLEV==50].copy()
  maxi=nv[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)
  mini=nv[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)
  tot=(maxi-mini).to_frame('ABSchange')
  #tot['ABSchange']=tot['ABSchange'].abs()
  tot.index=nv['CTYNAME']
  tot=tot.sort_values(by='ABSchange', ascending=False)
  tot=tot.reset_index()
  return tot.iloc[0][0]

answer_seven()

"""### Question 8
In this datafile, the United States is broken up into four regions using the "REGION" column. 

Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.

*This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).*
"""

def answer_eight():
  filtro=census_df[((census_df.REGION==1)|(census_df.REGION==2))&(census_df.POPESTIMATE2015 > census_df.POPESTIMATE2014)&(census_df.CTYNAME.str.contains('Washington'))]
  filtro=filtro.loc[:,'STNAME':'CTYNAME'].sort_index()
  return filtro

answer_eight()

