#!/usr/bin/env python2

import sys, os, getopt
sys.path.append('../../../src/')
import numpy as np
import subprocess
import mscgfm_check as check
import shutil 


############################### config #####################################

opts, args = getopt.getopt(sys.argv[1:], "f:s:e:")

mscg_exe = ''
mscg_suffix = ''
for opt, arg in opts:
    if opt == '-f':
        mscg_exec_path = arg
    elif opt == '-s':
        mscg_suffix = arg
    elif opt == '-e':
        mscg_exe = arg


input_traj = "../trajectories/4_site_d_non_periodic.lammpstrj"

output_dir ='output/'
input_dir  ='input/'
reference_dir ='reference/'

filesToCheck = ['1_1_1_ang.dat']

mscg_exec = mscg_exec_path + '/' + 'newfm' + mscg_suffix
range_exec = mscg_exec_path + '/' + 'rangefinder' + mscg_suffix

############################### run ########################################

#try:
#    os.chdir(output_dir)
#except:
#    print('Error: Could not find directory %s\n', output_dir)
#    exit()
#
#input_traj = '../' + input_traj

if not os.path.isfile(mscg_exec):
    raise Exception('Could not find mscg executable\n')
if not os.path.isfile(range_exec):
    raise Exception('Could not find rangefinder executable\n')
if not os.path.isfile(input_traj):
    raise Exception('Could not find trajectory %s\n', input_traj)

shutil.copy2(input_dir+'rmin.in',    output_dir)
shutil.copy2(input_dir+'rmin_b.in',  output_dir)
shutil.copy2(input_dir+'control.in', output_dir)
shutil.copy2(input_dir+'top.in',     output_dir)


#############################
try: 
    test_output = subprocess.check_output([mscg_exec, '-l', '../'+input_traj], cwd=output_dir, stderr= subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    print e.output
    print "MSCG Did not complete! Please check the output\n"
    sys.exit(1)

lastLine  = test_output.split('\n')[-2]
if 'Freeing' not in lastLine:
    print "MSCG Did not complete! Please check the output\n"
    sys.exit(1);

result = True

for fileCheck in filesToCheck:
    dat1 = np.loadtxt(output_dir + fileCheck, unpack=True)
    dat2 = np.loadtxt(reference_dir + fileCheck, unpack=True)
    myResult = check.mscg_content_equality(dat1, dat2)
    if myResult == False:
        result = False


sys.exit(check.check_result_to_exitval(result))
