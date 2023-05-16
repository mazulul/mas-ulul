import dash
import dash_core_components as dcc
import dash_html_components as html

app = Flask(__name__)
# Membuat instance Dash
app = dash.Dash(__name__)

@app.route("/")
def hello_world():
  return "<p>Nama : Muhammad ulul albab</p><p> Tempat,Tanggal Lahir : Malang, 31 Juli 2004</p><p> Alamat : dinoyo, lowokwaru, Malang</p><p> Jenis Kelamin : Laki-Laki</p><p> Kewarganegaraan : Indonesia</p><p> Agama : Islam</p>"
# Layout aplikasi
app.layout = html.Div(
    children=[
        html.H1("Selamat Datang di Aplikasi Web Sederhana"),
        dcc.Input(id="input-text", type="text", placeholder="Masukkan teks"),
        html.Button("Kirim", id="submit-button", n_clicks=0),
        html.Div(id="output")
    ]
)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

# Callback untuk merespon input pengguna
@app.callback(
    dash.dependencies.Output("output", "children"),
    [dash.dependencies.Input("submit-button", "n_clicks")],
    [dash.dependencies.State("input-text", "value")]
)
def update_output(n_clicks, input_text):
    if n_clicks > 0 and input_text:
        return html.H2(f"Anda mengirim: {input_text}")
    else:
        return ""
#menjalankan aplikasi
if __name__ == '__main__':
    app.run_server(debug=True)