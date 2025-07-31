# upscayl_auto
Run cmdline to call upscayl-bin to AI upscale images automatically.

============================================================================================================

Prior steps before running any batch scripts or python programs.

1. Checkout this repository and run "create_bin.bat" to extract exe + model files into ~\bin folder (about 500 MB).

2. Add ~\bin full path and ~\jpeg full path to system user environment path.

3. Test 3 exe can run properly

	Open cmd terminal
	
	upscayl-bin         Should show help messages
	
	cjpeg				Ctr-C should exit.
	
	djpeg				Ctr-C should exit.

4. For python program.

	Install python 3.11.9 here. 
	
	python 3.12 and 3.13 is NOT ready for deep learning stuff ;-)
	
	https://www.python.org/downloads/windows/
	

	py -0p        Show installed python versions.
	
	py -3.11 -m venv C:\my_venv          Create python venv environment
	
	C:\my_venv\scripts\activate.bat		 Activate python venv
	
	pip list

	python.exe -m pip install --upgrade pip

	cd into ~\upscayl_auto\ folder
	
	pip install -r requirements.txt
	
	cd into ~\upscayl_auto\python folder
	
	Run 
	
	python upscayl_dirs.py -h        Show help messages


5. classify_dir.py usage.

	python classify_dir.py -h        Show help messages

	python classify_dir.py -i dirname        Classify jpeg images in "dirname" and move into subfolders by class labels.


============================================================================================================

2025.0731.

	Added subfolder ~\hacker_rank with interview mock test (day 1 and day 2) codes cpp files and pdf reports ;-)

2025.0723.

	Added option --recursive to make classify_dir.py classify all images recursively in a folder with duplicate file name detection and rename using uuid.
	
2025.0722.

	Fixed classify_dir.py to read and convert grayscale image to color RGB correctly.
	Added and fixed req_freeze.txt to use "pip install -r req_freeze.txt" without red error conflicts.

2025.0721.

	Added new python program classify_dir.py to use keras model and imagenet labels to classify images in a folder and move into subfolders.
	requirements.txt is updated.

2025.0715.

	Make pdf2jpegs.py parse command line -i pdfname.
	Added batch script do_pdf2jpegs_subdirs.bat to run to process all pdf files in subfolders of a main folder.
	
	Added requirements.txt for "pip install -r ". Updated Readme.md.

2025.0714.

	Added new python file pdf2jpegs.py to extract images from a pdf file.
	We need to install poppler binary first and add its bin to path.
	Then install
	
	pip install img2pdf pdf2image
	

2025.0712.

	Fixed unicode folder and file name support using cv2.imencode().

2025.0711.

	Added bmp and tif images support with various extensions. Output upscayled images are always jpeg files with extension ".jpg".

2025.0710.

	Added batch script ~\python\py311_activate.bat to activate python venv.
	Changed python program to use cv2.imread() and cv2.imwrite() to replace cjpeg and djpeg to speed up a little.
	
	
2025.0709.

	Added subfolder ~\bin_split to store 7zip split bin files and batch script to create ~\bin automatically.
	Please install 7zip first and add 7zip installed path to system user environment path.
	

2025.0708.

	Added recursive subfolder support if input -i is a folder name.
	The program can create all subfolders under ~/?_up/ same as source folder and upscale image into it.

2025.0707.

	Added python program ~/python/upscayl_dirs.py to upscale one image file or one folder.
	It can detect and convert png file to jpg automatically and can handle Windows file names containg spaces.
	
	Python packages needed:  opencv-python, argparse, pathlib (subprocess and glob are part of python).
	
	Command line syntax:	(Output image name will be input image name prefix _x4.jpg)
	
	python upscayl_dirs.py -h		Help
	
	python upscayl_dirs.py --inname image.jpg --model model_name (default is ultrasharp-4x if not specified)
	
	python upscayl_dirs.py --inname dirname
	
	python upscayl_dirs.py --inname "image 123.jpg"
	
	python upscayl_dirs.py --inname "screenshot (80).png"
	

2025.0621.

	Added new batch script do_upscayl_subdirs_jpeg_rename.bat to deal with UNICODE file names
	to output numberred image names using batch delayed expansion with index variable.

2025.0617.

	Added new batch script to upscale 2 (option -z 2) using animv3-x2 model.
	It is useful to upscale HD and larger images x 2 with pixels >=1600 to match 4K monitor resolution 3840 x 2160.
	
	Tests show that option -z only works with corresponding model with special scales.
	For example, regular *x4 model with -z 2 will get artifacts ;-)


2025.0613.	Created this new repository.

	Added batch scripts and models list. Added jpeg subfolder with cjpeg.exe and djpeg.exe.
	
	Batch scripts can run on Windows with folders and filenames containing spaces " ".
	
	Added djpeg and cjpeg in 2 batch scripts to do jpg => ppm => jpg (qulity=95) conversion.
	It can save 50% file size and disk space.

	
	1. Best models tested so far:
	
	ultrasharp-4x	
		Default choice for >=1000 pixels images. Speed is medium.
	
	RealESRGAN_General_x4_v3	
		Default choice for <1000 pixel images. Speed is fast.
		
	realesr-animevideov3-x4
		Very fast with OK quality.
		
	realsr_jpeg
		Good for jpeg artifacts reduce. Speed is medium.
		
	2. upscayl-bin supported output image format = jpeg, png and webp.
	
	jpeg quality is 100 => file very large.
	
	djpeg outputs to *.ppm by default.
	
	cjpeg read *.ppm and outputs to *.jpg.
	
	