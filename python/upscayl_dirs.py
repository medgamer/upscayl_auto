import argparse
import subprocess
from pathlib import Path
import glob
import cv2
import numpy as np


# Detect whether input name having png extension.
def is_png_bmp_tif(inname):
    ext = Path(inname).suffix
    ext_list = [
        ".png",
        ".PNG",
        ".Png",
        ".bmp",
        ".Bmp",
        ".BMP",
        ".tif",
        ".Tif",
        ".TIF",
        ".tiff",
        ".Tiff",
        ".TIFF",
    ]
    if ext in ext_list:
        return True
    else:
        return False


def to_jpg(inname, jpgname):
    img = cv2.imread(inname)
    cv2.imwrite(jpgname, img)
    return jpgname


# Add and replace extension to "_x4.jpg"
def name_add_x4(inname):
    file_path = Path(inname)
    file_noext = file_path.parent / file_path.stem
    outname = str(file_noext) + "_x4.jpg"
    return outname


# Call upscayl-bin on one image
def run_upscayl_one(inname, outname, model_name):

    # Call png2jpg first if input is a png file.
    if is_png_bmp_tif(inname):
        jpgname = "xyz.jpg"
        to_jpg(inname, jpgname)
        inname = jpgname

    cmd_list = ["upscayl-bin", "-i", inname, "-o", "abc.jpg", "-n", model_name]
    # Basic execution
    res1 = subprocess.run(cmd_list)

    # Now use OpenCV to read quality=100 jpeg image and write to quality=95 ;-)
    temp_img = cv2.imread("abc.jpg")
    if outname.isascii():
        # Normal English name.
        res2 = cv2.imwrite(outname, temp_img, [cv2.IMWRITE_JPEG_QUALITY, 95])
    else:
        # Unicode name.
        res2, buffer = cv2.imencode(".jpg", temp_img, [cv2.IMWRITE_JPEG_QUALITY, 95])
        buffer.tofile(outname)

    return res1, res2


# Find all sub dir recursively under dirname and create new under dir_up
def mkdir_recursive(dirname: str, newdir: Path):
    for name in glob.glob(str(Path(dirname) / "**"), recursive=True):
        if Path(name).is_dir():
            # Find relative path from name to dirname.
            subdir_only = Path(name).relative_to(Path(dirname))
            # create new subdir of newdir / subdir
            newdir_subdir = newdir / subdir_only
            newdir_subdir.mkdir(exist_ok=True)
            print("Create subdir: ", str(newdir_subdir))


# Process dir using glob.
def upscayl_dir(dirname, model_name):
    # Create _up dir
    upscale_dir = Path(dirname + "_up")
    upscale_dir.mkdir(exist_ok=True)

    # Create all subdir one by one follow dirname to upscale_dir
    mkdir_recursive(dirname, upscale_dir)

    name_list = (
        glob.glob(str(Path(dirname) / "**" / "*.jpg"), recursive=True)
        + glob.glob(str(Path(dirname) / "**" / "*.jpeg"), recursive=True)
        + glob.glob(str(Path(dirname) / "**" / "*.png"), recursive=True)
        + glob.glob(str(Path(dirname) / "**" / "*.bmp"), recursive=True)
        + glob.glob(str(Path(dirname) / "**" / "*.tif"), recursive=True)
        + glob.glob(str(Path(dirname) / "**" / "*.tiff"), recursive=True)
    )

    for name in name_list:
        # For each image under dirname and its subfolders,
        # create one name under upscayl_dir with same prefix and _x4.jpg extension.
        # name_only = Path(name).name
        # name relative to dirname
        name_only = Path(name).relative_to(Path(dirname))
        outname = str(upscale_dir / name_add_x4(str(name_only)))

        print(name, " => ", outname)
        res = run_upscayl_one(name, outname, args.model)
        # print(res[0].stdout)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Call upscayl-bin to process subfolders recursively"
    )

    parser.add_argument(
        "-i", "--inname", type=str, default="", help="Input image or dir name"
    )
    parser.add_argument(
        "-m", "--model", type=str, default="ultrasharp-4x", help="Input model name"
    )

    args = parser.parse_args()
    if args.inname == "":
        print("No input image.")
        exit(1)

    if Path(args.inname).is_file():
        # Upscale an image.
        res = run_upscayl_one(args.inname, name_add_x4(args.inname), args.model)
        print(res[0].stdout)
    elif Path(args.inname).is_dir():
        # Upscale all images under the folder inname.
        upscayl_dir(args.inname, args.model)
