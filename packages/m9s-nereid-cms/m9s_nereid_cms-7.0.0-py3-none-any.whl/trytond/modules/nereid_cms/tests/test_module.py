# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase


class NereidCmsTestCase(ModuleTestCase):
    "Test Nereid Cms module"
    module = 'nereid_cms'


del ModuleTestCase
