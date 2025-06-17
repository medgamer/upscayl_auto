@echo on

IF [%1] == [] (
	echo Need input folder name
	exit /b 1
)

echo Run upscayl-bin to process one folder.

set "dirname=%1"
set "outdir=%~1_up"
mkdir "%outdir%"

echo %outdir%

for %%f in (%dirname%\*.jpg %dirname%\*.jpeg) do (

	echo Upscale "%%f"

	upscayl-bin -i "%%f" -o abc.jpg -n ultrasharp-4x

	djpeg -outfile tmp.ppm abc.jpg

	cjpeg -quality 95 -outfile "%outdir%\%%~nf_x4.jpg" tmp.ppm
	
)
