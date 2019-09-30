from PythonScripts.PermutationTest import exact_mc_perm_test
import numpy as np
arr1 = [[2,5],[7,9],[2,9]]
arr2 = [[3,5],[7,9],[2,9]]
arr3 = [[2,5],[7,9],[1,9]]
arr4 = [[20,50],[70,90],[10,900]]
permvalue = exact_mc_perm_test(arr1, arr2, 1)

n, k = len(arr1), 0
zs = np.concatenate([arr1, arr2])
diff = np.abs(np.mean(arr1) - np.mean(arr2))
for j in range(10):
    np.random.shuffle(zs)
    k += diff < np.abs(np.mean(zs[:n]) - np.mean(zs[n:]))
    print(np.mean(zs[:n]))
    print(np.mean(zs[n:]))
    print("----------------")