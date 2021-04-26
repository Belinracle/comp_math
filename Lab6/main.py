import holeckiy_method
import utils as ut

matrix = (("6.25*x1 -     x2 +  0.5*x3 = 7.5   \n"
           "    -x1 +   5*x2 + 2.12*x3 = -8.68 \n"
           " 0.5*x1 +2.12*x2 +  3.6*x3 = -0.24 \n",
           ([[6.25, -1, 0.5], [-1, 5, 2.12], [0.5, 2.12, 3.6]], [7.5, -8.68, -0.24])),
          ("  81*x1 + -45*x2 +   45*x3 = 531   \n"
           " -45*x1 +  50*x2 +  -15*x3 = -460  \n"
           "  45*x1 + -15*x2 +   38*x3 = 193   \n",
           ([[81, -45, 45], [-45, 50, -15], [45, -15, 38]], [531, -460, 193])),
          )

if __name__ == '__main__':
    matrix_num = ut.choose_from_map(matrix)
    result = holeckiy_method.solve_system(matrix[matrix_num][1][0], matrix[matrix_num][1][1])
    for i in range(len(result)):
        print("x" + str(i+1) + "=" + str(result[i]))
