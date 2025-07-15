@echo off

IF [%1] == [] (
	echo Need input folder name
	exit /b 1
)

echo Run pdf2jpegs.py to process all subfolders.

set "dirname=%1"

@echo on

for /d %%i in (%dirname%\*) do (

	echo Working on subdir %%i

	for %%f in ("%%i"\*.pdf) do (

		echo Process "%%f"

		python pdf2jpegs.py -i "%%f"

	)

)
