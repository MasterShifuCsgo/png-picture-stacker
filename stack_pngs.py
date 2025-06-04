from PIL import Image

# Load all images (in stacking order: 1.png is top, 21.png is bottom)
file_names = [f"{i}.png" for i in range(1, 22)]
images = [Image.open(name).convert("RGBA") for name in file_names]

# Ensure all images are the same width; resize if needed
width = max(img.width for img in images)
images = [img if img.width == width else img.resize((width, img.height)) for img in images]

# Calculate total height
total_height = sum(img.height for img in images)

# Create a blank canvas to paste onto
stacked_image = Image.new("RGBA", (width, total_height))

# Paste each image one after another vertically
y_offset = 0
for img in images:
    stacked_image.paste(img, (0, y_offset), mask=img)
    y_offset += img.height

# Save the result
stacked_image.save("stacked_vertical.png")
print("Saved as stacked_vertical.png")
