
import numpy as np



aa = np.full((2,2),7)

print(aa)
#creating sequece of numbers

arr = np.arange(1,10,2)
print(arr)


identity_metrix = np.eye(4)
print(identity_metrix)


#shape 


arra = np.array([[1,2,3],
                [4,5,6]])

print(arra.shape)


#size

arr = np.array([[10,20,30],
                [40,50,60]])

print(arr.size)


#number of dimensions

ar1 = np.array([1,2,3,4,5])

ar3 = np.array([[1, 2, 3], [4, 5, 0]])  # pad with 0 or some default value



print(ar1.ndim)

print(ar3.ndim)


#to see data type under the array
art = np.array([1,23,4,5])

print(art.dtype)

#astype

a = np.array([1.2,3.4,5.1,3.2])

int_arr = a.astype(int)
print(int_arr)
print(int_arr.dtype)

#operators
w = np.array([1,2,3,4,6])
print(w * 2)
print(w ** 2)
print(w + 2)


#agreegation


e = np.array([10,20,30,40,50])
print(np.sum(e))
print(np.std(e))
print(np.var(e))
print(np.mean(e))
print(np.median(e))


g = np.array([102,23,4,5,5,66])

print(g[0])
print(g[-1])
print(g[4])
print(g[0:-1])
print(g[::4])
print(g[::-1])

#fnacy false
p = np.array([102,23,4,5,5,66])
print(p[[0,3,5]])

#condition indexing

a = np.array([102,23,4,5,5,66])

print(a > 4)

#reshaping and manipulating test 

p = np.array([102,23,4,5,5,66])
rshape_arr = p.reshape(2,3)
print(rshape_arr)
print(rshape_arr.flatten())
#insertion
z = np.array([[1,2],[3,4]])
print(z)
print(z.flatten())
print(z.ravel())

r = np.insert(z,1,[5,6],axis=0)
print(r)
p = np.array([102,23,4,5,5,66])


w = np.insert(p,2,100)
print(w)

k = np.array([[1,2],[3,4]])
g = np.append(k,[5,6])
print(g)
u1 = np.array([1,2,3])
u2 = np.array([3,4,56,67])
u3_ans = np.concatenate((u1,u2))
print(u3_ans)


#delete 
j = np.array([10,20,30,405,60])

h = np.delete(j,0)
print(h)
#for two dimensional array

kk = np.array([[1,2,3,4],[5,6,7,8]])
kkk = np.delete(kk,0,axis=0)
print(kkk)

arr1 = np.array([10,20,30,40,50,607])
print(np.vstack(arr1))
print(np.hstack(arr1))