"""
Flask to Static Site Generator for GitHub Pages
This script converts your Flask app to static HTML files for GitHub Pages deployment
"""

import os
import sys
from urllib.parse import urljoin
from flask import Flask

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

from app import app

def generate_static_site():
    """Generate static HTML files from Flask routes"""
    
    # Create docs directory for GitHub Pages
    output_dir = 'docs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Copy static files
    import shutil
    static_source = 'static'
    static_dest = os.path.join(output_dir, 'static')
    
    if os.path.exists(static_dest):
        shutil.rmtree(static_dest)
    shutil.copytree(static_source, static_dest)
    
    # Routes to generate
    routes = [
        ('/', 'index.html'),
        ('/about', 'about.html'),
        ('/services', 'services.html'),
        ('/contact', 'contact.html'),
        ('/request-quote', 'request_quote.html'),
        ('/industries', 'industries.html'),
        ('/services/inbound', 'services/inbound.html'),
        ('/services/outbound', 'services/outbound.html'),
        ('/services/data-scrubbing', 'services/data_scrubbing.html'),
        ('/services/website-development', 'services/website_development.html'),
        ('/services/software-development', 'services/software_development.html'),
        ('/services/digital-marketing', 'services/digital_marketing.html'),
        ('/industries/healthcare', 'industries/healthcare.html'),
        ('/industries/insurance', 'industries/insurance.html'),
        ('/industries/real-estate', 'industries/real_estate.html'),
        ('/industries/information-technology', 'industries/it.html'),
        ('/industries/financial', 'industries/financial.html'),
    ]
    
    # Generate static files
    with app.test_client() as client:
        for route, filename in routes:
            try:
                response = client.get(route)
                if response.status_code == 200:
                    # Create subdirectories if needed
                    file_path = os.path.join(output_dir, filename)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    
                    # Get HTML content and fix asset paths for GitHub Pages
                    html_content = response.get_data(as_text=True)
                    
                    # Fix asset paths
                    html_content = html_content.replace('href="/static/', 'href="static/')
                    html_content = html_content.replace('src="/static/', 'src="static/')
                    
                    # Fix relative paths based on directory depth
                    depth = filename.count('/')
                    if depth > 0:
                        prefix = '../' * depth
                        html_content = html_content.replace('href="static/', f'href="{prefix}static/')
                        html_content = html_content.replace('src="static/', f'src="{prefix}static/')
                    
                    # Write HTML content
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    print(f"Generated: {filename}")
                else:
                    print(f"Error generating {filename}: {response.status_code}")
            except Exception as e:
                print(f"Error generating {filename}: {e}")
    
    print(f"\nStatic site generated in '{output_dir}' directory")
    print("Ready for GitHub Pages deployment!")

if __name__ == "__main__":
    generate_static_site()