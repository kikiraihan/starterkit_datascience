import networkx as nx
import plotly.graph_objs as go
import plotly.io as pio

# Mendapatkan posisi node
pos = nx.spring_layout(G)

# buat tracer
# Membuat edge trace
edge_x = []
edge_y = []

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1.5, color='#888'),
    hoverinfo='none',
    mode='lines'
)

# Membuat node trace
node_x = []
node_y = []
node_colors = []
node_text = []

for node in G.nodes(data=True):
    x, y = pos[node[0]]
    node_x.append(x)
    node_y.append(y)
    # node_colors.append(node[1]['color'])
    # node_text.append(node[1]['label'])

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    # hoverinfo='text',
    marker=dict(
        reversescale=True,
        # color=node_colors,
        size=10,
        line_width=2),
    # text=node_text
)

# Membuat figure dan plot
fig = go.Figure(
    data=[edge_trace, node_trace],
    layout=go.Layout(
        title='Graph Visualization',
        titlefont=dict(size=16),
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=5, r=5, t=40),
        annotations=[dict(
            text="Coba plotly",
            showarrow=False,
            xref="paper", yref="paper",
            x=0.005, y=-0.002
        )],
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    ))


# Menyimpan visualisasi ke file HTML
pio.write_html(fig, file='graph_plotly.html', auto_open=False)