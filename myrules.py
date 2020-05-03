# Andrea Diamantini
# my own resT directives

from docutils import nodes
from docutils.parsers.rst import directives

CODE = """\
<iframe width="%(width)s" 
        height="%(height)s" 
        src="https://www.youtube.com/embed/%(yid)s" 
        frameborder="0" 
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen
        style="padding:10px 0px">
</iframe>
"""

def youtube(name, args, options, content, lineno,
            contentOffset, blockText, state, stateMachine):
    if len(content) == 0:
        return
    string_vars = {
        'yid': content[0],
        'width': 600,
        'height': 485
        }
    extra_args = content[1:] # Because content[0] is ID
    extra_args = [ea.strip().split("=") for ea in extra_args] # key=value
    extra_args = [ea for ea in extra_args if len(ea) == 2] # drop bad lines
    extra_args = dict(extra_args)
    if 'width' in extra_args:
        string_vars['width'] = extra_args.pop('width')
    if 'height' in extra_args:
        string_vars['height'] = extra_args.pop('height')
    return [nodes.raw('', CODE % (string_vars), format='html')]

# Take a look here...
youtube.content = True
directives.register_directive('youtube', youtube)

# --------------------------------------------------------------------------------------------------------------

# to draw a stupid horizontal line

def line(name, args, options, content, lineno,
            contentOffset, blockText, state, stateMachine):

    return [nodes.raw('', "<hr>", format='html')]

line.content = False
directives.register_directive('line', line)
