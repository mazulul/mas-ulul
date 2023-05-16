import dash
import dash_core_components as dcc
import dash_html_components as html

# Membuat instance Dash
app = dash.Dash(__name__)

# Layout aplikasi
app.layout = html.Div(
    children=[
        html.H1("Selamat Datang di Aplikasi Web Sederhana"),
        dcc.Input(id="input-text", type="text", placeholder="Masukkan teks"),
        html.Button("Kirim", id="submit-button", n_clicks=0),
        html.Div(id="output")
    ]
)

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
