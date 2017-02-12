#import cc_dat_utils
from cc_dat_utils import make_cc_data_from_dat

thatdata = make_cc_data_from_dat('data\pfgd_test.dat')
print(str(thatdata))

with open('pfgd_test.txt', 'w') as f:
    f.write(str(thatdata))
f.close()

