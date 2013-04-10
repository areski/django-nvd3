from django import template
from django.template.defaultfilters import register
from django.utils import simplejson
from django.utils.safestring import mark_safe
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


@register.assignment_tag(name='load_nvd3')
def load_nvd3(chart_type, series, render_to=''):
    """Loads the ``Chart`` objects in the ``chart_list`` to the
    HTML elements with id's specified in ``render_to``.

    **Arguments**:

    - **render_to** - id where the chart needs to be rendered to.
    """
    js_script = (
        '<script type="text/javascript">\n'
        'var test=1;\n\n'
        'alert(\'NVD3\');\n</script>')
    return mark_safe(js_script)
