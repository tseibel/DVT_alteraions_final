from __future__ import division

import run_SPM_DVT as rsd


max = {
    'conv1' : 1.9921875,
    'pool1' : 1.984375,
    'conv2' : 1.984375,
    'pool2' : 1.96875,
    'conv3' : 1.96875,
    'conv4' : 1.96875,
    'conv5' : 1.96875,
    'pool5' : 1.9375,
    'fc8'   : 1
}


with open('filters.txt') as a:
    filters = a.readline()

filters = filters.split()

full = ''

output_file = open('output.txt','w')
total = 0
count = 0
for filter in filters:
    avg_filter = rsd.run_SPM(filter, full)/max[filter]
    if filter in max.keys():
        total += avg_filter
        count += 1
        output_file.write('avg_value of ' + filter + ': ' + str(avg_filter) + '\n')
    total_avg = total/count
output_file.write('------------------------------------\n')
output_file.write('OVERALL_AVG: ' + str(total_avg))

    
output_file.close()