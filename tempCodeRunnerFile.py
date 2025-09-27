import pandas as pd
import numpy as np

n = 20
data = [[35,1,20,179],
        [42,2,15,200],
        [50,2,18,221],
        [60,3,10,263], 
        [67,3,8,280], 
        [75,3,12,314], 
        [80,4,5,327], 
        [90,4,5,360], 
        [95,4,6,377],
        [100,5,5,391],
        [110,5,3,425],
        [120,5,2,462],
        [130,6,2,493],
        [140,6,1,521],
        [150,6,1,552],
        [160,7,1,582],
        [175,7,2,631],
        [190,8,2,675],
        [210,8,1,740],
        [230,9,1,804]]

columns = ["A",'B','C','D']
df = pd.DataFrame(data= data , columns= columns, index= range(n))
print(df.head())
print(df.shape)

min_a = df["A"].min()
min_b = df["B"].min()
min_c = df["C"].min()
min_d = df["D"].min()

mean_a = df["A"].mean()
mean_b = df["B"].mean()
mean_c = df["C"].mean()
mean_d = df["D"].mean()

std_a = np.array(df["A"]).std()
std_b = np.array(df["B"]).std()
std_c = np.array(df["C"]).std()
std_d = np.array(df["D"]).std()

print(f"{mean_a:.2f},{std_a:.2f}")

df["A"] = (df["A"] - mean_a)/std_a
df["B"] = (df["B"] - mean_b)/std_b
df["C"] = (df["C"] - mean_c)/std_c

x = np.array(df.iloc[:,0:-1]) #all rows and columns except last column
y = np.array(df.iloc[:,-1])

th0 = 0
th1 = 0
th2 = 0
th3 = 0

x1 = x[:,0]
x2 = x[:,1]
x3 = x[:,2]

a = 0.01
ephocs = 300

for i in range(ephocs):
  yp = th0 + th1*x1 + th2*x2 + th3*x3
  err = yp - y

  th0 -= a*err.mean()
  th1 -= a*(err*x1).mean()
  th2 -= a*(err*x2).mean()
  th3 -= a*(err*x3).mean()

print(th0,th1,th2,th3)

def normalize(x1,x2,x3):
  x1_ = (x1-mean_a)/std_a
  x2_ = (x2-mean_b)/std_b
  x3_ = (x3-mean_c)/std_c

  return np.array([x1_,x2_,x3_])

def predict(x1,x2,x3):
  nor = normalize(x1,x2,x3)
  yp = th0 + th1*nor[0] + th2*nor[1] + th3*nor[2]
  return yp

print(predict(150,3,5))

yp = th0 + th1*x1 + th2*x2 + th3*x3
err = yp-y
mse = (err**2).mean()/2
print(mse)