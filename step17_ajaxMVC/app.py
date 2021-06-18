from flask import Flask, request, render_template
from dao import EmpDAO
from dto import EmpDTO

app = Flask(__name__)

@app.route('/', methods=['get'])
def get():
    return render_template('reqres.html')  


@app.route('/getdata', methods=['get'])
def getdata():
    return '{"name":"재석", "age":49}'


@app.route("/getemp", methods=['post'])
def datemp():
    return EmpDAO().empone(request.form.get('empno'))

@app.route('/insert', methods=['post'])
def insertemp():
    
    dao = EmpDAO()
    dto = EmpDTO(request.form.get('empno'), request.form.get('ename'), request.form.get('sal'))
    dao.empinsert(dto)

    return EmpDAO().empone(request.form.get('empno'))



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")