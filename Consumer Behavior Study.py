#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:49:07 2019

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math



sheetsname = pd.read_excel('/Users/suisland/Downloads/DE-final/Personal Financial Example.xlsx', None)
sheetsname.keys()

#merge data; add Customerid column
m = 1
df=[]
for i in sheetsname:
    sheetsname[i]['Customerid'] = m
    m += 1
    df.append(sheetsname[i])
df = pd.concat(df)

df.head(10)

#delete cloumns that we donot need
df.drop(df.columns[6:], axis=1, inplace=True)

#Split CTR to State, MachineNum and Classification
df[['State_MachineNum','Classification']] = df.CTR.str.split('_',expand=True)
df.head()

df['State']= df['State_MachineNum'].str[:2]
df['MachineNum'] = df['State_MachineNum'].str[2:]
df.head()

#switch DA to negative number, when Oper =7
df.loc[ (df.Oper == 7), 'DA' ] *= -1 
df.loc[ (df.Customerid == 14) & (df.Oper == 1) , 'DA' ] *= -1 
df.loc[ (df.Customerid == 14) & (df.Oper == 3) , 'DA' ] *= -1 
df.loc[ (df.Customerid == 14) & (df.Oper == 5) , 'DA' ] *= -1 

#df.to_excel('Personal Financial Example_v11.xls')

df_daneg = df.loc[df.DA<0]
sumDA_Neg = df_daneg.groupby('Customerid')['DA'].sum()
sumDA_Neg
df_dapos = df.loc[df.DA>0]
sumDA_Pos = df_dapos.groupby('Customerid')['DA'].sum()
sumDA_Pos
df_percentage = abs(sumDA_Neg) / sumDA_Pos
df_percentage


DA=df['DA']
countpositiveDA=df[DA>0].groupby(['Customerid'])['DA'].count()
countpositiveDA
countnegativeDA=df[DA<0].groupby(['Customerid'])['DA'].count()
countnegativeDA

#df.to_excel('C://Users//canli//OneDrive//Desktop//Personal Financial Example_T.xls')

Classification =df['Classification']
df.head()
sumsuperDA=df[Classification=='Superfluous'].groupby(['Customerid'])['DA'].sum()
sumsuperDA
suminvestDA=df[Classification=='Investment'].groupby(['Customerid'])['DA'].sum()
suminvestDA
sumEssenDA=df[Classification=='Essencials'].groupby(['Customerid'])['DA'].sum()
sumEssenDA

Oper=df['Oper']
countOper1=df[Oper==1].groupby('Customerid')['Oper'].count()
countOper1
countOper2=df[Oper==2].groupby('Customerid')['Oper'].count()
countOper2
countOper3=df[Oper==3].groupby('Customerid')['Oper'].count()
countOper3
countOper4=df[Oper==4].groupby('Customerid')['Oper'].count()
countOper4
countOper5=df[Oper==5].groupby('Customerid')['Oper'].count()
countOper5
countOper6=df[Oper==6].groupby('Customerid')['Oper'].count()
countOper6
countOper7=df[Oper==7].groupby('Customerid')['Oper'].count()
countOper7
countOper8=df[Oper==8].groupby('Customerid')['Oper'].count()
countOper8


countsuper=df[Classification=='Superfluous'].groupby(['Customerid'])['Classification'].count()
countsuper
countinvest=df[Classification=='Investment'].groupby(['Customerid'])['Classification'].count()
countinvest
countessen=df[Classification=='Essencials'].groupby(['Customerid'])['Classification'].count()
countessen

df2=pd.concat([countsuper,countinvest,countessen,countpositiveDA,countnegativeDA, sumDA_Pos,sumDA_Neg,df_percentage,sumsuperDA,suminvestDA,sumEssenDA,countOper1,countOper2,countOper3,countOper4,countOper5,countOper6,countOper7,countOper8],axis=1,sort=False)
df2.columns = ['Num_superfluous','Num_investment', 'Num_essencials','Num_DAPos','Num_DANeg','Sum_DAPos','Sum_DANeg','Da_Percentage','Sum_DA_Sup','Sum_DA_Inv','Sum_DA_Ess','Num_Oper1','Num_Oper2','Num_Oper3','Num_Oper4','Num_Oper5','Num_Oper6','Num_Oper7','Num_Oper8']
df2.head(10)

#df2.to_excel('df2.xlsx')

#Defining last 3 questions

df2['Q1'] = 0
df2['Q2'] = 0
df2['Q3'] = 0

df2.loc [(df2.Da_Percentage > 0) & (df2.Da_Percentage <= 0.93),'Q1'] = 'A'
df2.loc [(df2.Da_Percentage > 0.93) & (df2.Da_Percentage <= 0.99),'Q1'] = 'B'
df2.loc [(df2.Da_Percentage > 0.99) & (df2.Da_Percentage <= 1.03),'Q1'] = 'C'
df2.loc [(df2.Da_Percentage > 1.03) & (df2.Da_Percentage <= 1.051),'Q1'] = 'D'
df2.loc [(df2.Da_Percentage > 1.051),'Q1'] = 'E'

