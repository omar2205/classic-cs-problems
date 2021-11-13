## Follows Classic CS Problems

Follows Classic Computer Science Problems With Python

By David Kopec

### Import a module

Bad practice, but to import a module named like this
1.fib.py

```py
import importlib.util
import sys

module_name = '1.fib.py'
file_path = '/path/to/module/1.fib.py'

spec = importlib.util.spec_from_file_location(module_name, file_path)
fib = importlib.util.module_from_spec(spec) # change module to any name
sys.modules['1.fib.py'] = fib
spec.loader.exec_module(fib)
```
