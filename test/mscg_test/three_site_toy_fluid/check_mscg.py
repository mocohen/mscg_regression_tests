#!/usr/bin/env python2

import sys
sys.path.append("../../../src/")
import mscgfm_check as check

test_name = ['A_A.dat', 'A_B.dat', 'A_C.dat', 'B_B.dat', 'B_C.dat', 'C_C.dat', 'A_B_bon.dat', 'B_C_bon.dat', 'B_A_C_ang.dat']

for fname in test_name :
    out_file = open("output/" + fname,'r').readlines()
    ref_file = open("reference/" + fname,'r').readlines()

    result=check.mscg_content_equality(out_file,ref_file)

    sys.exit(check.check_result_to_exitval(result))

