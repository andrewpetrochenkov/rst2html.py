__all__ = ['rst2html']

import docutils.core


def rst2html(rst):
    kwargs = {
        'writer_name': 'html',
        'settings_overrides': {
            '_disable_config': True,
            'report_level': 5
        }
    }
    parts = docutils.core.publish_parts(rst, **kwargs)
    return parts['html_body']


rst = """
*****
Title
*****

subtitle
########

subsubtitle
**********************
and so on
"""
print(rst2html(rst))
