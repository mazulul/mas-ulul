from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Nama : Muhammad ulul albab</p><p> Tempat,Tanggal Lahir : Malang, 31 Juli 2004</p><p> Alamat : dinoyo, lowokwaru, Malang</p><p> Jenis Kelamin : Laki-Laki</p><p> Kewarganegaraan : Indonesia</p><p> Agama : Islam</p>"

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
  
