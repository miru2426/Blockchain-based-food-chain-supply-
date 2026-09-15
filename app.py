from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from blockchain import FoodBlockchain

app = Flask(__name__)
app.secret_key = "food-chain-demo-key"
DB = "food_supply.db"
chain = FoodBlockchain()

def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = db()
    conn.execute("""CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        batch_id TEXT NOT NULL,
        quantity TEXT,
        location TEXT,
        owner TEXT,
        status TEXT,
        timestamp TEXT,
        block_hash TEXT,
        previous_hash TEXT
    )""")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = db()
    products = conn.execute("SELECT * FROM products ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", products=products, valid=chain.verify_chain(),
                           blocks=chain.chain)

@app.route("/add", methods=["GET", "POST"])
def add_record():
    if request.method == "POST":
        data = {k: request.form.get(k, "").strip() for k in
                ["product", "batch_id", "quantity", "location", "owner", "status"]}
        if not data["product"] or not data["batch_id"]:
            flash("Product name and Batch ID are required.")
            return redirect(url_for("add_record"))

        block = chain.add_food_record(**data)

        conn = db()
        conn.execute("""INSERT INTO products
            (product,batch_id,quantity,location,owner,status,timestamp,block_hash,previous_hash)
            VALUES (?,?,?,?,?,?,?,?,?)""",
            (data["product"], data["batch_id"], data["quantity"], data["location"],
             data["owner"], data["status"], block.timestamp, block.hash, block.previous_hash))
        conn.commit()
        conn.close()
        flash("Food supply-chain record added to the blockchain.")
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/verify")
def verify():
    return render_template("verify.html", valid=chain.verify_chain(), blocks=chain.chain)

@app.route("/reset")
def reset():
    global chain
    chain = FoodBlockchain()
    conn = db()
    conn.execute("DELETE FROM products")
    conn.commit()
    conn.close()
    flash("Demo blockchain and database were reset.")
    return redirect(url_for("index"))

init_db()

if __name__ == "__main__":
    app.run(debug=True)
