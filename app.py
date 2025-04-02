from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Créer la base de données
"""  init():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  name TEXT, 
                  amount REAL, 
                  category TEXT, 
                  date TEXT)''')  # Nouvelle colonne 'date' pour stocker la date
    conn.commit()
    conn.close()

init() """

# Route principale pour afficher toutes les dépenses
@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    conn.close()
    
    return render_template('index.html', expenses=expenses)

# Route pour ajouter une nouvelle dépense
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format de la date actuelle
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO expenses (name, amount, category, date) VALUES (?, ?, ?, ?)", 
                  (name, amount, category, date))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('add_expense.html')

# Route pour afficher le résumé des dépenses par catégorie
@app.route('/summary')
def summary():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    summary_data = c.fetchall()
    conn.close()
    
    return render_template('summary.html', summary=summary_data)

# Point d'entrée pour exécuter l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
