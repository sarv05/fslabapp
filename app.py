from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Define HTML and CSS within the Python code
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App with CSS</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My Flask App</h1>
        <p>This is a simple example of embedding CSS within the HTML.</p>
    </body>
    </html>
    '''
    # Render the HTML content as the response
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
