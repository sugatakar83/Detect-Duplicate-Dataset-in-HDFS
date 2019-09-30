from PythonScripts.RMSEofArrays import rmseofarrays
import numpy as np

arr1 = [[2,5],[7,9],[1,9]]
arr2 = [[2,5],[7,9],[1,9]]

arr3 = [[200,50],[700,90],[100,29]]
arr4 = [[2,5],[7,9],[1,9]]
#result = rmseofarrays(arr1,arr2)
rmse_val = rmseofarrays(np.array(arr1), np.array(arr2))
#result = np.sqrt(((arr1-arr2)**2).mean())
print(rmse_val)