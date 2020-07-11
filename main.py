from flask import *
from flask_sqlalchemy import SQLAlchemy
import MySQLdb
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

mysql = MySQLdb.connect(host = "localhost", user =,passwd = , database = )
cur = mysql.cursor()

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchase_bill_no = db.Column(db.String(1000))
    purchase_product_type = db.Column(db.String(100))
    purchase_product_name = db.Column(db.String(100))
    purchase_description = db.Column(db.String(100))
    purchase_rate = db.Column(db.Float)
    purchase_quantity = db.Column(db.String(100))
    purchased_units = db.Column(db.Integer)
    purchased_date = db.Column(db.Date)
    seller_name = db.Column(db.String(200))
    purchase_payment_method = db.Column(db.String(100))
    purchase_total_amount = db.Column(db.Float)
    purchase_amount_paid = db.Column(db.Float)
    purchase_due_amount = db.Column(db.Float)

    def __init__(self, purchase_bill_no, purchase_product_type, purchase_product_name, purchase_description, purchase_rate, purchase_quantity,
                 purchased_units, purchased_date,
                 seller_name, purchase_payment_method, purchase_total_amount, purchase_amount_paid,
                 purchase_due_amount):
        self.purchase_bill_no = purchase_bill_no
        self.purchase_product_type = purchase_product_type
        self.purchase_product_name = purchase_product_name
        self.purchase_description = purchase_description
        self.purchase_rate = purchase_rate
        self.purchase_quantity = purchase_quantity
        self.purchased_units = purchased_units
        self.purchased_date = purchased_date
        self.seller_name = seller_name
        self.purchase_payment_method = purchase_payment_method
        self.purchase_total_amount = purchase_total_amount
        self.purchase_amount_paid = purchase_amount_paid
        self.purchase_due_amount = purchase_due_amount


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sales_bill_no = db.Column(db.String(1000))
    sales_product_type = db.Column(db.String(100))
    sales_product_name = db.Column(db.String(100))
    sales_description = db.Column(db.String(100))
    selling_rate = db.Column(db.Float)
    sales_quantity = db.Column(db.String(100))
    sold_units = db.Column(db.Integer)
    sold_date = db.Column(db.Date)
    purchaser_name = db.Column(db.String(200))
    sales_payment_method = db.Column(db.String(100))
    sales_total_amount = db.Column(db.Float)
    sales_amount_paid = db.Column(db.Float)
    sales_due_amount = db.Column(db.Float)

    def __init__(self, sales_bill_no, sales_product_type, sales_product_name, sales_description, selling_rate, sales_quantity,
                 sold_units, sold_date, purchaser_name,
                 sales_payment_method, sales_total_amount, sales_amount_paid,
                 sales_due_amount):
        self.sales_bill_no = sales_bill_no
        self.sales_product_type = sales_product_type
        self.sales_product_name = sales_product_name
        self.sales_description = sales_description
        self.selling_rate = selling_rate
        self.sales_quantity = sales_quantity
        self.sold_units = sold_units
        self.sold_date = sold_date
        self.purchaser_name = purchaser_name
        self.sales_payment_method = sales_payment_method
        self.sales_total_amount = sales_total_amount
        self.sales_amount_paid = sales_amount_paid
        self.sales_due_amount = sales_due_amount

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(100))
    product = db.Column(db.String(100))
    description = db.Column(db.String(100))
    rate = db.Column(db.Float)
    quantity = db.Column(db.String(100))
    units = db.Column(db.Integer)
    Amounts = db.Column(db.Float)

    def __init__(self, product_type, product, description, rate, quantity, units, Amounts):
        self.product_type = product_type
        self.product = product
        self.description = description
        self.quantity = quantity
        self.units = units
        self.Amounts = Amounts

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(200))
    expenses = db.Column(db.String(200))
    expense_description = db.Column(db.String(200))
    expenses_amount = db.Column(db.Float)
    date = db.Column(db.Date)

    def __init__(self, company_name, expenses, expense_description, expenses_amount, date):
        self.company_name = company_name
        self.expenses = expenses
        self.expense_description = expense_description
        self.expenses_amount = expenses_amount
        self.date = date

