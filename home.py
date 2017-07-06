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


@app.route("/")
def show_tables():
    # Read sqlite query results into a pandas DataFrame

    con = sqlite3.connect("otc.db")
    cursor = con.execute('SELECT * FROM company')
    # data = pd.read_sql_query("SELECT * from company", con)
    # con.close()
    # data = pd.read_excel('dummy_data.xlsx')
    # data.set_index(['ID'], inplace=True)
    # data.index.name=None
    return render_template('view.html',items=cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
