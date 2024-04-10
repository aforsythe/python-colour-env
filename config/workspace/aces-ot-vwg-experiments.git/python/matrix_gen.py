import colour
import numpy as np

np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.10f}'.format})

AP0_ACES = colour.models.RGB_COLOURSPACE_ACES2065_1
AP1_ACES = colour.models.RGB_COLOURSPACE_ACESCG
Rec709_D65 = colour.models.RGB_COLOURSPACE_BT709
Rec2020_D65 = colour.models.RGB_COLOURSPACE_BT2020
P3_D65 = colour.models.RGB_COLOURSPACE_P3_D65
P3_DCI = colour.models.RGB_COLOURSPACE_DCI_P3

def format_matrix(M, indent1=4, indent2=2):
    out = " " * indent1 + "{\n"
    for i in range(3):
        out = out + " " * (indent1+indent2) + "{: 0.10f}f, {: 0.10f}f, {: 0.10f}f".format(M[i][0], M[i][1], M[i][2]) + ("," if i < 2 else "") + "\n"
    out = out + " " * indent1 + "};\n"
    return out

spaces = [AP0_ACES, AP1_ACES, Rec709_D65, Rec2020_D65, P3_D65, P3_DCI]

for space in spaces:
    name = [ i for i, j in locals().items() if j == space][0]
    print("    float XYZ_to_" + name + "_matrix_data[]=")
    print(format_matrix(space.matrix_XYZ_to_RGB))

print("D65 White", colour.algebra.vector_dot(Rec709_D65.matrix_RGB_to_XYZ, [100, 100, 100]))
print("ACES White", colour.algebra.vector_dot(AP0_ACES.matrix_RGB_to_XYZ, [100, 100, 100]))