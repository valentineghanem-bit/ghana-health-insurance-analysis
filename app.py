"""
NHIS Uninsurance & Health Equity — Ghana 261 Districts
Dash application entry point.
See dashboard/NHIS_OOP_Ghana_Dashboard.html for the standalone static dashboard.
"""
import dash
from dash import html, dcc

app = dash.Dash(__name__, title="NHIS Uninsurance Ghana")
server = app.server

app.layout = html.Div([
    html.H1("NHIS Uninsurance & Health Equity — Ghana 261 Districts"),
    html.P("Interactive spatial analysis of district-level health insurance inequities."),
    html.P([
        "For the standalone dashboard, open ",
        html.Code("dashboard/NHIS_OOP_Ghana_Dashboard.html"),
        " in your browser.",
    ]),
])

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8050)
