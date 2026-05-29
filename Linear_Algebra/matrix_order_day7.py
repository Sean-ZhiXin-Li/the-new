import numpy as np

def main():
    vector = np.array([1.0, 2.0])

    scale_transform = np.array([
        [2.0, 0.0],
        [0.0, 1.0],
    ])

    shear_transform = np.array([
        [1.0, 1.0],
        [0.0, 1.0],
    ])

    scale_after_shear = scale_transform @ (shear_transform @ vector)
    shear_after_scale = shear_transform @ (scale_transform @ vector)

    combined_scale_after_shear = scale_transform @ shear_transform
    combined_shear_after_scale = shear_transform @ scale_transform

    print("Vector: ", vector)
    print("A(Bv): ", scale_after_shear)
    print("B(Av): ", shear_after_scale)
    print("AB: ", combined_scale_after_shear)
    print("BA: ", combined_shear_after_scale)

if __name__ == "__main__":
    main()