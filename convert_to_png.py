from cairosvg import svg2png
import os

# Create the output directory if it doesn't exist
os.makedirs('png_pfp', exist_ok=True)

# Get all SVG files in the new_pfp directory
svg_files = [f for f in os.listdir('new_pfp') if f.endswith('.svg')]

# Convert all SVG files to PNG
for svg_file in svg_files:
    svg_path = f'new_pfp/{svg_file}'
    png_path = f'png_pfp/{svg_file.replace(".svg", ".png")}'
    
    try:
        # Convert with transparent background and high resolution
        svg2png(url=svg_path, write_to=png_path, output_width=1000, output_height=1000)
        print(f"Converted {svg_path} to {png_path}")
    except Exception as e:
        print(f"Error converting {svg_path}: {e}")

# Also convert the improved_pfp.svg if it exists
if os.path.exists('improved_pfp.svg'):
    try:
        svg2png(url='improved_pfp.svg', write_to='improved_pfp.png', output_width=1000, output_height=1000)
        print(f"Converted improved_pfp.svg to improved_pfp.png")
    except Exception as e:
        print(f"Error converting improved_pfp.svg: {e}")

print("Conversion complete.")