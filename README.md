Step 1: Prepare your SRM
1.	Put your SRM file somewhere easy to access, e.g., ~/Desktop/. and ensure the save file is named "save.srm"
	
2.	Let’s say your file is called save.srm.

⸻

Step 2: Create the Python script
	1.	Open TextEdit → make sure it’s in plain text mode (Format → Make Plain Text).
	2.	Paste this code:

  
	input_file = "save.srm"
	output_file = "save_swapped.srm"
	
	with open(input_file, "rb") as f:
	    data = f.read()
	
	swapped = bytearray()
	for i in range(0, len(data), 4):
	    word = data[i:i+4]
	    if len(word) == 4:
	        swapped.extend(word[::-1])  # reverse the 4-byte word
	    else:
	        swapped.extend(word)  # in case leftover bytes
	
	with open(output_file, "wb") as f:
	    f.write(swapped)
	
	print("Done. Saved to", output_file)

3.	Save it as swap_srm.py on your Desktop (or wherever your SRM is).

⸻

Step 3: Run the script
1.	Open Terminal.
2.	Navigate to your Desktop (or wherever your files are) using:

		cd ~/Desktop

3. Run the script:

		python3 swap_srm.py

•	If your Mac has Python 3 installed, it will create a new file called save_swapped.srm in the same folder.

⸻

✅ Step 4: Test
	•	Load save_swapped.srm in your emulator and see if it now reads correctly.
