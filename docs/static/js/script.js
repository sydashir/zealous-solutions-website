// Optimized Mobile Navigation with event delegation
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const body = document.body;

// Single event listener for hamburger
if (hamburger && navMenu) {
    hamburger.addEventListener('click', (e) => {
        e.preventDefault();
        navMenu.classList.toggle('active');
        body.classList.toggle('menu-open');
    });

    // Event delegation for nav links
    navMenu.addEventListener('click', (e) => {
        if (e.target.classList.contains('nav-link')) {
            navMenu.classList.remove('active');
            body.classList.remove('menu-open');
        }
    });
}

// Optimized Smooth Scrolling with event delegation
document.addEventListener('click', (e) => {
    const link = e.target.closest('a[href^="#"]');
    if (link) {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const target = document.querySelector(targetId);
        
        if (target) {
            const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
            const targetPosition = target.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    }
});

// Optimized Services Tab Functionality with event delegation
const servicesTabContainer = document.querySelector('.services-tabs');

if (servicesTabContainer) {
    servicesTabContainer.addEventListener('click', (e) => {
        const button = e.target.closest('.tab-btn');
        if (!button) return;
        
        const tabId = button.getAttribute('data-tab');
        const targetContent = document.getElementById(tabId);
        
        if (targetContent) {
            // Remove active from all tabs and contents
            document.querySelectorAll('.tab-btn').forEach(btn => 
                btn.classList.remove('active')
            );
            document.querySelectorAll('.tab-content').forEach(content => 
                content.classList.remove('active')
            );
            
            // Add active to current tab and content
            button.classList.add('active');
            targetContent.classList.add('active');
            
            // Add futuristic glow effect
            button.style.boxShadow = '0 0 20px rgba(255, 107, 53, 0.5)';
            setTimeout(() => {
                button.style.boxShadow = '';
            }, 300);
        }
    });
}

// Testimonials Slider
const testimonials = document.querySelectorAll('.testimonial');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
let currentTestimonial = 0;

function showTestimonial(index) {
    testimonials.forEach((testimonial, i) => {
        testimonial.classList.remove('active');
        if (i === index) {
            testimonial.classList.add('active');
        }
    });
}

if (prevBtn && nextBtn) {
    prevBtn.addEventListener('click', () => {
        currentTestimonial = currentTestimonial === 0 ? testimonials.length - 1 : currentTestimonial - 1;
        showTestimonial(currentTestimonial);
    });

    nextBtn.addEventListener('click', () => {
        currentTestimonial = currentTestimonial === testimonials.length - 1 ? 0 : currentTestimonial + 1;
        showTestimonial(currentTestimonial);
    });

    // Auto-slide testimonials
    setInterval(() => {
        currentTestimonial = currentTestimonial === testimonials.length - 1 ? 0 : currentTestimonial + 1;
        showTestimonial(currentTestimonial);
    }, 5000);
}

// FAQ Accordion
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    
    question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        
        // Close all FAQ items
        faqItems.forEach(faqItem => {
            faqItem.classList.remove('active');
        });
        
        // Open clicked item if it wasn't active
        if (!isActive) {
            item.classList.add('active');
        }
    });
});

// Contact Form Submission with Flask Backend
const contactForm = document.querySelector('.quote-form');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Get submit button and show loading state
        const submitBtn = contactForm.querySelector('.submit-btn');
        const btnText = submitBtn.querySelector('.btn-text');
        const originalText = btnText.textContent;
        
        // Show loading state
        btnText.textContent = 'Submitting...';
        submitBtn.disabled = true;
        
        try {
            // Get form data
            const formData = new FormData(contactForm);
            
            // Send to Flask backend
            const response = await fetch('/submit-quote', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            
            if (result.success) {
                // Show success message with custom alert
                showCustomAlert('Success!', result.message, 'success');
                // Reset the form
                contactForm.reset();
            } else {
                // Show error message
                showCustomAlert('Error', result.message, 'error');
            }
            
        } catch (error) {
            console.error('Form submission error:', error);
            showCustomAlert('Error', 'Network error. Please check your connection and try again.', 'error');
        } finally {
            // Reset button state
            btnText.textContent = originalText;
            submitBtn.disabled = false;
        }
    });
}

