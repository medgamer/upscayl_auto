import argparse
from pathlib import Path
from pdf2image import convert_from_path

# Example 2: Convert a PDF to a list of PIL images and save to a folder
def pdf_to_jpegs(pdf_name):
    # Create new dir using pdf file name without extension.
    file_path = Path(pdf_name)
    file_noext = file_path.parent / file_path.stem
    outdir = file_noext
    outdir.mkdir(exist_ok=True)
    print("Create subdir: ", str(outdir))

    images = convert_from_path(pdf_name, output_folder=str(outdir), fmt="jpeg")
    print(f"From {pdf_name} total {len(images)} images extracted.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Use pdf2image to extract images from a pdf file."
    )

    parser.add_argument(
        "-i", "--inname", type=str, default="", help="Input pdf file name"
    )

    args = parser.parse_args()
    if (args.inname == "") or (".pdf" not in args.inname):
        print("No input pdf file.")
        exit(1)

    pdf_to_jpegs(args.inname)
