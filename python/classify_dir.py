
import numpy as np
from skimage.io import imread
from skimage.color import gray2rgb
from skimage.transform import resize
from keras.applications.imagenet_utils import decode_predictions
from classification_models.keras import Classifiers

import glob
from pathlib import Path
import argparse

# read and prepare image
def load_image(name, tensor_width, tensor_height, preprocess_input):
    try:
        x = imread(name, as_gray=False)
    except:
        return None
        
    if len(x.shape)==2:
        x = gray2rgb(x)
    if x is None:
        return None
    x = resize(x, (tensor_width, tensor_height)) * 255    # cast back to 0-255 range
    x = preprocess_input(x)
    x = np.expand_dims(x, 0)
    return x


def classify_imagenet(dirname):
    # Init and load model
    keras_obj, preprocess_input = Classifiers.get("inceptionv3") # 'resnet18')
    model = keras_obj(input_shape=(299,299,3), weights='imagenet', classes=1000)

    # Classify all images in a folder.
    for name in glob.glob(dirname + "/*.jpg"):
        x = load_image(name, 299, 299, preprocess_input)
        if x is None:
            continue

        # processing image
        y = model.predict(x)
        # result
        class_str = decode_predictions(y)[0][0][1]

        class_dir = Path(dirname) / class_str
        if not class_dir.is_dir():
            # Create new subdir if not exists.
            class_dir.mkdir(exist_ok=True)

        # move image file to subdir
        name_only = Path(name).relative_to(Path(dirname))
        target_name = class_dir / name_only
        Path(name).rename(target_name)
        print(name, " => ", str(target_name))

# classify_imagenet("img/people")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Classify images in a folder using inceptionv3 model."
    )

    parser.add_argument(
        "-i", "--inname", type=str, default="", help="Input dir name"
    )

    args = parser.parse_args()
    if (args.inname == ""):
        print("No input dir name.")
        exit(1)

    classify_imagenet(args.inname)
