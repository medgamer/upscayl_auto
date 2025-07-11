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

	py -0p        Show installed python versions.
	
	py -3.11 -m venv C:\my_venv          Create python venv environment
	
	C:\my_venv\scripts\activate.bat		 Activate python venv
	
	pip list    (and upgrade pip to latest version follow cmdline messages).
	
	cd into ~\upscayl_auto\python folder
	
	Run 
	
	python upscayl_dirs.py -h        Show help messages



============================================================================================================

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
	
	