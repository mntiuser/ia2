import matplotlib.pyplot as plt
import pandas as pd
d={
    "First_name":["Ayan","Roan","Riya","Yash","Siddhanth"],
    "Lasrt_name":["Singh","Agarwal","Shah","Bhatia","Khanna"],
    "Type":["fulltime-employee","intern","Fulltime-employee","partime-employee","fulltime-employee"],
    "Dept":["Administration","technical","administraion","technical","management"],
    "YoE":[2,3,5,7,6],"Salary":[20000,5000,10000,20000,10000]
}
df=pd.DataFrame(d)
print(df)
av=df.pivot_table(index=['Dept', 'Type'], values='Salary',aggfunc='mean') 
print("Average Salary from ecah dept:",av)
sm=df.pivot_table(index=['Type'], values='Salary', aggfunc=['sum', 'mean','count'])
sm.columns=['Total Salary', 'Mean Salary', 'Number of Employees']
print("Sum and Mean of:",sm)
st=df.pivot_table(values='Salary', index='Type',aggfunc='std')
print("Standard Deviation of salary column:",st)
plt.plot(df["Salary"],'^-')
plt.plot(df["Salary"],color='red')
plt.title('Salary by Employment Type')
plt.xlabel('values')
plt.ylabel('salary')
plt.show()
### SCATTER PLOT
x=[2,4,6,7,8,2]
y=[5,4,3,2,4,5]
plt.scatter(x,y,label='value of x,y',color='purple')
plt.title('Scatterplot')
plt.xlabel('x axis'),plt.ylabel('yaxis')
plt.show()

###PIECHART
na=["dell","lenovo","hp","victus"]
use=[23,34,63,40]
co=['red','green','yellow','blue']
e=[0,0,0.2,0.4]
plt.pie(label='use',color='co',explode='e',startangle=270,autopct='%1.2f%%')
plt.show()