// Custom Alert Function for better UX
function showCustomAlert(title, message, type) {
    // Remove existing alerts
    const existingAlert = document.querySelector('.custom-alert');
    if (existingAlert) {
        existingAlert.remove();
    }
    
    // Create alert element
    const alertDiv = document.createElement('div');
    alertDiv.className = `custom-alert alert-${type}`;
    alertDiv.innerHTML = `
        <div class="alert-content">
            <div class="alert-icon">
                <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-triangle'}"></i>
            </div>
            <div class="alert-text">
                <h4>${title}</h4>
                <p>${message}</p>
            </div>
            <button class="alert-close" onclick="this.parentElement.parentElement.remove()">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `;
    
    // Add to page
    document.body.appendChild(alertDiv);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (alertDiv && alertDiv.parentElement) {
            alertDiv.remove();
        }
    }, 5000);
}

// Back to Top Button
const backToTopBtn = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        backToTopBtn.classList.add('visible');
    } else {
        backToTopBtn.classList.remove('visible');
    }
});

backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Optimized Header Background on Scroll with throttling
const header = document.querySelector('.header');
let ticking = false;

function updateHeader() {
    const scrolled = window.scrollY > 50;
    
    if (scrolled) {
        header.style.background = 'rgba(255, 255, 255, 0.98)';
        header.style.backdropFilter = 'blur(20px)';
        header.style.borderBottom = '1px solid rgba(212, 175, 55, 0.4)';
    } else {
        header.style.background = 'rgba(255, 255, 255, 0.95)';
        header.style.backdropFilter = 'blur(20px)';
        header.style.borderBottom = '1px solid rgba(212, 175, 55, 0.3)';
    }
    
    ticking = false;
}

if (header) {
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(updateHeader);
            ticking = true;
        }
    }, { passive: true });
}

// Intersection Observer for Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
        }
    });
}, observerOptions);

// Observe elements for animation
document.querySelectorAll('.service-card, .feature-card, .industry-card').forEach(el => {
    observer.observe(el);
});

// Optimized CSS animations injection
const futuristicAnimations = `
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px) scale(0.95);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }
    
    @keyframes glowPulse {
        0%, 100% { 
            box-shadow: 0 0 20px rgba(255, 107, 53, 0.3); 
        }
        50% { 
            box-shadow: 0 0 30px rgba(255, 107, 53, 0.6); 
        }
    }
    
    @keyframes floatEffect {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    .service-card,
    .feature-card,
    .industry-card {
        opacity: 0;
        transform: translateY(40px) scale(0.95);
    }
    
    .floating-element {
        animation: floatEffect 3s ease-in-out infinite;
    }
`;

// Only inject styles once
if (!document.querySelector('#futuristic-animations')) {
    const style = document.createElement('style');
    style.id = 'futuristic-animations';
    style.textContent = futuristicAnimations;
    document.head.appendChild(style);
}

// Counter Animation for Stats
function animateCounter(element, target, duration = 2000) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        element.textContent = Math.floor(current);
        
        if (current >= target) {
            element.textContent = target;
            clearInterval(timer);
        }
    }, 16);
}

// Animate stats when they come into view
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const statNumber = entry.target.querySelector('h3');
            const targetValue = parseInt(statNumber.textContent);
            
            if (targetValue === 500) {
                animateCounter(statNumber, 500);
            } else if (targetValue === 24) {
                statNumber.textContent = '24/7';
            } else if (targetValue === 99) {
                animateCounter(statNumber, 99);
                setTimeout(() => {
                    statNumber.textContent = '99%';
                }, 2000);
            }
            
            statsObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.stat').forEach(stat => {
    statsObserver.observe(stat);
});

// Futuristic Loading Animation
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
    
    // Add floating elements after load
    setTimeout(addFloatingElements, 1000);
});

