from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Route for the login page
@app.route('/')
def login():
    return render_template('login.html')

# Route to handle registration form submission
@app.route('/register', methods=['POST'])
def register():
    user_id = request.form.get('user_id')
    password = request.form.get('password')

    if not user_id or not password:
        flash("UserID and Password cannot be empty!", "error")
        return redirect(url_for('login'))
    
    # For demonstration, we'll just flash the success message. Normally, you would store the details in a database.
    flash(f"Successfully registered UserID: {user_id}", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
 