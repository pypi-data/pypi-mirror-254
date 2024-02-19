# nano_profiler
Extreme simple profiler of time execution of code.
The major goal of `none_profiler` is simple time measure in long chain of code execution,
such as web applications.

## Quick example

```python
from time import sleep

from nano_profiler import NanoProfiler

n_p = NanoProfiler(name='Foo Bar Baz profiler', autostart=True)

def foo():
    sleep(0.1)
    n_p.mark('Foo')

def bar():
    sleep(0.125)
    n_p.mark('Bar')

def baz():
    foo()
    bar()
    n_p.mark('Baz')

baz()
```

Output:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Statistic of profiler "Foo Bar Baz" ┃
┡━━━┯━━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━━━━━┦
│ 1 │ 0.100s │  44.45% │ Foo          │
├───┼────────┼─────────┼──────────────┤
│ 2 │ 0.125s │  55.55% │ Bar          │
├───┼────────┼─────────┼──────────────┤
│ 3 │ 0.000s │   0.00% │ Baz          │
┢━━━╈━━━━━━━━╈━━━━━━━━━╈━━━━━━━━━━━━━━┪
┃   ┃ 0.225s ┃ 100.00% ┃ Total        ┃
┗━━━┻━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━━━━━━┛
```