df2.loc [(df2.Sum_DA_Sup < 0) & (df2.Sum_DA_Sup >= -5800),'Q2'] = 'A'
df2.loc [(df2.Sum_DA_Sup < -5800) & (df2.Sum_DA_Sup >= -7900),'Q2'] = 'B'
df2.loc [(df2.Sum_DA_Sup < -7900) & (df2.Sum_DA_Sup >= -20000),'Q2'] = 'C'
df2.loc [(df2.Sum_DA_Sup < -20000) & (df2.Sum_DA_Sup >= -35000),'Q2'] = 'D'
df2.loc [(df2.Sum_DA_Sup < -35000),'Q2'] = 'E'

df2.loc [(df2.Num_Oper5 > 0) & (df2.Num_Oper5 <= 25),'Q3'] = 'A'
df2.loc [(df2.Num_Oper5 > 25) & (df2.Num_Oper5 <= 80),'Q3'] = 'B'
df2.loc [(df2.Num_Oper5 > 80) & (df2.Num_Oper5 <= 97),'Q3'] = 'C'
df2.loc [(df2.Num_Oper5 > 97) & (df2.Num_Oper5 <= 111),'Q3'] = 'D'
df2.loc [(df2.Num_Oper5 > 111),'Q3'] = 'E'
df2

#export training data
df2['Openness']=0
df2['Conscientiousness']=0
df2['Extraversion']=0
df2['Agreeableness']=0
df2['Neuroticism']=0
df2.head()

#Q1=df2['Q1']
#df2=df2.join(pd.get_dummies(Q1,prefix=Q1))
#df2.keys()



Q1dummy=pd.get_dummies(df2['Q1'],prefix='Q1')
Q1dummy
df2=df2.join(Q1dummy)
df2.keys()
df2.head()
Q2dummy=pd.get_dummies(df2['Q2'],prefix='Q2')
Q2dummy
df2=df2.join(Q2dummy)
df2.keys()
df2.head()
Q3dummy=pd.get_dummies(df2['Q3'],prefix='Q3')
Q3dummy
df2=df2.join(Q3dummy)
df2.keys()
df2.head()

df2['Openness']=0.5426*(df2['Q1_A']+df2['Q2_A']+df2['Q3_A'])+1.2992*(df2['Q1_B']+df2['Q2_B']+df2['Q3_B'])+1.5350*(df2['Q1_C']+df2['Q2_C']+df2['Q3_C'])+0.8700*(df2['Q1_D']+df2['Q2_D']+df2['Q3_D'])+2.5573*(df2['Q1_E']+df2['Q2_E']+df2['Q3_E'])-0.7987
df2['Openness']
df2['Conscientiousness']=1.1075*(df2['Q1_A']+df2['Q2_A']+df2['Q3_A'])-0.2429*(df2['Q1_B']+df2['Q2_B']+df2['Q3_B'])-0.0947*(df2['Q1_C']+df2['Q2_C']+df2['Q3_C'])+0.8700*(df2['Q1_D']+df2['Q2_D']+df2['Q3_D'])+0.3457*(df2['Q1_E']+df2['Q2_E']+df2['Q3_E'])-6.7612
df2['Conscientiousness']
df2['Extraversion']=0.0457*(df2['Q1_A']+df2['Q2_A']+df2['Q3_A'])-13.2535*(df2['Q1_B']+df2['Q2_B']+df2['Q3_B'])-0.1389*(df2['Q1_C']+df2['Q2_C']+df2['Q3_C'])-1.4815*(df2['Q1_D']+df2['Q2_D']+df2['Q3_D'])-1.5505*(df2['Q1_E']+df2['Q2_E']+df2['Q3_E'])+16.6073
df2['Extraversion']
df2['Agreeableness']=0.2742*(df2['Q1_A']+df2['Q2_A']+df2['Q3_A'])-1.2962*(df2['Q1_B']+df2['Q2_B']+df2['Q3_B'])-0.0770*(df2['Q1_C']+df2['Q2_C']+df2['Q3_C'])-0.4142*(df2['Q1_D']+df2['Q2_D']+df2['Q3_D'])-1.7046*(df2['Q1_E']+df2['Q2_E']+df2['Q3_E'])-4.3258
df2['Agreeableness']
df2['Neuroticism']=-0.2750*(df2['Q1_A']+df2['Q2_A']+df2['Q3_A'])-0.1276*(df2['Q1_B']+df2['Q2_B']+df2['Q3_B'])-0.7074*(df2['Q1_C']+df2['Q2_C']+df2['Q3_C'])-0.8657*(df2['Q1_D']+df2['Q2_D']+df2['Q3_D'])-0.7667*(df2['Q1_E']+df2['Q2_E']+df2['Q3_E'])+1.7046
df2['Neuroticism']

df2.keys()
df2

df.to_csv('/Users/suisland/Downloads/DE-final/df.csv',index = False)
df2.to_csv('/Users/suisland/Downloads/DE-final/withpersonalty.csv',index = False)
##########EDA，before this is the dataset we use to do sas, after this is EDA part.

