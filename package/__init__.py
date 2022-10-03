print('Hello word')
from .foo import foo
from .baz.operation import minus, division
from .bar.info import log, foo as another_foo

# variant 5 з інформацією в info
__all__ = ['foo', 'division', 'minus', 'log', 'another_foo']