// Futuristic loading styles
const loadingStyles = `
    body:not(.loaded) {
        overflow: hidden;
    }
    
    body:not(.loaded)::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        animation: fadeOut 0.8s ease 1.2s forwards;
    }
    
    body:not(.loaded)::after {
        content: '';
        position: fixed;
        top: 50%;
        left: 50%;
        width: 60px;
        height: 60px;
        margin: -30px 0 0 -30px;
        border: 2px solid transparent;
        border-top: 2px solid #FF6B35;
        border-right: 2px solid #00D9FF;
        border-radius: 50%;
        animation: futuristicSpin 1.5s linear infinite;
        z-index: 10000;
        filter: drop-shadow(0 0 20px rgba(255, 107, 53, 0.5));
    }
    
    @keyframes futuristicSpin {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.1); }
        100% { transform: rotate(360deg) scale(1); }
    }
    
    @keyframes fadeOut {
        to {
            opacity: 0;
            visibility: hidden;
        }
    }
`;

// Only inject loading styles once
if (!document.querySelector('#loading-styles')) {
    const loadingStyleElement = document.createElement('style');
    loadingStyleElement.id = 'loading-styles';
    loadingStyleElement.textContent = loadingStyles;
    document.head.appendChild(loadingStyleElement);
}

// Add floating elements for futuristic effect
function addFloatingElements() {
    const hero = document.querySelector('.hero');
    if (hero) {
        for (let i = 0; i < 3; i++) {
            const floater = document.createElement('div');
            floater.className = 'floating-element';
            floater.style.cssText = `
                position: absolute;
                width: ${Math.random() * 100 + 50}px;
                height: ${Math.random() * 100 + 50}px;
                border: 1px solid rgba(255, 107, 53, 0.3);
                border-radius: 50%;
                top: ${Math.random() * 80}%;
                left: ${Math.random() * 80}%;
                pointer-events: none;
                animation-delay: ${Math.random() * 2}s;
                z-index: 0;
            `;
            hero.appendChild(floater);
        }
    }
}

// Handle Contact Form Submission
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            
            // Show loading state
            submitButton.textContent = 'Sending...';
            submitButton.disabled = true;
            
            try {
                const response = await fetch('/submit-contact', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                if (result.success) {
                    showAlert(result.message, 'success');
                    this.reset();
                } else {
                    showAlert(result.message, 'error');
                }
            } catch (error) {
                showAlert('Network error. Please try again.', 'error');
            } finally {
                submitButton.textContent = originalText;
                submitButton.disabled = false;
            }
        });
    }

    // Handle Multi-step Quote Form
    const quoteForm = document.getElementById('quoteForm');
    if (quoteForm) {
        const steps = document.querySelectorAll('.form-step');
        const progressFill = document.querySelector('.progress-fill');
        const progressSteps = document.querySelectorAll('.progress-steps .step');
        let currentStep = 1;
        
        function showStep(stepNumber) {
            steps.forEach(step => step.classList.remove('active'));
            progressSteps.forEach(step => step.classList.remove('active'));
            
            document.querySelector(`[data-step="${stepNumber}"]`).classList.add('active');
            
            for (let i = 0; i < stepNumber; i++) {
                progressSteps[i].classList.add('active');
            }
            
            progressFill.style.width = `${(stepNumber / 4) * 100}%`;
            currentStep = stepNumber;
        }
        
        document.querySelectorAll('.next-step').forEach(button => {
            button.addEventListener('click', function() {
                if (currentStep < 4) {
                    showStep(currentStep + 1);
                }
            });
        });
        
        document.querySelectorAll('.prev-step').forEach(button => {
            button.addEventListener('click', function() {
                if (currentStep > 1) {
                    showStep(currentStep - 1);
                }
            });
        });

        // Handle quote form submission
        quoteForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            
            // Show loading state
            submitButton.textContent = 'Submitting...';
            submitButton.disabled = true;
            
            try {
                const response = await fetch('/submit-quote', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                if (result.success) {
                    showAlert(result.message, 'success');
                    this.reset();
                    showStep(1); // Reset to first step
                } else {
                    showAlert(result.message, 'error');
                }
            } catch (error) {
                showAlert('Network error. Please try again.', 'error');
            } finally {
                submitButton.textContent = originalText;
                submitButton.disabled = false;
            }
        });
    }
});