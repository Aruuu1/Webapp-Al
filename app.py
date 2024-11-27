from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

app.secret_key = 'secret'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        session['nama'] = request.form.get('nama')
        session['nim'] = request.form.get('nim')
        session['email'] = request.form.get('email')
        session['jurusan'] = request.form.get('jurusan')
        session['kode_matakuliah'] = request.form.get('kode_matakuliah')
        session['matakuliah'] = request.form.get('matakuliah')
        session['nilai'] = float(request.form.get("nilai", 0.0))
        session['sks'] = int(request.form.get('sks', 0))
        session['ipk'] = (session['nilai'] * session['sks']) / session['sks']

        return redirect(url_for('dashboard'))

    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    if 'nama' in session:
        return render_template ('dashboard.html',
        nama = session['nama'],
        nim = session['nim'],
        jurusan = session['jurusan'],
        email = session['email'])

    return redirect(url_for("index"))

@app.route("/krs")
def krs():
    if 'nama' in session:
        return render_template ('krs.html',
        kode_matakuliah = session['kode_matakuliah'],
        matakuliah = session['matakuliah'],
        sks = session['sks'])

    return redirect(url_for("index"))

@app.route("/ipk")
def ipk():
    if 'nama' in session:
        return render_template ('ipk.html',
        ipk = session['ipk'],
        sks = session['sks'])

    return redirect(url_for("index"))

@app.route("/daftarnilai")
def daftarnilai ():
    if 'nama' in session:
        return render_template ('daftarnilai.html',
        nilai = session['nilai'],
        matakuliah = session['matakuliah'],
        sks = session['sks'])

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
