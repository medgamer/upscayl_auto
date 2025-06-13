# upscayl_auto
Run cmdline to call upscayl-bin to AI upscale images automatically.

2025.0613.	Created this new repository.

	Added upscayl zip. Added batch scripts and models list. Added jpeg subfolder with cjpeg.exe and djpeg.exe.
	
	Batch scripts can run on Windows with folders and filenames containing spaces " ".
	
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
	
	