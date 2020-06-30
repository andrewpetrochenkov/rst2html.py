<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/django-template-cli.svg?maxAge=3600)](https://pypi.org/project/django-template-cli/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-template-cli.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-template-cli.py/actions)

### Installation
```bash
$ [sudo] pip install django-template-cli
```

#### How it works
```
index.html
context.json (optional)
```

#### Examples
`index.html`:
```html
{% for v in values %}
{{ forloop.counter0 }}: {{ v }}
{% endfor %}
```

`context.json`:
```json
{
    "values": ["value1","value2","value3"]
}
```

```bash
$ django-template-cli index.html
0: value1

1: value2

2: value3
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>