# Historgram with Sum_DA_Sup variable
numOfBins = math.ceil(math.sqrt(len(df2['Sum_DA_Sup'])))
binWidth = (df2['Sum_DA_Sup'].max() - df2['Sum_DA_Sup'].min())/numOfBins

histGraph = df2.hist(column='Sum_DA_Sup', bins=numOfBins, grid=False, figsize=(12,8),color='#f5a607',zorder=2,
                    rwidth=0.9)
histGraph=histGraph[0]
for x in histGraph:
    x.spines['right'].set_visible(False)
    x.spines['top'].set_visible(False)
    x.spines['left'].set_visible(False)
    
    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", 
                   labelleft="on")
    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)
    
    # Remove title
    x.set_title('')
    
    # Set x-axis label
    x.set_xlabel("Sum_DA_Sup", labelpad=20, weight='bold', size=12)
    
    # Set y-axis label
    x.set_ylabel("Number", labelpad=20, weight='bold', size=12)
    
    # Format y-axis label
    fmtr = ticker.StrMethodFormatter('{x:,g}')
    x.yaxis.set_major_formatter(fmtr)
plt.savefig('DA_type_hist.png')

# Historgram with Da_Percentage variable
numOfBins_da = math.ceil(math.sqrt(len(df2['Da_Percentage'])))
binWidth_da = (df2['Da_Percentage'].max() - df2['Da_Percentage'].min())/numOfBins_da

histGraph = df2.hist(column='Da_Percentage', bins=numOfBins_da, grid=False, figsize=(12,8),color='#86bf91',zorder=2,
                    rwidth=0.9)
histGraph=histGraph[0]
for x in histGraph:
    x.spines['right'].set_visible(False)
    x.spines['top'].set_visible(False)
    x.spines['left'].set_visible(False)
    
    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", 
                   labelleft="on")
    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)
    
    # Remove title
    x.set_title('')
    
    # Set x-axis label
    x.set_xlabel("Da_Percentage", labelpad=20, weight='bold', size=12)
    
    # Set y-axis label
    x.set_ylabel("Number", labelpad=20, weight='bold', size=12)
    
    # Format y-axis label
    fmtr = ticker.StrMethodFormatter('{x:,g}')
    x.yaxis.set_major_formatter(fmtr)
plt.savefig('Da_Percentage.png')    

# Area chart  with  Sum_DA_Sup,Sum_DA_Inv,Sum_DA_Ess
df2[['Sum_DA_Sup','Sum_DA_Inv','Sum_DA_Ess']].plot.area(alpha=0.6)
plt.savefig('DA_type.png')


#histogram
df8 = df.loc[df.DA<0]
df9 = df.loc[df.DA>0]
plt.hist(df8.DA, bins=20, normed=0, width =40, facecolor="darkseagreen", alpha=0.7)
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')

#Prepare data for plotting the scatter plot.

DAPosAvgByCus = df8.groupby('Customerid')['DA'].mean()
DANegAvgByCus = df9.groupby('Customerid')['DA'].mean()
DAAvgByCus = pd.concat([DAPosAvgByCus,DANegAvgByCus],axis=1)
DAAvgByCus['Customerid']='1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40'
DAAvgByCus.rename(columns={ DAAvgByCus.columns[1]: "DAPos" }, inplace=True)
DAAvgByCus.columns = ['DANeg', 'DAPos', 'Customerid']
DAAvgByCus.DANeg = abs(DAAvgByCus.DANeg)
DAAvgByCus

#Scatterplot

a = plt.scatter(DAAvgByCus.Customerid, DAAvgByCus.DAPos,color='blue', alpha=0.5)
a = plt.scatter(DAAvgByCus.Customerid, DAAvgByCus.DANeg,color='green', alpha=0.5)
a.axes.get_xaxis().set_visible(False)
plt.savefig('dots.png')

#Correlation Matrix
df3=pd.concat([countsuper,countinvest,countessen,countpositiveDA,countnegativeDA,sumDA_Neg,df_percentage,sumsuperDA,suminvestDA,sumEssenDA],axis=1,sort=False)
df3.columns = ['Num_superfluous','Num_investment', 'Num_essencials','Num_DAPos','Num_DANeg','Sum_DANeg','Da_Percentage','Sum_DA_Sup','Sum_DA_Inv','Sum_DA_Ess']
df3.head(10)
corr = df3.corr()
ax = sns.heatmap(
        corr,
        vmin = -1, vmax = 1, center =0,
        cmap = sns.diverging_palette(20,220,n=200),
        square = True
        )
ax.get_xticklabels(),
rotation = 45,
horizontalalignment = 'right'


plt.savefig('picture1') 

#Boxplot

df4=pd.concat([countOper1,countOper2,countOper3,countOper4,countOper5,countOper6,countOper7,countOper8],axis=1,sort=False)
df4.columns = ['Num_Oper1','Num_Oper2','Num_Oper3','Num_Oper4','Num_Oper5','Num_Oper6','Num_Oper7','Num_Oper8']

ax = sns.boxplot(data = df4,orient = "h", palette = "Set2")
