from cython.parallel cimport prange
cimport openmp
import numpy as np
cimport numpy as np
import cython
cimport cython


cpdef void are_any_colors_in_pic(
    unsigned char[:] pic,
    unsigned char[::1] colors,
    Py_ssize_t [::1] results,
    Py_ssize_t width,
    Py_ssize_t totallengthpic,
    Py_ssize_t totallengthcolor,
    int cpus,
    ):
    cdef:
        Py_ssize_t i, j
        unsigned char r,g,b
        openmp.omp_lock_t locker
    if cpus < 1:
        cpus=openmp.omp_get_max_threads()
    if cpus > 1:
        openmp.omp_set_num_threads(cpus)
        openmp.omp_init_lock(&locker)
        for i in prange(0, totallengthcolor, 3, nogil=True): # should be possible, but not work not working: use_threads_if=cpus>1
            r = colors[i]
            g = colors[i + 1]
            b = colors[i + 2]
            for j in range(0, totallengthpic, 3):
                if results[0]==1:
                    break
                if (r == pic[j]) and (g == pic[j+1]) and (b == pic[j+2]):
                    openmp.omp_set_lock(&locker)
                    results[0]=1
                    openmp.omp_unset_lock(&locker)
                    break
            if results[0]==1:
                break
        openmp.omp_destroy_lock(&locker)
    else:
        for i in range(0, totallengthcolor, 3):
            r = colors[i]
            g = colors[i + 1]
            b = colors[i + 2]
            for j in range(0, totallengthpic, 3):
                if (r == pic[j]) and (g == pic[j+1]) and (b == pic[j+2]):
                    results[0]=1
                    return


cpdef void searchforcolor(
    unsigned char[:] pic,
    unsigned char[::1] colors,
    Py_ssize_t [:,::1] results,
    Py_ssize_t [::1] countervar,
    Py_ssize_t width,
    Py_ssize_t totallengthpic,
    Py_ssize_t totallengthcolor,
    int cpus,
    bint add_results
    ):
    cdef:
        Py_ssize_t i, j
        unsigned char r,g,b
        openmp.omp_lock_t locker
    if cpus < 1:
        cpus=openmp.omp_get_max_threads()
    if cpus > 1:
        openmp.omp_set_num_threads(cpus)
        openmp.omp_init_lock(&locker)
        if add_results:
            for i in prange(0, totallengthcolor, 3, nogil=True): # should be possible, but not work not working: use_threads_if=cpus>1
                r = colors[i]
                g = colors[i + 1]
                b = colors[i + 2]
                for j in range(0, totallengthpic, 3):
                    if (r == pic[j]) and (g == pic[j+1]) and (b == pic[j+2]):
                        openmp.omp_set_lock(&locker)
                        results[countervar[0]][1] = ((j / 3) // width) #x
                        results[countervar[0]][0] = ((j / 3) % width) #y
                        results[countervar[0]][2] = b
                        results[countervar[0]][3] = g
                        results[countervar[0]][4] = r
                        countervar[0]+=1
                        openmp.omp_unset_lock(&locker)
        else:
            for i in prange(0, totallengthcolor, 3, nogil=True): # should be possible, but not work not working: use_threads_if=cpus>1
                r = colors[i]
                g = colors[i + 1]
                b = colors[i + 2]
                for j in range(0, totallengthpic, 3):
                    if (r == pic[j]) and (g == pic[j+1]) and (b == pic[j+2]):
                        openmp.omp_set_lock(&locker)
                        results[countervar[0]][1] = ((j / 3) // width) #x
                        results[countervar[0]][0] = ((j / 3) % width) #y
                        countervar[0]+=1
                        openmp.omp_unset_lock(&locker)
        openmp.omp_destroy_lock(&locker)
    else:
        if add_results:
            for i in range(0, totallengthcolor, 3):
                r = colors[i]
                g = colors[i + 1]
                b = colors[i + 2]
                for j in range(0, totallengthpic, 3):
                    if (r == pic[j]) and (g == pic[j+1]) and (b == pic[j+2]):
                        results[countervar[0]][1] = ((j / 3) // width) #x
                        results[countervar[0]][0] = ((j / 3) % width) #y
                        results[countervar[0]][2] = b
                        results[countervar[0]][3] = g
                        results[countervar[0]][4] = r
                        countervar[0]+=1
        else:
            for i in range(0, totallengthcolor, 3):
                r = colors[i]
                g = colors[i + 1]
                b = colors[i + 2]
                for j in range(0, totallengthpic, 3):
                    if (r == pic[j]) and (g == pic[j+1]) and (b == pic[j+2]):
                        results[countervar[0]][1] = ((j / 3) // width) #x
                        results[countervar[0]][0] = ((j / 3) % width) #y
                        countervar[0]+=1