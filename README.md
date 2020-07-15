<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/rst2html.svg?maxAge=3600)](https://pypi.org/project/rst2html/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/rst2html.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/rst2html.py/actions)

### Installation
```bash
$ [sudo] pip install rst2html
```

#### Examples
```python
from rst2html import rst2html

rst2html('reStructuredText string')
```

catch rst warnings/errors:
```python
from contextlib import redirect_stderr
import io

target = io.StringIO()
with redirect_stderr(target):
    try:
        html, error = rst2html('reStructuredText string'), target.getvalue().strip()
    except Exception as e:
        html, error = 'reStructuredText string', str(e)
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>