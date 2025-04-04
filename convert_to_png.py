from cairosvg import svg2png
import os

# Create the output directory if it doesn't exist
os.makedirs('png_pfp', exist_ok=True)

# Convert all SVG files to PNG
for i in range(1, 6):
    svg_path = f'new_pfp/pfp{i}.svg'
    png_path = f'png_pfp/pfp{i}.png'
    
    if os.path.exists(svg_path):
        try:
            # Convert with transparent background and high resolution
            svg2png(url=svg_path, write_to=png_path, output_width=1000, output_height=1000)
            print(f"Converted {svg_path} to {png_path}")
        except Exception as e:
            print(f"Error converting {svg_path}: {e}")
    else:
        print(f"File not found: {svg_path}")

print("Conversion complete.")