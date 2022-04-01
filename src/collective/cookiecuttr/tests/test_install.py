# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import get_installer
from collective.cookiecuttr.testing import\
    COLLECTIVE_COOKIECUTTR_INTEGRATION_TESTING
import unittest


class TestInstall(unittest.TestCase):

    layer = COLLECTIVE_COOKIECUTTR_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal)

    def test_product_is_installed(self):
        """Validate that our products GS profile has been run and the product
           installed
        """
        self.assertTrue(
            self.installer.is_product_installed('collective.cookiecuttr'),
            'package appears not to have been installed',
        )
