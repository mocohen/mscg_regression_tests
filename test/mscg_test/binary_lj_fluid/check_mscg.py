#!/usr/bin/env python2

import sys
sys.path.append("../../../src/")
import mscgfm_check as check

test_name = ['1_1.dat', '2_2.dat', '1_2.dat']

for fname in test_name :
    out_file = open("output/" + fname,'r').readlines()
    ref_file = open("reference/" + fname,'r').readlines()

    result=check.mscg_content_equality(out_file,ref_file)

    sys.exit(check.check_result_to_exitval(result))

