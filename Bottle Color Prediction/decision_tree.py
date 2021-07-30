import pandas as pd

df=pd.read_csv('/home/susang/testdir/c_data.csv', delimiter=',')
df.head()

inputs=df.drop('color',axis='columns')
target=df['color']

from sklearn.preprocessing import LabelEncoder

le_people=LabelEncoder()
le_stall=LabelEncoder()

inputs['people_n']=le_people.fit_transform(inputs['people'])

inputs_n=inputs.drop(['people'],axis='columns')

from sklearn import tree

model=tree.DecisionTreeClassifier()

model.fit(inputs_n,target)

c=model.score(inputs_n,target)

dress_data=str(input("Enter the color of the dress:"))
b=input("Enter the stall number ranging from 1 to 4:")

if dress_data.lower()=='red':
    a=1
elif dress_data.lower()=='green':
    a=2
elif dress_data.lower()=='blue':
    a=3
elif dress_data.lower()=='yellow':
    a=4

t=model.predict([[a,b]])
r=t[0]

if r==1:
    print('The probable choice of the dress is: RED')
elif r==2:
    print('The probable choice of the dress is: GREEN')
elif r==3:
    print('The probable choice of the dress is: BLUE')
elif r==4:
    print('The probable choice of the dress is: YELLOW')    
    