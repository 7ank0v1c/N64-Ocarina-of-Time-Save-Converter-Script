**What is this?**


Here is a simple python script to run on MacOS to correctly convert your 'native N64' '.sra' save file for Ocarina of Time, one dumped from an actual genuine cart, to a workable save file with emulators such as OpenEmu and RetroArch.

I imagine this should also work on windows, but it is untested, let me know if it doesnt

Furthermore I imagine this will also work with some other N64 cart saves, ones that need byte swapping every 4 bytes, but I havents gotten around to testing this yet.
If you do test it, let me know =D


(This does not currently work with all emulators)


[This is only for .sra files and .srm files]

[This is not a tool which converts between the different formats, it simple makes the file of current save type, comptible, where otherwise it would not be]


**Tested and working on:**

OpenEmu (using Mupen64 Core) - '.sra' file type

RetroArch (using Mupen64 Core) - '.srm' file type


**Tested and 'not' currently working on:**

M64Plus FZ Pro (on android) - '.sra' file type


⸻


**PLEASE NOTE: 
ALWAYS MAKE A BACKUP OF YOUR SAVE BEFORE CONVERTING OR MESSING WITH IT IN ANYWAY**


⸻


Steps are almost identical, just ensure you use the correct script, depending on your current save file type


⸻


**PLEASE NOTE: 
ALWAYS MAKE A BACKUP OF YOUR SAVE BEFORE CONVERTING OR MESSING WITH IT IN ANYWAY**


⸻


**SRA Save Files:**

Step 1: Prepare your SRA

1.	Put your SRA file somewhere easy to access, e.g., ~/Desktop/.
	
2.	Ensure the save file is named "save.sra"

3.	Download and move the 'swap_sra.py' file to your Desktop (or wherever your SRA is). <a href="https://github.com/7ank0v1c/N64-Ocarina-of-Time-Save-Converter-Script/raw/main/Python%20Script/swap_sra.py" download>📥 Download swap_sra.py</a> (Right Click and click 'download linked file'

⸻

Step 2: Run the script

1.	Open Terminal.

2.	Navigate to your Desktop (or wherever your files are) using:

		cd ~/Desktop

3. Run the script:

		python3 swap_sra.py

•	If your Mac has Python 3 installed, it will create a new file called save_swapped.sra in the same folder.

⸻

✅ Step 4: Test

1. Rename your 'save_swapped.srm' file to the correct name for that save file

2. Copy the save to your emulator folder and load in your emulator and see if it now reads correctly.


⸻

**PLEASE NOTE: 
ALWAYS MAKE A BACKUP OF YOUR SAVE BEFORE CONVERTING OR MESSING WITH IT IN ANYWAY**

⸻

SRM Save Files:

Step 1: Prepare your SRM

1.  If needed you can convert your save to SRM using this tool: https://github.com/drehren/ramp64-convert-gui

2.	Put your SRM file somewhere easy to access, e.g., ~/Desktop/.
	
3.	Ensure the save file is named "save.srm"

4.	Download and move the 'swap_srm.py' file to your Desktop (or wherever your SRM is) <a href="https://github.com/7ank0v1c/N64-Ocarina-of-Time-Save-Converter-Script/raw/main/Python%20Script/swap_srm.py" download>📥 Download swap_srm.py</a> (Right Click and click 'download linked file'

⸻

Step 2: Run the script

1.	Open Terminal.

2.	Navigate to your Desktop (or wherever your files are) using:

		cd ~/Desktop

3. Run the script:

		python3 swap_srm.py

•	If your Mac has Python 3 installed, it will create a new file called save_swapped.srm in the same folder.

⸻

✅ Step 4: Test

1. Rename your 'save_swapped.srm' file to the correct name for that save file

2. Copy the save to your emulator folder and load in your emulator and see if it now reads correctly.
