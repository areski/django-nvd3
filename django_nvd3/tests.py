from templatetags.nvd3_tags import load_chart, include_nvd3jscss, include_container
import unittest


class NVD3TemplateTagsTestCase(unittest.TestCase):

    def testPiechart(self):
        xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
        ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "pieChart"

        self.assertTrue(load_chart(charttype, chartdata, 'container', y_is_date=False))
        self.assertTrue(include_nvd3jscss())
        self.assertTrue(include_container('container', height=400, width=600))


if __name__ == '__main__':
    unittest.main()
