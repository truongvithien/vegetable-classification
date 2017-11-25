import numpy as np

def get_feature(img_name):
    """
    :param img_name: "images/Chuoi_Su/4.jpg"
    :return:
        img_feature_name: "features/Chuoi_Su/4.npy"
        img_feature_data: [[ 0. 0. 1.340..., 0. 1.557 0. ]]
    :usage:
        from . import support_function as sf
        _, data = sf.get_feature(img_name)
    """
    img_feature_name = img_name
    img_feature_name = img_feature_name.replace("images","features")
    img_feature_name = img_feature_name.replace("jpg","npy")

    img_feature_data = np.load(img_feature_name)
    #print(img_feature_data)

    return img_feature_name, img_feature_data
