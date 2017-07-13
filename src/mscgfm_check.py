import numpy as np

def mscg_content_equality(dat_1,dat_2, prefix="Data File equality: ",xyz_abs_tol=1e-8):
    result = True
    if not(np.array_equal(dat_1[0], dat_2[0])):
        print(prefix+"Warning: Coordinates don't match bit for bit.")

        sqdiff_mat = (dat_1[0]-dat_2[0])**2
        min_mat    = np.minimum(abs(dat_1[0]),abs(dat_2[0]))

        residual       = sqdiff_mat.mean()**0.5
        max_residual   = sqdiff_mat.max()**0.5
        print(prefix+"Warning: RMS coordinate residual: {}".format(residual))
        print(prefix+"Warning: Max coordinate residual: {}".format(max_residual))

        rel_residual_mat = sqdiff_mat**0.5/min_mat

        residual         = rel_residual_mat.mean()
        max_residual     = rel_residual_mat.max()
        print(prefix+"Warning: Mean relative coordinate residual: {}".format(residual))
        print(prefix+"Warning: Max relative coordinate residual: {}".format(max_residual))

        print(prefix+"First sqdiff coordinate frame: {}".format(\
                (dat_1[0]-dat_2[0])))

        violations = np.nonzero((dat_1[0]-dat_2[0]) > xyz_abs_tol)

        print(prefix+"Indices violating residual ({}): {}".format(\
                xyz_abs_tol,violations))

        if (residual > xyz_abs_tol):
            result=False
    if not(np.array_equal(dat_1[1], dat_2[1])):
        print(prefix+"Warning: Forces don't match bit for bit.")

        sqdiff_mat = (dat_1[1]-dat_2[1])**2
        min_mat    = np.minimum(abs(dat_1[1]),abs(dat_2[1]))

        residual       = sqdiff_mat.mean()**0.5
        max_residual   = sqdiff_mat.max()**0.5
        print(prefix+"Warning: RMS Force residual: {}".format(residual))
        print(prefix+"Warning: Max Force residual: {}".format(max_residual))

        rel_residual_mat = sqdiff_mat**0.5/min_mat

        residual         = rel_residual_mat.mean()
        max_residual     = rel_residual_mat.max()
        print(prefix+"Warning: Mean relative force residual: {}".format(residual))
        print(prefix+"Warning: Max relative force residual: {}".format(max_residual))

        print(prefix+"First sqdiff coordinate frame: {}".format(\
                (dat_1[1]-dat_2[1])))

        violations = np.nonzero((dat_1[1]-dat_2[1]) > xyz_abs_tol)

        print(prefix+"Indices violating residual ({}): {}".format(\
                xyz_abs_tol,violations))

        if (residual > xyz_abs_tol):
            result=False    
    return result




def check_result_to_exitval(result):
    '''Transforms boolean to command line exit value. 
    True -> 0, False -> 1. No guard logic.
    '''

    return int(not(result))

