import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('D:\\datasets 5thsem\\dataset\\auto-mpg.csv')
print(data)
hp_mean=data['Horsepower'].mean()
print("mean:",hp_mean)
s1=data['Acceleration'].std()
print("standard deviation",s1)
m_y=data.groupby('Model Year')['Model Year'].count()
print(m_y)
###histogram
data=pd.read_csv('D:\\datasets 5thsem\\dataset\\titanic.csv')
a_s=data[data['survived']==1]['age']
an_s=data[data['survived']==0]['age']
plt.hist(a_s,color='green',alpha=0.5,label="survived")
plt.hist(an_s,color='purple',alpha=1,label="not survived")
plt.xlabel('age')
plt.ylabel('frequency')
plt.title('age distribution of survived and not survived pasengers')
plt.legend()
plt.show()

