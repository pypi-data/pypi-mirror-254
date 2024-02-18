# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

#from address import AddressTestCase
from auth import AuthTestCase

from trytond.config import config

# Use NereidModuleTestCase as a wrapper for ModuleTestCase
from nereid.testing import NereidModuleTestCase

#from country import CountryTestCase

FROM = 'no-reply@localhost'

class NereidBaseTestCase(
        NereidModuleTestCase,
        #AuthTestCase,
        #AddressTestCase,
        #CountryTestCase
        ):
    "Test Nereid Base module"
    module = 'nereid_base'

    def setUp(self):
        super().setUp()
        reset_from = config.get('email', 'from', default='')
        config.set('email', 'from', FROM)
        self.addCleanup(lambda: config.set('email', 'from', reset_from))

del NereidModuleTestCase
