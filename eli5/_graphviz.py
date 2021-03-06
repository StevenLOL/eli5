# -*- coding: utf-8 -*-
import graphviz


def is_supported():
    try:
        graphviz.Graph().pipe('svg')
        return True
    except RuntimeError:
        return False


def dot2svg(dot):
    """ Render Graphviz data to SVG """
    svg = graphviz.Source(dot).pipe(format='svg').decode('utf8')
    # strip doctype and xml declaration
    svg = svg[svg.index('<svg'):]
    return svg
