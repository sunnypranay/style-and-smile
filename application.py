import pymysql as mysql
import flask
from flask import render_template, request,  redirect, url_for
import flask_login
import requests
import uuid
from flask_login import login_required
import Checksum
import forgot_password as mail
import mailer_confirmation as mc
import mailer_ack as ma

application = app = flask.Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

result = ""
users = {}

time_1 = ""
date = ""
design_type = ""


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()

    user.id = email
    print("request", request.form['password'])
    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


@app.route('/')
def index():
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    connection = mysql.connect(host='localhost',
                               database='user_information',
                               user='sunnypranay',
                               password='XXXXXXXXXXX')
    if flask.request.method == 'GET':
        return render_template("userlogin_m.html")
    email = request.form.get("username")

    cursor = connection.cursor()
    sql = ("SELECT * FROM user_data where user_name = '%s';" % (email,))
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.close()
    if len(result) == 0:
        return render_template("Bad_login.html")
    else:
        users[email] = {'password': result[0][2]}

    if request.form.get('password') == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('welcome'))
        # return flask.redirect(flask.url_for('protected'))
    return render_template("Bad_login.html")


@app.route('/register')
def register():
    return render_template('registration_modified.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    connection = mysql.connect(host='localhost',
                               database='user_information',
                               user='sunnypranay',
                               password='XXXXXXXXXXX')
    s1 = " "
    s2 = " "
    username_flag = False
    password_flag = False

    user = request.form.get("e-mail")
    password = request.form.get("password")
    password1 = request.form.get("password-1")

    cursor = connection.cursor()
    sql = "SELECT * FROM user_data"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        if user == i[1]:
            print("User name already taken")
            s1 = "User name already taken"
            username_flag = True
            break
        else:
            continue
    if password != password1:
        s2 = "Password doesn't match !!!"
        password_flag = True
    else:
        password_flag = False

    if (username_flag == True) or (password_flag == True):
        s3 = s1 + " " + s2
        return render_template("error.html", error_message=s3)
    else:
        # conn.execute("INSERT INTO user_data (user_name, password) VALUES (?,?)", (user, password))
        # conn.commit()
        sql = "INSERT INTO user_data (user_name, password,hash) VALUES (%s, %s,%s)"
        val = (user, password1, "NULL")
        cursor.execute(sql, val)
        connection.commit()
        print("Successfully Registered")
        # conn.close()
        s3 = "Registered successfully"

        return render_template("success_m.html", status=s3)


@app.route("/verify", methods=["GET", "POST"])
def verify():
    if flask.request.method == 'GET':
        return render_template("verify.html")
    email = request.form.get("username")
    connection = mysql.connect(host='localhost',
                               database='user_information',
                               user='sunnypranay',
                               password='XXXXXXXXXXX')
    cursor = connection.cursor()
    sql = ("SELECT * FROM user_data where user_name = '%s';" % (email,))
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    if len(result) == 0:
        return 'No user found please try again'
    else:
        code = uuid.uuid4().hex
        sql = "update user_data set hash = '%s' where user_name = '%s';" % (code, email,)
        cursor.execute(sql)
        connection.commit()
        connection.close()
        message = "http://ECommerce-env.u6cbbx6p7d.ap-south-1.elasticbeanstalk.com/verify/" + code
        print(mail.send_mail(message, email))

        return "<h1> Please Check your E-Mail </h1>"


@app.route("/verify/<hash_code>", methods=["GET", "POST"])
def email_verify(hash_code):
    connection = mysql.connect(host='localhost',
                               database='user_information',
                               user='sunnypranay',
                               password='XXXXXXXXXXX')
    cursor = connection.cursor()
    if flask.request.method == 'GET':

        sql = ("SELECT * FROM user_data where hash = '%s';" % (hash_code,))
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.close()
        if len(result) == 0:
            return "<h1> Invalid URL</h1>"
        else:
            return render_template("password_change.html", email=result[0][1])
    sql = ("SELECT * FROM user_data where hash = '%s';" % (hash_code,))
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.close()
    email = result[0][1]
    password = request.form.get("password")
    connection = mysql.connect(host='localhost',
                               database='user_information',
                               user='sunnypranay',
                               password='XXXXXXXXXXX')
    cursor = connection.cursor()
    sql = "update user_data set hash = 'NULL', password = '%s' where user_name = '%s';" % (password, email,)
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return "Password changed Successfully please login again"


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


