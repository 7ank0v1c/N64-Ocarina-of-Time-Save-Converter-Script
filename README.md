What is this?

Here is a simple python script to run on MacOS to correctly convert your 'native N64' '.sra' save file, one dumped from an actual genuine cart, to a workable save file with emulators
(This does not currently work with all emulators)

Currently this is only for .sra files and .srm files

Tested and working on:
OpenEmu (using Mupen64 Core) - '.sra' file type
RetroArch (using Mupen64 Core) - '.srm' file type

Tested and not currently working on:
M64Plus FZ Pro (on android) - '.sra' file type

SRA Save Files:
Step 1: Prepare your SRA
1.	Put your SRA file somewhere easy to access, e.g., ~/Desktop/.
	
2.	Ensure the save file is named "save.sra"

3.	Download and move the 'swap_sra.py' file to your Desktop (or wherever your SRA is).

⸻

Step 2: Run the script
1.	Open Terminal.
2.	Navigate to your Desktop (or wherever your files are) using:

		cd ~/Desktop

3. Run the script:

		python3 swap_srm.py

•	If your Mac has Python 3 installed, it will create a new file called save_swapped.sra in the same folder.

⸻

✅ Step 4: Test
1. Rename your 'save_swapped.srm' file to the correct name for that save file
2. Copy the save to your emulator folder and load in your emulator and see if it now reads correctly.


⸻


SRM Save Files:
Step 1: Prepare your SRM
1.	Put your SRM file somewhere easy to access, e.g., ~/Desktop/.
	
2.	Ensure the save file is named "save.srm"

3.	Download and move the 'swap_srm.py' file to your Desktop (or wherever your SRM is).

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
