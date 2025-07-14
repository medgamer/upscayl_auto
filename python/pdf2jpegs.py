from pdf2image import convert_from_path

# Example 2: Convert a PDF to a list of PIL images and save to a folder
def pdf_to_jpegs(pdf_name, outpath):
    images = convert_from_path(pdf_name, output_folder=outpath, fmt="jpeg")


pdf_to_jpegs("wallpaper.pdf", "wallpaper")
