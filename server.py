from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/<string:page_url>")
def page_name(page_url):
    return render_template(page_url)


@app.route('/submitform', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        email = data['email']
        subject = data['subject']
        message = data['message']
        print([data])

        with open('database.txt', 'a') as f:
            f.write(f"\n{email}, {subject}, {message}")

        field_names = ['email', 'subject', 'message']

        with open('database.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writerows([data])

        return redirect('thankyou.html')
    else:
        return 'something went wrong!'
