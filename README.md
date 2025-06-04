🧩 PNG Vertical Stack Script
This script stacks multiple .png images vertically into a single tall image, preserving transparency. It’s useful for combining layered graphics, game sprites, or vertically aligned visual elements.

🔧 What It Does
Loads images named 1.png through 21.png

Ensures all images have the same width (resizing if needed)

Stacks them from top (1.png) to bottom (21.png)

Saves the final result as stacked_vertical.png

▶️ Usage
Place your 1.png to 21.png files in the same folder as the script.

Install Pillow if you haven't:

bash
Copy
Edit
pip install pillow
Run the script:

bash
Copy
Edit
python stack_images.py
The result will be saved as stacked_vertical.png.

📌 Notes
All PNGs should ideally have the same width for best results.

Transparency is preserved (RGBA mode).

You can change the file range or modify the stacking order by adjusting the file_names list.

