# [vdomify](https://github.com/rgbkrk/vdomify)

Convert plain ol' Python objects to VDOM ready objects

Note: the library isn't ready yet, this is README driven development

## Why use vdomify?

When you want a handy utility to convert python objects to vdom components.

```python
from vdomify import vdomify

display(
    vdomify({
      'test': True
    })
)
```

## Install the Python package

```bash
pip install vdomify
```

## Developer install from source code

```bash
git clone https://github.com/rgbkrk/vdomify
cd vdomify
pip install -e .
```

## We welcome feedback.

Since this project and its API is still a work in progress, we would love to
hear your thoughts on the API and suggestions for enhancements. 
