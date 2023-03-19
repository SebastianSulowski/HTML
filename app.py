from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/mypage/me')
def about_me():
    return render_template('index.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact_info():
    if request.method == 'POST':
        message = request.form['message']
        print(f"Received message: {message}")
    return render_template('index_1.html')

if __name__ == '__main__':
    app.run(debug=True)
