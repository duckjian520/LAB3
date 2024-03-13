from tokenize import Ignore
import pandas as pd
import numpy as np
student_data1={
    'student_id':["S1","S2","S3","S4","S5"],
    'name':["Danniella Fenton","Ryder Storey","Bryce Jensen","Ed Bernal","Kwame Morin"],
    'marks':[200,210,190,222,199]
}
student_data2={
    'student_id':["S4","S5","S6","S7","S8"],
    'name':["Scarlette Fisher","Carla Williamson","Danta Moser","Kaiser William","Maddeeha Preston"],
    'marks':[201,200,198,219,201]
}
df1=pd.DataFrame(student_data1)
df2=pd.DataFrame(student_data2)
print(df1,"\n",df2,"\n")

print(pd.concat([df1,df2]),"\n")

print(pd.concat([df1,df2],axis=1),"\n")

new_row={
    'student_id':["S6"],
    'name':["Scarlette Fisher"],
    'marks':[205]
    }
a=pd.DataFrame(new_row)
print(pd.concat([df1,a],ignore_index=True),"\n")

Dictionary={
    'student_id':"S6",
    'name':"Scarlette Fisher",
    'marks':205
    }
b=pd.Series(Dictionary)
print(df1._append(b,ignore_index=True),"\n")

exam_data={
    'student_id':["S1","S2","S3","S4","S5","S7","S8","S9","S10","S11","S12","S13"],
    'exam_id':[23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]
    }
c=pd.DataFrame(exam_data)
d=pd.concat([df1,df2])
print(pd.merge(d,c,on='student_id'),"\n")

print(pd.merge(df1,df2,on='student_id'))

print(pd.merge(df1,df2,on='student_id',how='outer'),"\n")

data1=pd.DataFrame({
    'key1':["K0","K0","K1","K2"],
    'key2':["K0","K1","K0","K1"],
    'P':["P0","P1","P2","P3"],
    'Q':["Q0","Q1","Q2","Q3"]
})
data2=pd.DataFrame({
    'key1':["K0","K1","K1","K2"],
    'key2':["K0","K0","K0","K0"],
    'R':["R0","R1","R2","R3"],
    'S':["S0","S1","2","S3"]
})
print(pd.merge(data1,data2,on=['key1','key2'],how='left'))
print(pd.merge(data2,data1,on=['key1','key2'],how='left'),"\n")

print(pd.merge(data1,data2,on=['key1','key2'],how='right'))
print(pd.merge(data2,data1,on=['key1','key2'],how='right'),"\n")

print(pd.merge(data1,data2,on=['key1','key2']),"\n")

a1=pd.Series([1,3,2,4])
a2=pd.Series([2,3,1,4])
a3=pd.Series([4,1,3,2])
print(pd.concat([a1,a2,a3],axis=1,keys=["col1","col2","col3"]),"\n")

print(pd.merge(data1,data2,on='key1'),"\n")

data1=pd.DataFrame({
    'A':["A0","A1","A2"],
    'B':["B0","B1","B2"]
},index=["K0","K1","K2"])
data2=pd.DataFrame({
    'C':["C0","C2","C3"],
    'D':["D0","D2","D3"]
},index=["K0","K2","K3"])
print(data1.join(data2),"\n")

data1=pd.DataFrame({
    'key1':["K0","K0","K1","K2"],
    'key2':["K0","K1","K0","K1"],
    'P':["P0","P1","P2","P3"],
    'Q':["Q0","Q1","Q2","Q3"]
})
data2=pd.DataFrame({
    'key1':["K0","K1","K1","K2"],
    'key2':["K0","K0","K0","K0"],
    'R':["R0","R1","R2","R3"],
    'S':["S0","S1","2","S3"]
})
print(pd.concat([data1,data2],ignore_index=True),"\n")

a=pd.DataFrame({
    'A':[np.nan,0.0,np.nan],
    'B':[3,4,5]
})
b=pd.DataFrame({
    'A':[1,1,3],
    'B':[3.0,np.nan,3.0]
})
print(a.combine_first(b))