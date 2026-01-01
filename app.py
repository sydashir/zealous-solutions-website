"""
Zealous Solutions - Professional Call Centre Website
Flask Backend Application

This Flask app handles:
- Contact form submissions
- Email notifications
- Database storage
- Professional deployment ready

Requirements:
- Flask
- Flask-Mail
- Flask-SQLAlchemy (optional for database)
- Flask-WTF (for form validation)

Installation:
pip install flask flask-mail flask-sqlalchemy flask-wtf

For production deployment, also install:
pip install gunicorn
"""

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_mail import Mail, Message
from datetime import datetime
import os
import logging

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['DEBUG'] = False  # Set to False in production
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-in-production')

# Email Configuration (Use environment variables in production)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', True)
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'Obsyed1217@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'your-app-password')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'Obsyed1217@gmail.com')

# Initialize extensions
mail = Mail(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    """Main homepage route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About us page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact us page"""
    return render_template('contact.html')

@app.route('/request-quote')
def request_quote():
    """Request a quote page"""
    return render_template('request_quote.html')

# Service Routes
@app.route('/services')
def services():
    """Main services page"""
    return render_template('services.html')

@app.route('/services/inbound')
def inbound_services():
    """Inbound call center services"""
    return render_template('services/inbound.html')

@app.route('/services/outbound')
def outbound_services():
    """Outbound call center services"""
    return render_template('services/outbound.html')

@app.route('/services/data-scrubbing')
def data_scrubbing():
    """Data cleansing services"""
    return render_template('services/data_scrubbing.html')

@app.route('/services/software-development')
def software_development():
    """Software development services"""
    return render_template('services/software_development.html')

@app.route('/services/digital-marketing')
def digital_marketing():
    """Digital marketing services"""
    return render_template('services/digital_marketing.html')

@app.route('/services/website-development')
def website_development():
    """Website development services"""
    return render_template('services/website_development.html')

# Industry Routes
@app.route('/industries')
def industries():
    """Industries we serve"""
    return render_template('industries.html')

@app.route('/industries/insurance')
def insurance_industry():
    """Insurance industry services"""
    return render_template('industries/insurance.html')

@app.route('/industries/healthcare')
def healthcare_industry():
    """Healthcare industry services"""
    return render_template('industries/healthcare.html')

@app.route('/industries/financial')
def financial_industry():
    """Financial services industry"""
    return render_template('industries/financial.html')

@app.route('/industries/real-estate')
def real_estate_industry():
    """Real estate industry services"""
    return render_template('industries/real_estate.html')

@app.route('/industries/information-technology')
def it_industry():
    """IT industry services"""
    return render_template('industries/it.html')

# Legal and Policy Routes
@app.route('/privacy-policy')
def privacy_policy():
    """Privacy policy page"""
    return render_template('privacy_policy.html')

@app.route('/terms-conditions')
def terms_conditions():
    """Terms and conditions page"""
    return render_template('terms_conditions.html')

@app.route('/sitemap')
def sitemap():
    """Sitemap page"""
    return render_template('sitemap.html')

@app.route('/submit-quote', methods=['POST'])
def submit_quote():
    """Handle contact form submissions"""
    try:
        # Get form data
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        company = request.form.get('company', '').strip()
        service = request.form.get('service', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not all([first_name, last_name, email, phone, company, service]):
            return jsonify({
                'success': False, 
                'message': 'Please fill in all required fields.'
            }), 400
        
        # Create email content
        email_content = f"""
        New Quote Request - Zealous Solutions
        
        Contact Information:
        - Name: {first_name} {last_name}
        - Email: {email}
        - Phone: {phone}
        - Company: {company}
        - Service Interest: {service}
        
        Message:
        {message}
        
        Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        # Send email notification
        msg = Message(
            subject=f'New Quote Request from {first_name} {last_name}',
            recipients=['Obsyed1217@gmail.com', 'info@zealous-solutions.com'],  # Your business emails
            body=email_content
        )
        
        mail.send(msg)
        
        # Log successful submission
        logger.info(f"Quote request submitted by {email} from {company}")
        
        # Send confirmation email to client
        confirmation_msg = Message(
            subject='Thank you for contacting Zealous Solutions',
            recipients=[email],
            body=f"""
            Dear {first_name},
            
            Thank you for your interest in Zealous Solutions call centre services!
            
            We have received your quote request and will get back to you within 24 hours.
            
            Your request details:
            - Service: {service}
            - Company: {company}
            
            Best regards,
            Zealous Solutions Team
            Phone: +923070088630
            Website: www.Z4zealous.com
            """
        )
        
        mail.send(confirmation_msg)
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your inquiry! We will contact you within 24 hours.'
        })
        
    except Exception as e:
        logger.error(f"Error processing quote request: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Sorry, there was an error processing your request. Please try again.'
        }), 500

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    """Handle general contact form submissions"""
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not all([name, email, message]):
            return jsonify({
                'success': False, 
                'message': 'Please fill in all required fields.'
            }), 400
        
        # Create email content
        email_content = f"""
        New Contact Message - Zealous Solutions
        
        Contact Information:
        - Name: {name}
        - Email: {email}
        - Phone: {phone}
        - Subject: {subject}
        
        Message:
        {message}
        
        Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        # Send email notification
        msg = Message(
            subject=f'Contact Form: {subject}' if subject else f'Contact from {name}',
            recipients=['Obsyed1217@gmail.com', 'info@zealous-solutions.com'],
            body=email_content
        )
        
        mail.send(msg)
        
        logger.info(f"Contact form submitted by {email}")
        
        return jsonify({
            'success': True,
            'message': 'Thank you for contacting us! We will get back to you soon.'
        })
        
    except Exception as e:
        logger.error(f"Error processing contact form: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Sorry, there was an error sending your message. Please try again.'
        }), 500

@app.route('/api/contact', methods=['POST'])
def api_contact():
    """API endpoint for contact form (for AJAX requests)"""
    return submit_quote()

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=5000)