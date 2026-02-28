import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
# Cargar datos procesados
df = pd.read_csv("data/clean_sales.csv")
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Dropdown(
        id="region-filter",
        options=[{"label": r, "value": r} for r in df["region"].unique()],
        value=df["region"].unique()[0]
    ),
    dcc.Graph(id="revenue-chart"),
    dcc.Graph(id="product-chart")
])

@app.callback(
    Output("revenue-chart", "figure"),
    Output("product-chart", "figure"),
    Input("region-filter", "value")
)
def update_dashboard(selected_region):
    filtered_df = df[df["region"] == selected_region]
    # Revenue over time
    revenue_fig = px.scatter(
        filtered_df,
        x="date",
        y="total_sale",
        title=f"Revenue Over Time - {selected_region}"
    )
    # Sales by product
    product_fig = px.bar(
        filtered_df.groupby("product")["total_sale"].sum().reset_index(),
        x="product",
        y="total_sale",
        title="Revenue by Product"
    )
    return revenue_fig, product_fig

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)