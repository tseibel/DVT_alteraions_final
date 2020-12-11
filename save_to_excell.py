import data_pull as dp

#desired save directory
dir = '/home/tseibel/deep-visualization-toolbox/data_pull/auto/conv3/'
filenames = ['barn_04_greengrass.npy','barn_04_red_white.npy','barn_04_red_white_grass.npy','barn_04_red_white_grass_sky.npy','barn_04_red_white_moregrass_sky.npy','barn_04_red_white_sky.npy','barn_04_sky.npy']
#filenames = ['barn_04.npy']
for filename in filenames:
    print filename

    #3D array we are opening
    array_3D = dp.open(filename, dir)

    #shape of 3D array
    orginal_shape = array_3D.shape

    #3D to 2D
    array_2D = dp.to_array_2D(array_3D)

    #Save 2D array
    dp.save(filename[0:4] + '_2D.npy', filename, dir)

    #Save 2D array into excel
    dp.to_excel(array_2D, orginal_shape , filename[0:-4] + '_2D.xlsx', dir)
