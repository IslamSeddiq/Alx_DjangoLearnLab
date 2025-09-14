# Permissions & Groups Setup

## Custom Permissions (on Book model)
- can_view → View book list
- can_create → Create a new book
- can_edit → Edit an existing book
- can_delete → Delete a book

## Groups
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → can_view, can_create, can_edit, can_delete

## Usage
- Permissions are enforced in views with `@permission_required`.
- Users inherit permissions from their assigned group.
- Test by creating users and adding them to groups via the admin site.

# Security Measures Implemented

## Settings
- DEBUG = False in production
- XSS, CSRF, and Clickjacking protections enabled via Django settings
- Cookies secured with CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE

## Views
- All forms include {% csrf_token %}
- ORM queries used instead of raw SQL to prevent SQL injection
- Input validated using Django Forms

## CSP
- Implemented strict Content Security Policy using django-csp middleware
- Only self-hosted content allowed, with exceptions for trusted CDNs

## Testing
- Manually tested CSRF tokens in forms
- Verified that untrusted script injections are blocked
- Confirmed that SQL injection attempts are neutralized

# Security Setup

## HTTPS & Secure Headers
- Enforced HTTPS with `SECURE_SSL_REDIRECT = True`.
- HSTS enabled for 1 year (`SECURE_HSTS_SECONDS = 31536000`).
- Secure cookies (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`).
- Added headers: 
  - `X_FRAME_OPTIONS = "DENY"`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `SECURE_BROWSER_XSS_FILTER = True`

## Deployment
- Configured SSL/TLS certificates using Let's Encrypt.
- Nginx redirects all HTTP → HTTPS.
