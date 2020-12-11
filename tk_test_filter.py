from __future__ import division

import tk_test_SPM as tts


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


output_file = open('tk_test_output.txt','w')

res = tts.run_SPM(filter, full)
print res
for r in res:
    output_file.write('avg_value of ' + filter + ': ' + r + '\n')
output_file.write('------------------------------------\n')

    
output_file.close()