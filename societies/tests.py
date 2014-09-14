# -*- coding: utf-8 -*-
"""
societies.tests
~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: Proprietary
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import GuitarSociety, Issue

class GuitarSocietyTest(TestCase):

    def test_str_of_guitar_society_returns_name(self):
        gs = GuitarSociety(name='test')
        self.assertEqual('test', str(gs))

    def test_repr_of_guitar_society_returns_class_and_name(self):
        gs = GuitarSociety(name='test')
        self.assertEqual('<GuitarSociety("test")>', repr(gs))


class IssueTest(TestCase):

    def test_str_includes_issue_type_and_society(self):
        gs = GuitarSociety(name='test')
        issue = Issue(issue_type=Issue.BROKEN_LINK, society=gs)
        self.assertEqual('link - test', str(issue))

    def test_repr_includes_issue_type_and_society(self):
        gs = GuitarSociety(name='test')
        issue = Issue(issue_type=Issue.BROKEN_LINK, society=gs)
        self.assertEqual('<Issue("link", <GuitarSociety("test")>)>', repr(issue))


class ViewsTest(TestCase):

    fixtures = ['societies.json']

    def test_society_index_includes_list_of_all_societies(self):
        """Check to make sure a known society is on the page"""
        resp = self.client.get(reverse('societies:index'))
        self.assertContains(resp, 'Guitar Fort Worth', status_code=200)

    def test_society_country_list_includes_correct_societies(self):
        """Check our headine and make sure a known society is on the page"""
        resp  = self.client.get(reverse('societies:country', args=('us',)))
        self.assertContains(resp, 'United States', status_code=200)
        self.assertContains(resp, 'Guitar Fort Worth')

    def test_single_society_redirects_to_society_link(self):
        gs = self._create_society()
        resp = self.client.get(reverse('societies:single', args=(gs.pk,)), follow=False)
        self.assertEqual(302, resp.status_code)
        self.assertTrue(resp['Location'].startswith('http://www.example.com'))

    def test_issue_fetch_shows_form_for_correct_society(self):
        society = self._create_society()
        resp = self.client.get(reverse('societies:issue', args=(society.pk,)))
        self.assertContains(resp, 'test society', status_code=200)

    def test_submit_issue_with_bad_data_shows_error_messages(self):
        society = self._create_society()
        resp = self.client.post(reverse('societies:issue', args=(society.pk,)), {
            'issue_type': 'notvalid',
        })
        self.assertContains(resp, 'Select a valid choice')

    def test_submit_custom_issue_without_description_shows_as_invalid(self):
        society = self._create_society()
        resp = self.client.post(reverse('societies:issue', args=(society.pk,)), {
            'issue_type': Issue.CUSTOM_ISSUE,
        })
        self.assertContains(resp, 'describe the issue')

    def test_submit_issue_with_valid_data_creates_new_issue(self):
        society = self._create_society()
        resp = self.client.post(reverse('societies:issue', args=(society.pk,)), {
            'issue_type': Issue.BROKEN_LINK,
            'description': 'oops',
        }, follow=False)

        issues = Issue.objects.filter(society=society)

        self.assertEqual(302, resp.status_code)
        self.assertGreater(len(issues), 0, 'society should have at least one issue')

    def _create_society(self):
        gs = GuitarSociety(name='test society', country='US', link='http://www.example.com', active=True)
        gs.save()
        return gs
