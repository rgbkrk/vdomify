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

## Welcoming feedback

Since this project and its API are still a work in progress, I would love to
hear your thoughts on the API and suggestions for enhancements. PRs likely\* accepted
quickly, as this is not intended to be as stringent as `vdom`.

\* for some value of likely

