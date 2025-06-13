@echo off

IF [%1] == [] (
	echo Need input folder name
	exit /b 1
)

echo Run upscayl-bin to process one folder.

set "dirname=%1"
set "outdir=%~1_up"
mkdir %outdir%

@echo on

echo %outdir%

for /d %%i in (%dirname%\*) do (

	echo Create new subfolder %outdir%\%%~nxi
	mkdir "%outdir%\%%~nxi"
	echo Working on subdir %%i to output %outdir%\%%~nxi
	
	for %%f in ("%%i"\*.jpg) do (
	
		echo Upscale "%%f"

		upscayl-bin -i "%%f" -o "%outdir%\%%~nxi\%%~nf_x4.jpg" -n ultrasharp-4x
	
	)

)

