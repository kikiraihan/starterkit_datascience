def plotly_graph(G, isShowlegend=False):
    # G = _set_networkx_graph(df_node, df_edge)
    pos = nx.nx_agraph.graphviz_layout(G, prog="neato", args="")
    # pos = nx.spring_layout

    # buat tracer graph. tracer adalah titik2, kalo edge titik yang jadi garis
    edge_trace, node_trace= _buat_tracer(G,pos)

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title='Network graph made with Python',
            titlefont_size=16,
            showlegend=isShowlegend,
            hovermode='closest',
            margin={
                'b':20,'l':5,'r':5,'t':40
            },
            annotations=[{
                "text":"Insect-virus-plant",
                'showarrow':False,
                'xref':"paper", 
                'yref':"paper",
                'x':0.005, 
                'y':-0.002 
            }],
            xaxis={'showgrid':False, 'zeroline':False, 'showticklabels':False},
            yaxis={'showgrid':False, 'zeroline':False, 'showticklabels':False}
        )
    )

    # return fig.to_html(full_html=False) #, include_plotlyjs='cdn'
    return fig.show()

# tidak terpakai
def _buat_tracer(G,pos):
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line= {"width":0.5, "color":'#888'},
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    node_colors = []
    node_text = []
    for node,data in G.nodes(data=True):
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_colors.append(data['color'])
        node_text.append(data['label'])

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker={
            'reversescale':True,
            'color':[],
            'size':10,
            'line_width':2   
        }
    )
    node_trace.marker.color = node_colors
    node_trace.text = node_text
    
    return edge_trace, node_trace