# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

#from address import AddressTestCase
#from auth import AuthTestCase

from trytond.config import config

# Use NereidModuleTestCase as a wrapper for ModuleTestCase
from nereid.testing import NereidModuleTestCase

#from country import CountryTestCase

FROM = 'no-reply@localhost'


##########################
import base64
import json
import unittest
import urllib.error
import urllib.parse
import urllib.request

from unittest.mock import ANY, patch

import trytond.tests.test_tryton

from trytond.config import config
from trytond.model.modelsql import SQLConstraintError
from trytond.modules.nereid_base import user as user_module
from trytond.pool import Pool
from trytond.sendmail import get_smtp_server
from trytond.tests.test_tryton import with_transaction
from trytond.transaction import Transaction

from nereid.testing import POOL as pool
from nereid.testing import NereidTestCase

from common import setup_objects
from getpass import getuser

FROM = 'no-reply@localhost'
#FROM = getuser()


#############################




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

        trytond.tests.test_tryton.activate_module('nereid_base')
        setup_objects(self)
        self.templates = {
            'home.jinja': '{{get_flashed_messages()}}',
            'login.jinja':
            '{{ login_form.errors }} {{get_flashed_messages()}}',
            'registration.jinja':
            '{{ form.errors }} {{get_flashed_messages()}}',
            'reset-password.jinja': '{{get_flashed_messages()}}',
            'change-password.jinja':
            '''{{ change_password_form.errors }}
            {{get_flashed_messages()}}''',
            'address-edit.jinja': 'Address Edit {{ form.errors }}',
            'address.jinja': '',
            'account.jinja': '',
            'profile.jinja': '{{ current_user.name }}',
            'emails/activation-text.jinja': 'activation-email-text',
            'emails/activation-html.jinja': 'activation-email-html',
            'emails/reset-text.jinja': 'reset-email-text',
            'emails/reset-html.jinja': 'reset-email-html',
            }

    def setup_defaults(self):
        """
        Setup the defaults
        """
        usd, = self.currency_obj.create([{
            'name': 'US Dollar',
            'code': 'USD',
            'symbol': '$',
            }])
        self.party, = self.party_obj.create([{
            'name': 'MBSolutions',
            }])
        self.company, = self.company_obj.create([{
            'party': self.party,
            'currency': usd,
            }])

        en, = self.language_obj.search([('code', '=', 'en')])
        currency, = self.currency_obj.search([('code', '=', 'USD')])
        locale, = self.nereid_website_locale_obj.create([{
            'code': 'en',
            'language': en,
            'currency': currency,
            }])
        self.nereid_website_obj.create([{
            'name': 'localhost',
            'company': self.company,
            'application_user': 1,
            'default_locale': locale,
            }])

    def get_template_source(self, name):
        """
        Return templates
        """

        return self.templates.get(name)

    @with_transaction()
    def test_0010_register(self):
        #def test_0010_register(self, get_smtp_server):
        """
        Registration must create a new party
        """
        self.setup_defaults()
        app = self.get_app()
        with patch.object(
                user_module, 'sendmail_transactional') as sendmail, \
                patch.object(user_module, 'SMTPDataManager') as dm, \
                app.test_client() as c:
            print('****************', config.get('email', 'from'))
            response = c.get('/registration')
            self.assertEqual(response.status_code, 200)   # GET Request

            email_user = 'regd_user@m9s.biz'
            data = {
                'name': 'Registered User',
                'email': email_user,
                'password': 'password'
            }
            # Post with missing password
            response = c.post('/registration', data=data)
            self.assertEqual(response.status_code, 200)  # Form rejected

            # Test that NO email was sent
            sendmail.assert_not_called()

            data['confirm'] = 'password'
            response = c.post('/registration', data=data)
            self.assertEqual(response.status_code, 302)

            # Test if an email was sent
            print(sendmail.call_args)
            print(dm.call_args)
            sendmail.assert_called_once_with(
                FROM, email_user, ANY,
                datamanager=ANY)
            _, _, msg = sendmail.call_args[0]
            self.assertEqual(msg['From'], FROM)
            self.assertEqual(msg['Subject'], 'Account Activation')
            self.assertEqual(msg['To'], email_user)
            self.assertEqual(msg.get_content_type(), 'multipart/alternative')
            self.assertEqual(
                msg.get_payload(0).get_payload(), 'activation-email-text')

        parties = self.party_obj.search([('name', '=', data['name'])])

        self.assertEqual(len(parties), 1)
        self.assertEqual(len(parties[0].contact_mechanisms), 1)
        self.assertEqual(parties[0].contact_mechanisms[0].type, 'email')
        self.assertEqual(parties[0].contact_mechanisms[0].value,
            'regd_user@m9s.biz')

        with Transaction().set_context(active_test=False):
            self.assertEqual(self.nereid_user_obj.search(
                    [('email', '=', data['email'].lower())], count=True), 1)

        # Try to register the same user again (no activated user yet)
        response = c.post('/registration', data=data)
        self.assertEqual(response.status_code, 302)
        with Transaction().set_context(active_test=False):
            self.assertEqual(self.nereid_user_obj.search(
                    [('email', '=', data['email'].lower())], count=True), 2)

        # Activate one of the users
        with Transaction().set_context(active_test=False):
            user1, user2 = self.nereid_user_obj.search([
                    ('email', '=', data['email'].lower())
                    ])
        user1.active = True
        user1.email_verified = True
        user1.save()
        # Account of user1 must be activated
        self.assertTrue(user1.active)
        self.assertTrue(user1.email_verified)
        self.assertEqual(self.nereid_user_obj.search([
                    ('email', '=', data['email'].lower()),
                    ], count=True), 1)

        # Try to activate the second user
        user2.active = True
        user2.email_verified = True
        with self.assertRaises(SQLConstraintError) as cm:
            user2.save()
        self.assertEqual(cm.exception.code, 1)
        self.assertTrue("Email must be unique in a company" in
            cm.exception.message)

        # Try to register the same user again (activated user present)
        response = c.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("A registration already exists with this email" in
            response.data.decode('utf-8'))

        # Deactivate (block) the user
        user1.active = False
        user1.save()
        # Account of user1 must be deactivated (blocked)
        self.assertFalse(user1.active)
        self.assertTrue(user1.email_verified)

        # Try to register the same user again (blocked user present)
        response = c.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("A registration already exists with this email" in
            response.data.decode('utf-8'))




del NereidModuleTestCase
