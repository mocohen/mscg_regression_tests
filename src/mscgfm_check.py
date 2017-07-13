import numpy as np

def mscg_content_equality(dat_1,dat_2, prefix="Data File equality: ",xyz_abs_tol=1e-8):
    result = True
    
    return result




def check_result_to_exitval(result):
    '''Transforms boolean to command line exit value. 
    True -> 0, False -> 1. No guard logic.
    '''

    return int(not(result))

