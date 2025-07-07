import argparse
import subprocess
from pathlib import Path
import glob
import cv2


# Detect whether input name having png extension.
def is_png(inname):
    ext = Path(inname).suffix
    if ext == ".png" or ext == ".PNG" or ext == ".Png":
        return True
    else:
        return False


def png_2_jpg(inname, jpgname):
    img = cv2.imread(inname)
    cv2.imwrite(jpgname, img)
    return jpgname


# Add and replace extension to "_x4.jpg"
def name_add_x4(inname):
    file_path = Path(inname)
    outname = str(file_path.stem) + "_x4.jpg"
    return outname


# Call upscayl-bin on one image
def run_upscayl_one(inname, outname, model_name):

    # Call png2jpg first if input is a png file.
    if is_png(inname):
        jpgname = "xyz.jpg"
        png_2_jpg(inname, jpgname)
        inname = jpgname

    cmd_list = ["upscayl-bin", "-i", inname, "-o", "abc.jpg", "-n", model_name]
    # Basic execution
    res1 = subprocess.run(cmd_list)

    djpeg_list = ["djpeg", "-outfile", "tmp.ppm", "abc.jpg"]
    res2 = subprocess.run(djpeg_list)

    cjpeg_list = ["cjpeg", "-quality", "95", "-outfile", outname, "tmp.ppm"]
    res3 = subprocess.run(cjpeg_list)

    return res1, res2, res3


# Process dir using glob
def upscayl_dir(dirname, model_name):
    # Create _up dir
    upscale_dir = Path(dirname + "_up")
    upscale_dir.mkdir(exist_ok=True)

    name_list = (
        glob.glob(str(Path(dirname) / "*.jpg"))
        + glob.glob(str(Path(dirname) / "*.jpeg"))
        + glob.glob(str(Path(dirname) / "*.png"))
    )
    for name in name_list:
        name_only = Path(name).name
        outname = str(upscale_dir / name_add_x4(name_only))

        res = run_upscayl_one(name, outname, args.model)
        print(res[0].stdout)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Call upscayl-bin to process subfolders"
    )

    parser.add_argument("--inname", type=str, default="", help="Input image name")
    parser.add_argument(
        "--model", type=str, default="ultrasharp-4x", help="Input model name"
    )

    args = parser.parse_args()
    if args.inname == "":
        print("No input image.")
        exit(1)

    if Path(args.inname).is_file():
        res = run_upscayl_one(args.inname, name_add_x4(args.inname), args.model)
        print(res[0].stdout)
    elif Path(args.inname).is_dir():
        upscayl_dir(args.inname, args.model)
