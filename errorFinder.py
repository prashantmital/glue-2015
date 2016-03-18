def parser(file1):
    '''
    This function takes a 'file1' of a very particular form and finds the errors
    between the file's values and the equations that they model. The function
    utilizes another function called modelFunc which gives the correct answer from
    the particular equation from inputted parameters.
    '''

    # Initialize solution lists
    paraList = []; # Holds list of points
    ansList = []; # Computed values at paraList points

    f1 = open(file1, "r")

    for k in range(5):
        f1.readline()

    _data = f1.readline()
    numPoints= int(_data.split()[1])
    for i in range(numPoints):
        a = f1.readline()
        a = a.strip()
        a = a.split(' ')
        a = [float(k) for k in a]
        paraList.append(tuple(a))

    # Skip over useless stuff
    f1.readline()
    _data = f1.readline()
    numCells = int(_data.split()[1])
    for k in range(numCells+5):
        f1.readline()

    for k in range(numPoints):
        _data = f1.readline()
        _data = [float(x) for x in _data.split()]
        ansList.append(tuple(_data))

    return paraList, ansList


def create_err_vtk(src, error):
    dst_base = src.split('.')[0]
    dst = str(dst_base) + "-err.vtk"

    errvtk = []

    f1 = open(src, "r")

    for k in range(5):
        errvtk.append(f1.readline())

    _data = f1.readline()
    errvtk.append(_data)
    numPoints= int(_data.split()[1])

    # POSSIBLE: add check here to check if number of points
    #       is the same as the length of error

    for i in range(numPoints):
        errvtk.append(f1.readline())

    # Skip over useless stuff
    errvtk.append(f1.readline())
    _data = f1.readline()
    errvtk.append(_data)
    numCells = int(_data.split()[1])
    for k in range(numCells+5):
        errvtk.append(f1.readline())

    for k, err in zip(range(numPoints), error):
        line = str(err[0]) + ' ' + str(err[1]) + ' ' + str(err[2]) + '\n'
        errvtk.append(line)

    with open(dst, 'w') as f2:
        f2.writelines(errvtk)



if __name__=='__main__':
    from modelFunc import u_exact
    from numpy import abs

    lam_in = 5
    src = "CG_benchmark_05.vtk"
    points, data = parser(src)
    error = []
    for (coord, datapoint) in zip(points, data):
        _truesol = u_exact(*coord, lam=lam_in)
        _error = [abs(datapoint[idx] - _truesol[idx]) for idx in range(3)]
        error.append(_error)

    create_err_vtk(src, error)
