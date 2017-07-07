import pandas as pd
import sqlite3
import datetime
from flask import *
app = Flask(__name__)
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('home', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def datetimeformat(value):
    return datetime.datetime.fromtimestamp(value).strftime("%Y-%m-%d %H:%M")
env.filters['datetimeformat'] = datetimeformat

app.add_template_filter(datetimeformat)
# verify that result of SQL query is stored in the dataframe
# print(df.head())


@app.route("/",methods=['GET', 'POST'])
def show_tables():
    con = sqlite3.connect("otc.db")
    # Read sqlite query results into a pandas DataFrame
    if request.method == 'GET':
        cursor = con.execute('SELECT * FROM company')
        # data = pd.read_sql_query("SELECT * from company", con)
        # con.close()
        # data = pd.read_excel('dummy_data.xlsx')
        # data.set_index(['ID'], inplace=True)
        # data.index.name=None
        return render_template('view.html',items=cursor.fetchall())
    else:
        # print("Hi")
        price = request.form['price']
        volmin = request.form['numbermax'] or 0
        volmin = request.form['numbermin'] or 0
        cursor = con.execute('SELECT * FROM company where price <' + str(price))
        return render_template('view.html',items=cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
