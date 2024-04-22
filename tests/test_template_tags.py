import unittest


import django
from django.template import (
    Context,
    Template
)
django.setup()
from django.test.utils import override_settings
try:
    from django.template.base import add_to_builtins
except ImportError:
    # django >= 1.9
    def add_to_builtins(module):
        from django.template.engine import Engine
        template_engine = Engine.get_default()
        template_engine.builtins.append(module)
        template_engine.template_builtins = \
            template_engine.get_template_builtins(template_engine.builtins)

from django_nvd3.templatetags.nvd3_tags import load_chart, include_container


class NVD3TemplateTagsTestCase(unittest.TestCase):

    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def testPiechart(self):
        xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries",
                 "Dates", "Grapefruit", "Kiwi", "Lemon"]
        ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "pieChart"
        extra = {'y_is_date': False}

        self.assertTrue(load_chart(charttype, chartdata, 'container', extra))
        self.assertTrue(include_container('container', height=400, width=600))

    @override_settings(STATIC_URL='/static/')
    def test_include_chart_jscss_tag_custom_dirs(self):
        add_to_builtins('django_nvd3.templatetags.nvd3_tags')

        rendered = self.render_template(
            "{% include_chart_jscss css_dir='css' js_dir='js' %}"
        )

        # Not only does this test the output of the template tag,
        # but also the order of including the static files - mainly
        # d3 and nvd3 js files which should be in that order.
        expected = (
            '<link media="all" href="/static/css/nv.d3.min.css" '
            'type="text/css" rel="stylesheet" />\n'
            '<script src="/static/js/d3.min.js" '
            'type="text/javascript" charset="utf-8"></script>\n'
            '<script src="/static/js/nv.d3.min.js" '
            'type="text/javascript" charset="utf-8"></script>\n\n'
        )
        self.assertEqual(rendered, expected)


if __name__ == '__main__':
    unittest.main()
