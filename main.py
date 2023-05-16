import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Membuat instance Dash
app = dash.Dash(__name__)

# Layout aplikasi
app.layout = html.Div(
    children=[
        html.H1("Aplikasi Catatan Harian"),
        html.Div(
            children=[
                dcc.Textarea(
                    id="note-input",
                    placeholder="Masukkan catatan di sini",
                    style={"width": "100%", "height": "100px"}
                ),
                html.Button("Simpan", id="save-button", n_clicks=0),
            ],
            style={"margin-bottom": "20px"}
        ),
        html.Div(id="message"),
        html.H2("Daftar Catatan Harian"),
        html.Ul(id="note-list"),
    ],
    style={"max-width": "600px", "margin": "auto"}
)

# Callback untuk menyimpan catatan harian
@app.callback(
    Output("message", "children"),
    [Input("save-button", "n_clicks")],
    [State("note-input", "value")]
)
def save_note(n_clicks, note):
    if n_clicks > 0 and note:
        # Simpan catatan ke basis data atau tempat penyimpanan lainnya
        # Di sini, hanya mencetak catatan ke konsol sebagai contoh
        print("Catatan baru:", note)
        return html.P("Catatan berhasil disimpan!")
    else:
        return ""

# Callback untuk menampilkan daftar catatan harian
@app.callback(
    Output("note-list", "children"),
    [Input("save-button", "n_clicks")]
)
def display_notes(n_clicks):
    if n_clicks > 0:
        # Ambil daftar catatan dari basis data atau tempat penyimpanan lainnya
        # Di sini, hanya menampilkan catatan yang telah disimpan sebelumnya sebagai contoh
        notes = [
            "Catatan 1",
            "Catatan 2",
            "Catatan 3"
        ]
        return [html.Li(note) for note in notes]
    else:
        return []

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run_server(debug=True)

