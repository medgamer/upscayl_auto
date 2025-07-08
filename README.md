# upscayl_auto
Run cmdline to call upscayl-bin to AI upscale images automatically.

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

	Added upscayl zip. Added batch scripts and models list. Added jpeg subfolder with cjpeg.exe and djpeg.exe.
	
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
	
	