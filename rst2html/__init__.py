__all__ = ['rst2html']

from contextlib import redirect_stderr
import io

import docutils.core


def rst2html(rst, report_level=None):
    kwargs = {
        'writer_name': 'html',
        'settings_overrides': {
            '_disable_config': True,
            'report_level': int(report_level) if report_level else 0
        }
    }
    target = io.StringIO()
    with redirect_stderr(target):
        parts = docutils.core.publish_parts(rst, **kwargs)
        html = parts['html_body']
        warning = target.getvalue().strip()
        return html, warning
