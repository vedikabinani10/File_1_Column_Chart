import pandas as pd
import plotly.graph_objects as go

# Load data
df = pd.read_excel('File2.xlsx')

# Station columns
station_cols = ['Bakersfield Golden CAMP PA A', 'Bakersfield Golden CAMP PA B',
                'Sunview A', 'Sunview B', '6D A', '6D B']

# Format date
df['DateTime'] = pd.to_datetime(df['DateTime']).dt.strftime('%m/%Y')

# Colors for each station
colors = ['#1f77b4','#aec7e8','#ff7f0e','#ffbb78','#2ca02c','#98df8a']

fig = go.Figure()

for col, color in zip(station_cols, colors):
    fig.add_trace(go.Scatter(
        x=df['DateTime'],
        y=df[col],
        mode='lines+markers',
        name=col,
        line=dict(color=color, width=2),
        marker=dict(size=5)
    ))

fig.update_layout(
    title='Air Quality Index by Station',
    xaxis_title='Month/Year',
    yaxis_title='AQI (PM2.5)',
    hovermode='x unified',
    yaxis=dict(
        dtick=200,
        range=[0, max(df[station_cols].max().max() + 200, 200)]
    ),
    width=1200,
    height=600,
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='center',
        x=0.5
    )
)

fig.write_html('AQI_chart.html',
    include_plotlyjs='cdn',
    full_html=False,
    default_width='100%',
)

fig.show(config={
    'scrollZoom': True,
    'displayModeBar': True,
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'AQI_chart',
        'height': 600,
        'width': 1200,
        'scale': 2
    }
})