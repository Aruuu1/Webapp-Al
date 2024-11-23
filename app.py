from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        nama = request.form.get('nama')
        nim = request.form.get('nim')
        email = request.form.get('email')
        jurusan = request.form.get('jurusan')
        kode_matakuliah = request.form.get('kode_matakuliah')
        matakuliah = request.form.get('matakuliah')
        nilai = float(request.form.get("nilai", 0.0))
        sks = int(request.form.get('sks', 0))
        ipk = (nilai * sks) / sks

        return render_template ("index.html", nama=nama, nim=nim, email=email, jurusan=jurusan, kode_matakuliah=kode_matakuliah, nilai=nilai, matakuliah=matakuliah, sks=sks, ipk=ipk)

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
