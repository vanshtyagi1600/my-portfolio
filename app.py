# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/snake')
# def snake():
#     return render_template('snake.html')

# @app.route('/calculator')
# def calculator():
#     return render_template('calculator.html')

# @app.route('/contact', methods=['POST'])
# def contact():
#     name = request.form['name']
#     email = request.form['email']
#     message = request.form['message']

#     print("New Message")
#     print("Name:", name)
#     print("Email:", email)
#     print("Message:", message)

#     return """
#     <h1 style='text-align:center; margin-top:100px; color:green;'>
#     Message Sent Successfully ✅
#     </h1>
#     <div style='text-align:center;'>
#         <a href='/'>Go Back</a>
#     </div>
#     """

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Snake Game
@app.route('/snake')
def snake():
    return render_template('snake.html')

# Calculator
@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

# Sarkari Result
@app.route('/sarkari-result')
def sarkari_result():
    return render_template('sarkari_result.html')

# College Management System
@app.route('/collage')
def collage():
    return render_template('collage.html')

# Hospital Management System
@app.route('/hospital')
def hospital():
    return render_template('hospital.html')

   





# Contact Form
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = MIMEText(f"""
Name: {name}
Email: {email}
Message: {message}
""")

    msg['Subject'] = 'New Portfolio Contact Message'
    msg['From'] = 'v50528347@gmail.com'
    msg['To'] = 'v50528347@gmail.com'

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(
            'v50528347@gmail.com',
            'YOUR_16_DIGIT_APP_PASSWORD'
        )

        server.send_message(msg)
        server.quit()

        return "Message Sent Successfully!"

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)