class enterprise_detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enterprise_name = db.Column(db.String(200))
    udhyog_aadhar = db.Column(db.Integer)
    owner_name = db.Column(db.String(200))
    enterprise_email = db.Column(db.String(200))
    mobile_no = db.Column(db.Integer)
    investment = db.Column(db.Float)

    def __init__(self, enterprise_name, udhyog_aadhar, owner_name, enterprise_email, mobile_no, investment):
        self.enterprise_name = enterprise_name
        self.udhyog_aadhar = udhyog_aadhar
        self.owner_name = owner_name
        self.enterprise_email = enterprise_email
        self.mobile_no = mobile_no
        self.investment = investment


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/enter_in')
def company_in():
    return render_template('companyin.html')


@app.route('/enter_register')
def add_enter():
    return render_template('enter_register.html')

@app.route('/template')
def template():
    return render_template('template.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')
# Login Validation 
@app.route('/login', methods=['post'])
def login_validation():
    user_name = request.form.get('username')
    password = request.form.get('password')
    
    cur.execute("""SELECT * FROM users WHERE username LIKE '{}' AND user_password LIKE '{}' """
    .format(user_name,password))
    user = cur.fetchall()
    if len(user)>0:
        session['user_id'] =[0][0]
        return redirect('/home')
    else:
        return redirect('/login')
# Add users
@app.route('/register', methods=['post'])
def add_users():
    username = request.form.get('username')
    email  = request.form.get('email')
    user_password = request.form.get('password')

    cur.execute("INSERT INTO users(username, email, user_password) VALUES" 
    "('{}','{}','{}')".format(username, email, user_password))
    mysql.commit()

    return redirect('/')

# logout
@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

# enterprise is registered or not
@app.route('/enter_in', methods=['post'])
def enter_validation():
    
    enterprise_name = request.form.get('enterprise_name')
    udhyog_aadhar = request.form.get('udhyog_aadhar_no')
    
    cur.execute("""SELECT * FROM enterprise_detail WHERE enterprise_name LIKE '{}' AND udhyog_aadhar LIKE '{}' """
    .format(enterprise_name, udhyog_aadhar))
    user = cur.fetchall()
    
    if len(user)>0:
        return redirect('/template')
    else:
        return redirect('/enter_register')

#    Add enterprise data
@app.route('/enter_register', methods=['POST'])
def add_enterprise():
    if request.method == "POST":
        enterprise_name = request.form['enterprise_name']
        udhyog_aadhar = request.form['udhyog_aadhar']
        owner_name = request.form['owner_name']
        enterprise_email = request.form['enterprise_email']
        mobile_no = request.form['mobile_no']
        investment = request.form['investment']
        
        my_enterprise = enterprise_detail(enterprise_name, udhyog_aadhar, owner_name, enterprise_email, mobile_no, investment)
        db.session.add(my_enterprise)
        db.session.commit()

    return redirect('/ente_in')


@app.route('/invoice')
def invoice():
    purchase_data = Purchase.query.all()
    sales_data = Sales.query.all()
    expenses_data = Expense.query.all()
    return render_template('invoice.html', purchase=purchase_data, sales=sales_data, expense=expenses_data)


@app.route('/purchase')
def purchase():
    purchase_data = Purchase.query.all()
    return render_template('purchase.html', purchase=purchase_data)


@app.route('/sales')
def sales():
    sales_data = Sales.query.all()
    purchase_data = Purchase.query.all()
    return render_template('sales.html', sales=sales_data, purchase=purchase_data)


@app.route('/expenses')
def expenses():
    expenses_data = Expense.query.all()
    return render_template('expenses.html', expense=expenses_data)

# Add purchases
@app.route('/purchase', methods=['POST'])
def insert_purchase():
    if request.method == "POST":
        purchase_bill_no = request.form["purchase_bill_no"]
        purchase_product_type = request.form["purchase_product_type"]
        purchase_product_name = request.form["purchase_product_name"]
        purchase_description = request.form["purchase_description"]
        purchase_rate = request.form["purchase_rate"]
        purchase_quantity = request.form["purchase_quantity"]
        purchased_units = request.form["purchased_units"]
        purchased_date = request.form["purchased_date"]
        seller_name = request.form["seller_name"]
        purchase_payment_method = request.form["purchase_payment_method"]
        purchase_amount_paid = request.form["purchase_amount_paid"]

        purchase_total_amount = float(purchase_rate) * float(purchased_units)
        purchase_due_amount = float(purchase_total_amount) - float(purchase_amount_paid)
        my_data = Purchase(purchase_bill_no, purchase_product_type, purchase_product_name, purchase_description, purchase_rate,
                           purchase_quantity, purchased_units, purchased_date,
                           seller_name, purchase_payment_method, purchase_total_amount,
                           purchase_amount_paid, purchase_due_amount)
        db.session.add(my_data)
        db.session.commit()
        flash("Transaction Inserted Successfully")
        return redirect(url_for('purchase'))

