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

sorting = {'name':True,'open':True,'close':True, 'vol': True, 'price':True}

@app.route("/data/<name>")
def show_data(name):
    con = sqlite3.connect("otc.db")
    # Read sqlite query results into a pandas DataFrame
    cursor = con.execute("SELECT * FROM company where name='"+name+"'")
    # data = pd.read_sql_query("SELECT * from company", con)
    # con.close()
    # data = pd.read_excel('dummy_data.xlsx')
    # data.set_index(['ID'], inplace=True)
    # data.index.name=None
    return render_template('data.html',items=cursor.fetchall())


@app.route("/",methods=['GET', 'POST'])
def show_tables():
    sort = request.args.get('sort') or None
    con = sqlite3.connect("otc.db")
    # Read sqlite query results into a pandas DataFrame
    if request.method == 'GET':
        sql_stat = "select * from stocks"
        if sort:
            if sorting[sort]:
                order = "asc"
            else:
                order = "desc"
            sorting[sort] = not sorting[sort]
            sql_stat += " order by "+sort+" "+order
            print(sql_stat)
        cursor = con.execute(sql_stat)
        # cursor = con.execute("select * from stocks x where Timestamp = (select max(y.Timestamp) from stocks y where y.name = x.name)")
        # data = pd.read_sql_query("SELECT * from company", con)
        # con.close()
        # data = pd.read_excel('dummy_data.xlsx')
        # data.set_index(['ID'], inplace=True)
        # data.index.name=None
        return render_template('view.html',items=cursor.fetchall())
    else:
        # print("Hi")
        price = request.form['price']
        volmax = request.form['numbermax'] or 0
        volmin = request.form['numbermin'] or 0
        stat = "SELECT * FROM company where price < "+ str(price)
        if volmin or volmax:
            stat += " and vol<"+volmax+" and vol >"+volmin
        cursor = con.execute(stat)
        return render_template('view.html',items=cursor.fetchall())

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)
