import numpy as np
import cv2

# from skimage.io import imread
# from skimage.color import gray2rgb
from skimage.transform import resize
from keras.applications.imagenet_utils import decode_predictions
from classification_models.keras import Classifiers

import glob
from pathlib import Path
import argparse
import uuid


# read and prepare image
def load_image(name, tensor_width, tensor_height, preprocess_input):
    try:
        x = cv2.imread(name, cv2.IMREAD_COLOR)  # as_gray=False)
    except:
        return None

    # if len(x.shape) == 2:
    #     x = gray2rgb(x)
    if x is None:
        return None
    x = resize(x, (tensor_width, tensor_height)) * 255  # cast back to 0-255 range
    x = preprocess_input(x)
    x = np.expand_dims(x, 0)
    return x


def classify_imagenet(dirname, recursive_flag):
    # Init and load model
    keras_obj, preprocess_input = Classifiers.get("inceptionv3")  # 'resnet18')
    model = keras_obj(input_shape=(299, 299, 3), weights="imagenet", classes=1000)

    # Create new folder dirname / "_keras" if recursive.
    if recursive_flag:
        keras_dir = Path(dirname + "_keras")
        keras_dir.mkdir(exist_ok=True)
        print("Created new dir = ", str(keras_dir))
    else:
        keras_dir = Path(dirname)

    # Classify all images in a folder.
    name_list = (
        glob.glob(dirname + "/**/*.jpg", recursive=True)
        + glob.glob(dirname + "/**/*.jpeg", recursive=True)
        + glob.glob(dirname + "/**/*.png", recursive=True)
        + glob.glob(dirname + "/**/*.bmp", recursive=True)
        + glob.glob(dirname + "/**/*.tif", recursive=True)
        + glob.glob(dirname + "/**/*.tiff", recursive=True)
        if recursive_flag
        else glob.glob(dirname + "/*.jpg")
        + glob.glob(dirname + "/*.jpeg")
        + glob.glob(dirname + "/*.png")
        + glob.glob(dirname + "/*.bmp")
        + glob.glob(dirname + "/*.tif")
        + glob.glob(dirname + "/*.tiff")
    )
    for name in name_list:
        x = load_image(name, 299, 299, preprocess_input)
        if x is None:
            continue

        # processing image
        y = model.predict(x)
        # result
        class_str = decode_predictions(y)[0][0][1]

        class_dir = keras_dir / class_str
        if not class_dir.is_dir():
            # Create new subdir if not exists.
            class_dir.mkdir(exist_ok=True)

        # move image file to subdir
        name_only = Path(name).name
        target_name = class_dir / name_only

        # Check duplicate name
        if target_name.exists():
            # Create unique name using uuid
            unique_name = str(uuid.uuid4())
            target_name = class_dir / Path(unique_name + str(Path(name).suffix))

        Path(name).rename(target_name)
        print(name, " => ", str(target_name))


# classify_imagenet("img/people")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Classify images in a folder using inceptionv3 model."
    )

    parser.add_argument(
        "-i",
        "--inname",
        type=str,
        default="",
        help="Input dir name without ending slash",
    )

    parser.add_argument(
        "-r", "--recursive", type=bool, default=False, help="Recursive subfolders"
    )

    args = parser.parse_args()
    if args.inname == "":
        print("No input dir name.")
        exit(1)

    classify_imagenet(args.inname, args.recursive)