# Add Sales
@app.route('/sales', methods=['POST'])
def insert_sales():
    if request.method == "POST":
        sales_bill_no = request.form["sales_bill_no"]
        sales_product_type = request.form["sales_product_type"]
        sales_product_name = request.form["sales_product_name"]
        sales_description = request.form["sales_description"]
        selling_rate = request.form["selling_rate"]
        sales_quantity = request.form["sales_quantity"]
        sold_units = request.form["sold_units"]
        sold_date = request.form["sold_date"]
        purchaser_name = request.form["purchaser_name"]
        sales_payment_method = request.form["sales_payment_method"]
        sales_amount_paid = request.form["sales_amount_paid"]

        sales_total_amount = float(selling_rate) * float(sold_units)
        sales_due_amount = float(sales_total_amount) - float(sales_amount_paid)
        
        
        
        my_sales = Sales(sales_bill_no, sales_product_type, sales_product_name, sales_description, selling_rate, sales_quantity,
                         sold_units, sold_date, purchaser_name,
                         sales_payment_method, sales_total_amount, sales_amount_paid,
                         sales_due_amount)

        db.session.add(my_sales)
        db.session.commit()
       
        

        flash("Transaction Inserted Successfully")
        return redirect(url_for('sales'))

# Add Expenses
@app.route('/expenses', methods=['POST'])
def insert_expenses():
    if request.method == "POST":
        company_name = request.form["company_name"]
        expenses = request.form["expenses"]
        expense_description = request.form["expense_description"]
        expenses_amount = request.form["expenses_amount"]
        date = request.form["date"]

        my_expense = Expense(company_name, expenses, expense_description, expenses_amount, date)
        db.session.add(my_expense)
        db.session.commit()
        flash("Transaction Inserted Successfully")
        return redirect(url_for('expenses'))

# Delete Purchases
@app.route('/delete_purchase/<id>/', methods=['GET', 'POST'])
def delete_purchase(id):
    my_data = Purchase.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Deleted Successfully")

    return redirect(url_for('purchase'))

# Delete sales
@app.route('/delete_sales/<id>/', methods=['GET', 'POST'])
def delete_sales(id):
    my_sales = Sales.query.get(id)
    db.session.delete(my_sales)
    db.session.commit()
    flash("Deleted Successfully")

    return redirect(url_for('sales'))

# Delete Expenses
@app.route('/delete_expenses/<id>/', methods=['GET', 'POST'])
def delete_expenses(id):
    my_expenses = Expense.query.get(id)
    db.session.delete(my_expenses)
    db.session.commit()
    flash("Deleted Successfully")

    return redirect(url_for('expenses'))

def acounting():
       # Accountings
        invs = cur.execute("SELECT SUM(investment) FROM enterprise_detail ")
        my_investment = invs.fetchall()
        expenses = cur.execute("SELECT SUM(expenses_amount) FROM expense ")
        p_total = cur.execute("SELECT SUM(purchase_total_amount) FROM purchase ")
        p_due = cur.execute("SELECT SUM(purchase_due_amount) FROM purchase ")
        s_total = cur.execute("SELECT SUM(sales_total_amount) FROM sales ")
        s_due = cur.execute("SELECT SUM(sales_due_amount) FROM sales ")
        s_paid = cur.execute("SELECT SUM(sales_amount_paid) FROM sales ")
        profit = s_total
        c_b = (investment - p_total + expenses + s_total - s_due + profit )
        return  render_template('template.html', my_investment=my_investment, expenses=expenses, p_total=p_total, 
        p_due=p_due, s_total=s_total, s_due=s_due, profit=profit, c_b=c_b)

if __name__ == '__main__':
    app.run(debug=True)
