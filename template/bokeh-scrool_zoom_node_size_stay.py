# Membuat Graph
g = bplt.from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

# Membuat plot figure
p = bmod.Plot(
    width=800, height=800,
    x_range=bmod.Range1d(-1.1, 1.1), 
    y_range=bmod.Range1d(-1.1, 1.1),
    toolbar_location="above"
)

# Menambahkan tools interaktif termasuk alat zoom
p.add_tools(
    bmod.HoverTool(tooltips=[
        # ("index", "$index"), 
        ("Amount Paid", "@{id_from}"),
        ("Amount Paid", "@{id_to}"),
        ("Receiving Currency", "@{Receiving Currency}"),
        ("Amount Received", "@{Amount Received}"),
        ("Payment Currency", "@{Payment Currency}"),
        ("Payment Format", "@{Payment Format}"),
        ("Is Laundering", "@{Is Laundering}"),
    ]), 
    'reset',
    'pan',
    'box_zoom',
    'wheel_zoom',
    'save',
    bmod.TapTool(), 
    bmod.BoxSelectTool(),
    bmod.PointDrawTool(renderers=[g.node_renderer])  # Menambahkan PointDrawTool
)
p.toolbar.active_scroll = p.select_one(bmod.WheelZoomTool)

# Menambahkan styling
initial_radius = 0.01
g.node_renderer.glyph = bmod.Circle(radius=initial_radius, fill_color='skyblue')
g.node_renderer.hover_glyph = bmod.Circle(radius=initial_radius, fill_color='#24b06c')
g.node_renderer.selection_glyph = bmod.Circle(radius=initial_radius, fill_color='#b09b24')
g.node_renderer.nonselection_glyph = bmod.Circle(radius=initial_radius, fill_color='skyblue')

g.edge_renderer.glyph = bmod.MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=1)
g.edge_renderer.hover_glyph = bmod.MultiLine(line_color="#24b06c", line_alpha=0.8, line_width=1)
g.edge_renderer.selection_glyph = bmod.MultiLine(line_color="#b09b24", line_alpha=0.8, line_width=1)
g.edge_renderer.nonselection_glyph = bmod.MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=1)

g.inspection_policy = bmod.graphs.EdgesAndLinkedNodes() 
g.selection_policy = bmod.graphs.NodesAndLinkedEdges()
# NodesAndLinkedEdges()
#or EdgesAndLinkedNodes()
#NodesAndAdjacentNodes()

# Append graph to plot 
p.renderers.append(g)

# ===========================================================================
# CustomJS callback untuk mengubah ukuran node berdasarkan zoom level
callback = CustomJS(args=dict(g=g, p=p), code="""
    var x_range = p.x_range;
    var y_range = p.y_range;
    var x_span = x_range.end - x_range.start;
    var y_span = y_range.end - y_range.start;
    var zoom_level = Math.max(x_span, y_span);
    var new_radius = zoom_level / 220;

    g.node_renderer.glyph.radius = {value: new_radius};
    g.node_renderer.hover_glyph.radius = {value: new_radius};
    g.node_renderer.selection_glyph.radius = {value: new_radius};
    g.node_renderer.nonselection_glyph.radius = {value: new_radius};
""")

# Menambahkan callback ke x_range dan y_range
p.x_range.js_on_change('start', callback)
p.x_range.js_on_change('end', callback)
p.y_range.js_on_change('start', callback)
p.y_range.js_on_change('end', callback)
# ===========================================================================


# Menyimpan plot ke file HTML
bkio.output_file("graph.html")
bkio.save(p)

# Menampilkan plot
# bk.io.show(p)
