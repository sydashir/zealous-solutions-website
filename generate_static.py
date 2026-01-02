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
    
    # Routes to generate - filename must match the URL for GitHub Pages
    routes = [
        ('/', 'index.html'),
        ('/about', 'about.html'),
        ('/services', 'services.html'),
        ('/contact', 'contact.html'),
        ('/request-quote', 'request-quote.html'),
        ('/industries', 'industries.html'),
        ('/services/inbound', 'services/inbound.html'),
        ('/services/outbound', 'services/outbound.html'),
        ('/services/data-scrubbing', 'services/data-scrubbing.html'),
        ('/services/website-development', 'services/website-development.html'),
        ('/services/software-development', 'services/software-development.html'),
        ('/services/digital-marketing', 'services/digital-marketing.html'),
        ('/industries/healthcare', 'industries/healthcare.html'),
        ('/industries/insurance', 'industries/insurance.html'),
        ('/industries/real-estate', 'industries/real-estate.html'),
        ('/industries/information-technology', 'industries/information-technology.html'),
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
                    
                    # Fix internal navigation links for GitHub Pages (add .html extension)
                    # Root level pages
                    html_content = html_content.replace('href="/about"', 'href="about.html"')
                    html_content = html_content.replace('href="/services"', 'href="services.html"')
                    html_content = html_content.replace('href="/contact"', 'href="contact.html"')
                    html_content = html_content.replace('href="/request-quote"', 'href="request-quote.html"')
                    html_content = html_content.replace('href="/industries"', 'href="industries.html"')
                    html_content = html_content.replace('href="/"', 'href="index.html"')
                    
                    # Service pages
                    html_content = html_content.replace('href="/services/inbound"', 'href="services/inbound.html"')
                    html_content = html_content.replace('href="/services/outbound"', 'href="services/outbound.html"')
                    html_content = html_content.replace('href="/services/data-scrubbing"', 'href="services/data-scrubbing.html"')
                    html_content = html_content.replace('href="/services/website-development"', 'href="services/website-development.html"')
                    html_content = html_content.replace('href="/services/software-development"', 'href="services/software-development.html"')
                    html_content = html_content.replace('href="/services/digital-marketing"', 'href="services/digital-marketing.html"')
                    
                    # Industry pages
                    html_content = html_content.replace('href="/industries/healthcare"', 'href="industries/healthcare.html"')
                    html_content = html_content.replace('href="/industries/insurance"', 'href="industries/insurance.html"')
                    html_content = html_content.replace('href="/industries/real-estate"', 'href="industries/real-estate.html"')
                    html_content = html_content.replace('href="/industries/information-technology"', 'href="industries/information-technology.html"')
                    html_content = html_content.replace('href="/industries/financial"', 'href="industries/financial.html"')
                    
                    # Fix paths for subpages (add ../ prefix)
                    if depth > 0:
                        html_content = html_content.replace('href="about.html"', f'href="{prefix}about.html"')
                        html_content = html_content.replace('href="services.html"', f'href="{prefix}services.html"')
                        html_content = html_content.replace('href="contact.html"', f'href="{prefix}contact.html"')
                        html_content = html_content.replace('href="request-quote.html"', f'href="{prefix}request-quote.html"')
                        html_content = html_content.replace('href="industries.html"', f'href="{prefix}industries.html"')
                        html_content = html_content.replace('href="index.html"', f'href="{prefix}index.html"')
                        html_content = html_content.replace('href="services/', f'href="{prefix}services/')
                        html_content = html_content.replace('href="industries/', f'href="{prefix}industries/')
                    
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