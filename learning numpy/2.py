import numpy as np

prices  = np.array([100,200,300])


discount = 10

final_prizes = prices - discount
final = prices - (prices * discount/100)
print(final)

arrr =np.array([100,200,300])

result = arrr * 2
print(result)

matrix  = ([[1,2,3],[4,5,6]])
vector = ([10,20,30])

resul = matrix + vector
print(resul)

arr1 = ([[1,2,3],[4,5,6]])
arr2 = ([1,2])

res = arr1 + arr2

print(res)

#fast vectorization
rr1 = np.array([1,2,3])
rr2 = np.array([4,5,6])
re = rr1 + rr2
print(re)


n = np.array([1,2,np.nan,4,5,np.nan])

#r = (np.isnan(n))
#print(np.nan == np.nan)

r = np.nan_to_num(n,nan=100)# in this function thee default value iss zero

print(r)

arrayy = np.array([1,2,np.inf,4,-np.inf,6])

print(arrayy)

cleaned_arr = np.nan_to_num(arrayy,posinf=1000,neginf=-1000)

print(cleaned_arr)