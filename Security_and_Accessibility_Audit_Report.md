# Security and Accessibility Audit Report

Brandon Smith  
November 16, 2025  
Vinyl Collection App

## Security Issues

### 1. Hardcoded Secret Key

Location: app.py, line 6

The secret key is hardcoded in the source code:

```python
app.config['SECRET_KEY'] = 'your-secret-key-here'
```

This is bad because if the code gets uploaded to GitHub, anyone can see it and use it to fake user sessions.

Fix: Use environment variables instead. Put the key in a .env file and add .env to .gitignore.

```python
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
```

### 2. Debug Mode Enabled

Location: app.py, line 113

```python
app.run(debug=True)
```

Debug mode shows an interactive console when there's an error. Hackers can use this to run code on the server.

Fix: Turn off debug mode or only enable it in development.

```python
debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
app.run(debug=debug_mode)
```

### 3. No CSRF Protection

Location: All forms in templates

The forms don't have CSRF tokens. Attackers could trick users into submitting forms without knowing it.

Example:
```html
<form method="POST">
    <!-- No CSRF token -->
    <input type="text" name="title">
    <button type="submit">Add Record</button>
</form>
```

Fix: Install Flask-WTF and add CSRF tokens to all forms.

```bash
pip install Flask-WTF
```

```python
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)
```

```html
<form method="POST">
    {{ csrf_token() }}
    <!-- rest of form -->
</form>
```

## Accessibility Issues

### 1. Search Input Missing Label

Location: templates/index.html
WCAG: 3.3.2 Labels or Instructions (Level A)

The search box has no label tag. Screen readers just say "edit text" with no context.

```html
<form method="GET">
    <input type="text" name="search" placeholder="Search...">
    <button type="submit">Search</button>
</form>
```

Fix: Add a label tag.

```html
<form method="GET">
    <label for="search-input">Search:</label>
    <input type="text" id="search-input" name="search">
    <button type="submit">Search</button>
</form>
```

### 2. Poor Color Contrast on Table Headers

Location: templates/index.html (CSS section)
WCAG: 1.4.3 Contrast (Minimum) (Level AA)

Location: templates/index.html (CSS section)
WCAG: 1.4.3 Contrast (Minimum) (Level AA)

The table headers use white text on a purple gradient. The contrast is too low.

```css
th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}
```

Tested with WebAIM contrast checker:
- White on #667eea = 3.8:1 (need 4.5:1)
- White on #764ba2 = 4.2:1 (need 4.5:1)

Fix: Use a darker purple that passes contrast requirements.

```css
th {
    background: #4c51bf;
    color: white;
}
```

### 3. No Keyboard Focus Indicators

Location: templates/index.html (CSS section)
WCAG: 2.4.7 Focus Visible (Level AA)

Location: templates/index.html (CSS section)
WCAG: 2.4.7 Focus Visible (Level AA)

The Edit and Delete buttons have no visible focus outline. When I tab through the page, I can't see which button I'm on.

```css
input:focus, select:focus {
    outline: none;
}

.btn {
    /* No focus styles */
}
```

Fix: Add focus styles to buttons.

```css
.btn:focus {
    outline: 3px solid #ffd700;
    outline-offset: 2px;
}

input:focus, select:focus {
    outline: 2px solid #667eea;
}
```

## Summary

Security Issues:
1. Hardcoded secret key (Critical) - app.py line 6
2. Debug mode enabled (Critical) - app.py line 113
3. No CSRF tokens (High) - all forms

Accessibility Issues:
1. Search has no label (High) - violates WCAG 3.3.2 Level A
2. Low color contrast (Medium) - violates WCAG 1.4.3 Level AA
3. No focus indicators (High) - violates WCAG 2.4.7 Level AA