@app.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():
    global date, time_1, design_type
    if flask.request.method == 'POST':
        date = request.form.get("date")
        time_1 = request.form.get("Time")
        design_type = request.form.get("design")
        return flask.redirect(flask.url_for('design'))
    return render_template("welcome_m.html")


@app.route('/design', methods=['GET', 'POST'])
@login_required
def design():
    mydb = mysql.connect(
        host="localhost",
        user="sunnypranay",
        passwd="XXXXXXXXXXX",
        database="user_information"
    )

    mycursor = mydb.cursor()
    # sql = "select * from date_info where date_info = '%s';" % (date_info,)
    # sql = "select * from design_details where design_type = '%s';" % design_type
    sql = """select distinct d.UUID, d.type, d.price, s.date, s.time, i.img_name, i.product_id, f.name, s.slot_id from design d inner join slot s on d.UUID = s.ID inner join images i on s.ID = i.UID inner join freelancer f on i.UID = f.UUID
            where
            s.date = '%s'
            and s.time = '%s'
            and s.design_type = '%s'
            and s.status = 'Free'
            and d.type = '%s'
            and i.type = '%s';""" % (date, time_1, design_type, design_type, design_type)

    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) == 0:
        return render_template("design_error.html")
    print(result)
    l1 = result
    d1 = {}
    for i in l1:
        if i[6] in d1:
            # d1[i[6]][0].append(i[5])
            d1[i[6]]["images"].append(i[5])
        else:
            # d1[i[6]] = [[i[5]], i[1], i[2], i[7]]
            d1[i[6]] = {"images": [i[5]], "design_type": i[1], "price": i[2], "freelancer_name": i[7], "date": i[3],
                        "time": i[4], "slot_id": i[8]}
    print(d1)
    return render_template("product_modified.html", d1=d1)


@app.route("/design_preview", methods=["POST"])
def get_post_javascript_data():
    connection = mysql.connect(host='localhost',
                               database='user_information',
                               user='sunnypranay',
                               password='XXXXXXXXXXX')
    product_id = request.form['product_id']
    slot_id = request.form['slot_id']
    print(slot_id)
    cursor = connection.cursor()
    sql = ("SELECT img_name FROM images where product_id = '%s';" % product_id)
    cursor.execute(sql)
    result = cursor.fetchall()
    sql = ("SELECT date, time FROM slot where slot_id = '%s';" % slot_id)
    cursor.execute(sql)
    slot_details = cursor.fetchall()
    print(slot_details)
    for i in result:
        print(i[0])
    sql = ("SELECT description, price, type FROM design where product_id = '%s';" % product_id)
    cursor.execute(sql);
    result_1 = cursor.fetchall()
    print(result_1)
    return render_template("product_discription_modified.html", result=result, result_1=result_1, product_id=product_id,
                           slot_id=slot_id, slot_details=slot_details)


@app.route("/design_confirm", methods=["POST", "GET"])
def design_confirm():
    connection = mysql.connect(host='localhost',
                               database='user_information',
                               user='sunnypranay',
                               password='XXXXXXXXXXX')
    cursor = connection.cursor()
    product_id = request.form['product_id']
    slot_id = request.form['slot_id']
    sql = ("SELECT price FROM design where product_id = '%s';" % product_id)
    cursor.execute(sql);
    result_1 = cursor.fetchall()
    print(result_1)
    return render_template("booking.html", product_id=product_id, slot_id=slot_id)


details = {}


