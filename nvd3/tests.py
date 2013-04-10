from common.utils import BaseAuthenticatedClient
from nvd3.views import somemethod


class NVD3View(BaseAuthenticatedClient):
    """Test Function to check ..."""

    def test_writetest(self):
        """Test Function to check"""
        self.assertEqual(1, 4)
