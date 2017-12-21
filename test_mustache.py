import pystache

mustache_file = "svg.html.mustache"

circles = []
for i in range(0, 10):
    circles.append({'x': 100 + i * 70, 'y': 100, 'r': 15 + float(i) * 1.5, 'color': '#ffff00'})

template_data = {'circles': circles}

renderer = pystache.Renderer(missing_tags='strict')
svg_text = renderer.render_path(mustache_file, template_data)

f = open('circles_svg.html', 'w')
f.write(str(svg_text))
f.close()
