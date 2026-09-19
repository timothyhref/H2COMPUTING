from flask import *
import sqlite3
import random
houses = ['Taurus','Volans','Aquila','Pavo','Aries','Ursa']
app = Flask(__name__)
#home page
@app.route('/')
def home():
    return render_template('home.html')
#display house logos page
@app.route('/display_house')
def display_house():
    conn = sqlite3.connect('HOUSEALLOCATION.db')
    cursor = conn.cursor()
    cursor.execute('SELECT houseName, imageURL FROM HOUSE')
    result = cursor.fetchall()
    conn.close()
    return render_template('display_house.html',result = result)
@app.route('/allocate_house',methods = ["GET","POST"])
def allocate_house():
    if request.method == 'GET':
        return render_template('allocate_house.html')
    else:
        conn = sqlite3.connect('HOUSEALLOCATION.db')
        name = request.form.get('name')
        department = request.form.get('department')
        cursor = conn.cursor()
        cursor.execute('SELECT houseName FROM STAFF WHERE name = ? AND department = ?',(name,department))
        result = cursor.fetchone()
        if result[0] == 'Unassigned':
            newhouse = houses[random.randint(0,5)]
            cursor.execute('UPDATE STAFF SET houseName = ? WHERE name = ? AND department = ?',(newhouse,name,department))
            conn.commit()
            return render_template('house_result.html',name=name,department=department,result=False,house = newhouse)
        else:
            return render_template('house_result.html',name=name,department=department,result=True,house = result[0])
@app.route("/display_teachers")
def display_teachers():
    staff = []
    conn = sqlite3.connect('HOUSEALLOCATION.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT HOUSE.houseName group_concat(STAFF.name)
    FROM STAFF JOIN HOUSE ON STAFF.houseName = HOUSE.houseName
    GROUP BY HOUSE.houseName 
    ORDER BY HOUSE.houseName ASC''')
    result = cursor.fetchall()
    conn.close()
    return render_template('display_teachers.html',staff=result)
if __name__ == '__main__':
    app.run(debug=True)
    
