from collections import namedtuple
from clint.textui import colored

Style = namedtuple('Style', ['success', 'fail',])

colors = Style(success=colored.green,
               fail=colored.red)

def run():
    print("Running.............", colors.success('ok'))
