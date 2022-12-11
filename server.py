from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/') 
def my_home():
    return render_template('index.html')
 
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as mydatabase2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        mycsvwriter = csv.writer(mydatabase2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        mycsvwriter.writerow([email,subject,message])
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else: 
        return "Try again. Something went wrong."


