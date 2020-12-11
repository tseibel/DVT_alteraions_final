#Takes two 2D arrays turns them into an excell doc and compares them
import data_pull as dp

#directory
dir = '/home/tseibel/deep-visualization-toolbox/data_pull/auto/conv3/'


#imported 2D arrays
name_1 = 'barn_02_2D.npy'
name_2 = 'barn_05_2D.npy'





#3D array for reference
arr_3D = dp.open('barn_02.npy', dir)
shape = arr_3D.shape

#2D arrays for import
barn_01 = dp.open(name_1, dir)
barn_02 = dp.open(name_2, dir)

#2D arrays to dicts
barn_01_dict = dp.to_Dict(barn_01, shape)
barn_02_dict = dp.to_Dict(barn_02, shape)

print barn_01_dict
print barn_02_dict

#Comparing Dicts
dp.comp_Dicts(barn_01_dict, barn_02_dict, shape)
