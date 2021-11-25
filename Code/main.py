
def RowEchelon(Mat):

  #Mat is the matrix that needs to be converted into Row Echelon Form.

  Rows=len(Mat)
  Columns=len(Mat[0])
  count=0

  #Number of rows and columns of the given matrix are obtained.

  for k in range(Rows):

    #This loop iterates through each row.

        if count >= Columns:
            return
        i = k
        while Mat[i][count] == 0:
            i += 1
            if i == Rows:
                i = k
                count += 1
                if Columns == count:
                    return

        Mat[i],Mat[k] = Mat[k],Mat[i]
        #Swapping rows i and k.

        LV = Mat[k][count]
        #LV is the element of matrix situated below the element that needs to be changed.

        Mat[k] = [ mrx/float(LV) for mrx in Mat[k]]
        #Dividing row k by Mat[k][count]

        for i in range(Rows):
            if i != k:
                LV = Mat[i][count]
                Mat[i] = [ IV - LV*RV for RV,IV in zip(Mat[k],Mat[i])]
                #Subtracting Mat[i][count]*row r from row i.
        count += 1


A = [[1,	0,	0,	1,	0,	0,	0,	0,	4200],
[1,	-1,	-1,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	1,	-1,	-1,	0,	0,	0],
[0,	0,	1,	0,	1,	0,	0,	-1,	0],
[0,	1,	0,	0,	0,	0,	-1,	1,	0],
[0,	0,	0,	0,	0,	1,	1,	0,	4200]]
RowEchelon(A)
print("Reduced Row Echelon Form: Problem 1")
for i in A:
  print(i)

  """
Reduced Row Echelon Form: Problem 1
[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, 0.0, 0.0]
[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, 0.0]
[0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, -1.0, 0.0]
[0.0, 0.0, 0.0, 1.0, -1.0, 0.0, 1.0, 0.0, 4200.0]
[-0.0, -0.0, -0.0, -0.0, -0.0, 1.0, 1.0, -0.0, 4200.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
"""

  B = [[1,	1,	0,	0,	0,	4200],
[0,	1,	-1,	0,	-1,	0],
[1,	0,	1,	-1,	0,	0],
[0,	0,	0,	1,	1,	4200] ]
RowEchelon(A)
print("Reduced Row Echelon Form: Problem 2")
for i in A:
  print(i)

"""
 Reduced Row Echelon Form: Problem 2
[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, 0.0, 0.0]
[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, 0.0]
[0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, -1.0, 0.0]
[0.0, 0.0, 0.0, 1.0, -1.0, 0.0, 1.0, 0.0, 4200.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 4200.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
"""

