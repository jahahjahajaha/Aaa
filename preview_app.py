from flask import Flask, render_template, send_from_directory, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Count SVG files in new_pfp folder
    svg_count = 0
    if os.path.exists('new_pfp'):
        svg_count = len([f for f in os.listdir('new_pfp') if f.endswith('.svg')])
    
    # Count PNG files in png_pfp folder
    png_count = 0
    if os.path.exists('png_pfp'):
        png_count = len([f for f in os.listdir('png_pfp') if f.endswith('.png')])
    
    # Add the improved PFP
    has_improved = os.path.exists('improved_pfp.svg')
    
    return render_template('preview.html', svg_count=svg_count, png_count=png_count, has_improved=has_improved)

@app.route('/svg/<filename>')
def serve_svg(filename):
    return send_from_directory('new_pfp', filename)

@app.route('/png/<filename>')
def serve_png(filename):
    return send_from_directory('png_pfp', filename)

@app.route('/improved_pfp.svg')
def serve_improved_pfp():
    return send_file('improved_pfp.svg')

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Create templates/preview.html
    with open('templates/preview.html', 'w') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KnarliX Profile Pictures</title>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
            margin: 0;
            padding: 20px;
        }
        h1, h2 {
            color: #bb86fc;
            text-align: center;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .pfp-card {
            background-color: #1e1e1e;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            text-align: center;
        }
        .pfp-card h3 {
            margin-top: 10px;
            color: #03dac6;
        }
        .pfp-card img {
            width: 100%;
            height: auto;
            border-radius: 5px;
            background-color: transparent;
        }
        .format-section {
            margin-bottom: 40px;
        }
        .download-btn {
            display: inline-block;
            background-color: #bb86fc;
            color: #000000;
            padding: 8px 16px;
            border-radius: 4px;
            text-decoration: none;
            margin-top: 10px;
            font-weight: bold;
        }
        .download-btn:hover {
            background-color: #9c64fc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>KnarliX Profile Pictures</h1>
        <p style="text-align: center;">A collection of modern, gaming and developer-themed profile pictures.</p>
        
        <div class="format-section">
            <h2>SVG Format ({{ svg_count }})</h2>
            <div class="gallery">
                {% for i in range(1, svg_count + 1) %}
                <div class="pfp-card">
                    <img src="/svg/pfp{{ i }}.svg" alt="Profile Picture {{ i }} (SVG)">
                    <h3>Profile {{ i }}</h3>
                    <p>Vector format with transparent background</p>
                    <a href="/svg/pfp{{ i }}.svg" download class="download-btn">Download SVG</a>
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div class="format-section">
            <h2>PNG Format ({{ png_count }})</h2>
            <div class="gallery">
                {% for i in range(1, png_count + 1) %}
                <div class="pfp-card">
                    <img src="/png/pfp{{ i }}.png" alt="Profile Picture {{ i }} (PNG)">
                    <h3>Profile {{ i }}</h3>
                    <p>High-resolution PNG with transparency</p>
                    <a href="/png/pfp{{ i }}.png" download class="download-btn">Download PNG</a>
                </div>
                {% endfor %}
            </div>
        </div>
        
        {% if has_improved %}
        <div class="format-section">
            <h2>Improved Profile Picture</h2>
            <div class="gallery">
                <div class="pfp-card" style="grid-column: span 2;">
                    <img src="/improved_pfp.svg" alt="Improved Profile Picture" style="max-width: 500px; margin: 0 auto;">
                    <h3>Enhanced KnarliX PFP</h3>
                    <p>Enhanced futuristic design with improved effects and a more vibrant color scheme</p>
                    <a href="/improved_pfp.svg" download class="download-btn">Download SVG</a>
                </div>
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>''')
    
    app.run(host='0.0.0.0', port=5000)