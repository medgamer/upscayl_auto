@echo off

setlocal enabledelayedexpansion

IF [%1] == [] (
	echo Need input folder name
	exit /b 1
)

echo Run upscayl-bin to process one folder.

set "dirname=%1"
set "outdir=%~1_up"
mkdir "%outdir%"

@echo on

echo %outdir%

for /d %%i in (%dirname%\*) do (

	echo Create new subfolder %outdir%\%%~nxi
	mkdir "%outdir%\%%~nxi"
	echo Working on subdir %%i to output %outdir%\%%~nxi

	REM use loop index to handle UNICODE name output ;-)
	set ind=0
	for %%f in ("%%i"\*.jpg "%%i"\*.jpeg) do (

		set /A ind=ind+1
		echo Upscale "%%f" to !ind!

		upscayl-bin -i "%%f" -o abc.jpg -n ultrasharp-4x

		djpeg -outfile tmp.ppm abc.jpg

		cjpeg -quality 95 -outfile "%outdir%\%%~nxi\chn_"!ind!_x4.jpg tmp.ppm
	
	)

)