@app.route("/design_confirm_c", methods=["POST", "GET"])
def design_confirm_c():
    global details
    connection = mysql.connect(host='localhost',
                               database='user_information',
                               user='sunnypranay',
                               password='XXXXXXXXXXX')
    cursor = connection.cursor()
    product_id = request.form['product_id']
    slot_id = request.form['slot_id']
    sql = ("SELECT price FROM design where product_id = '%s';" % product_id)
    cursor.execute(sql);
    result_1 = cursor.fetchall()
    print(result_1)

    details = {flask_login.current_user.id: {"name": request.form.get('name'), "number": request.form.get('number'),
                                             "email": request.form.get('email'), "price": str(result_1[0][0]),
                                             "product_id": request.form['product_id'],
                                             "slot_id": request.form['slot_id'],
                                             "sadan": request.form.get('sadan'),
                                             "room_number": request.form.get('room_number')}}
    print(details)
    paytmParams = {

        # Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        "MID": "wZoPLo18357123923799",

        # Find your WEBSITE in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        "WEBSITE": "WEBSTAGING",

        # Find your INDUSTRY_TYPE_ID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        "INDUSTRY_TYPE_ID": "Retail",

        # WEB for website and WAP for Mobile-websites or App
        "CHANNEL_ID": "WEB",

        # Enter your unique order id
        "ORDER_ID": str(uuid.uuid1()),

        # unique id that belongs to your customer
        "CUST_ID": details[flask_login.current_user.id]['product_id'],

        # customer's mobile number
        "MOBILE_NO": details[flask_login.current_user.id]['number'],

        # customer's email
        "EMAIL": details[flask_login.current_user.id]['email'],

        # Amount in INR that is payble by customer
        # this should be numeric with optionally having two decimal points
        "TXN_AMOUNT": details[flask_login.current_user.id]['price'],

        # on completion of transaction, we will send you the response on this URL
        "CALLBACK_URL": "http://ecommerce-env.u6cbbx6p7d.ap-south-1.elasticbeanstalk.com/confirm",
    }
    print(paytmParams)
    checksum = Checksum.generate_checksum(paytmParams, "vwBZlOSxr0&k_Am7")
    paytmParams["CHECKSUMHASH"] = checksum
    r = requests.post(url="https://securegw-stage.paytm.in/order/process", data=paytmParams)
    return r.text
    return 'done'


@app.route("/confirm", methods=["POST", "GET"])
def confirm():
    connection = mysql.connect(host='localhost',
                               database='user_information',
                               user='sunnypranay',
                               password='XXXXXXXXXXX')
    cursor = connection.cursor()
    form = request.form
    if form['STATUS'] == "TXN_SUCCESS":
        product_id = details[flask_login.current_user.id]["product_id"]
        slot_id = details[flask_login.current_user.id]["slot_id"]
        sql = ("SELECT status FROM slot where slot_id = '%s';" % details[flask_login.current_user.id]["slot_id"])
        cursor.execute(sql)
        status = cursor.fetchall()
        if status[0][0] == "Free":
            sql = "update slot set status = 'Full' where slot_id = '%s';" % details[flask_login.current_user.id][
                "slot_id"]
            cursor.execute(sql)
            connection.commit()

            sql = ("SELECT UUID FROM design where product_id = '%s';" % product_id)
            cursor.execute(sql)
            result = cursor.fetchall()
            sql = ("SELECT name, email, phone_number FROM freelancer where UUID = '%s';" % result[0][0])
            cursor.execute(sql)
            free_lancer = cursor.fetchall()
            sql = ("SELECT date, time FROM slot where slot_id = '%s';" % slot_id)
            cursor.execute(sql)
            slot_details = cursor.fetchall()
            sql = "INSERT INTO booking_details_1 (free_lancer_name,free_lancer_email,date,time,name,free_lancer_number,amount) VALUES (%s, %s, %s, %s, %s,%s,%s)"
            val = (
                free_lancer[0][0], free_lancer[0][1], slot_details[0][0], slot_details[0][1],
                flask_login.current_user.id, free_lancer[0][2], details[flask_login.current_user.id]["price"])
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            connection.close()
            mc.send_mail(details[flask_login.current_user.id]["email"], free_lancer[0][1], free_lancer[0][0],
                         free_lancer[0][2])
            ma.send_ack(free_lancer[0][1], flask_login.current_user.id, free_lancer[0][0],
                        details[flask_login.current_user.id]["price"], slot_details[0][0], slot_details[0][1],
                        details[flask_login.current_user.id]["number"])
            return render_template("confirm.html", free_lancer_name=free_lancer[0][0],
                                   free_lancer_email=free_lancer[0][1], date=slot_details[0][0],
                                   time=slot_details[0][1], form=form)
        else:
            return "Sorry to tell you that free-lancer is already booked for refund please contact 8919345427"
    else:
        return "Sorry transaction is failure !!!"


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
