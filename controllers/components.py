# -*- coding: utf-8 -*-
# try something like
panel_rows = 4
panel_columns = 4
height = width = 100


def Panel():
    images = db().select(db.image.ALL, orderby=db.image.x|db.image.y)
    return dict(panel_rows=panel_rows,
                 panel_columns=panel_columns,
                 height=height,
                 width=width,
                 images=images)

def empty_panel():
    return dict(quilt_column=request.vars['col'],
                 panel_rows=panel_rows,
                 panel_columns=panel_columns,
                 height=height,
                 width=width,
                 images=None)

def row():
    import math
    num_panels = math.ceil(float(request.vars['width']) / (panel_rows * width))
    return dict(quilt_row=request.args(0),panels=int(num_panels))

def col():
    return dict(quilt_column=request.args(0))
