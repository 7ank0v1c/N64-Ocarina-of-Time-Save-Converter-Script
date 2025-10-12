input_file = "save.eep"
output_file = "save_swapped.eep"

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
