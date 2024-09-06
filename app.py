# Import libraries
from flask import Flask, request, url_for, redirect, render_template


# Instantiate Flask functionality
app = Flask(__name__)


# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]


# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)


# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        transation = {
              'id': len(transactions)+1,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
             }
        transactions.append(transation)
        return redirect(url_for("get_transactions"))
    return render_template("form.html")


# Update operation
@app.route("/edit/<int:transaction_id>", methods=["POST", "GET"])
def edit_transaction(transaction_id):
    transaction = get_transaction(transaction_id)
    if request.method == "POST":
        date = request.form['date']
        amount = float(request.form['amount'])
        update(transaction, date, amount)
        return redirect(url_for("get_transactions"))
    return render_template("edit.html", transaction=transaction)


def get_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return transaction


def update_by_id(id, date, amount):
    transaction = get_transaction(id)
    transaction["date"] = date
    transaction["amount"] = amount


def update(transaction, date, amount):
    transaction["date"] = date
    transaction["amount"] = amount


# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    transaction = get_transaction(transaction_id)
    transactions.remove(transaction)
    return redirect(url_for("get_transactions"))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
