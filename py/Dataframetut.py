import numpy as np
import pandas as pd


A=[1,2,3,4]
B=[5,6,7,8]
C=[9,1,1,2]
D=[3,4,5,6]
E=[7,8,9,0]


df=pd.DataFrame([A,B,C,D,E],['w','x','y','z','d'],['A','B','C','D'])
df


print()

df['E']=df['A']+df['D']
df


df.drop('d')
df
df.drop('d', inplace=True)
df


df.drop('A',axis=1)
df.drop('A',axis=1,inplace=True)
df





df['B']

df
df.loc['w']


df.loc['w']


df.loc['y','D']


df.loc[]


df



df >3


df[df>3]


df[df['B']>3]
















#


d={'a':[1,2,3,4,5],'b':[6,7,8,9,np.nan],'c':[3,4,np.nan,np.nan,np.nan],'d':[3,4,np.nan,np.nan,np.nan]}
d


df=pd.DataFrame(d)

df


df.dropna(axis=0)


df.dropna(thresh=3)

df.dropna(thresh=1)


df.dropna(thresh=2)


df.fillna(1)
df


df['b'].fillna(value=df['b'].mean())
