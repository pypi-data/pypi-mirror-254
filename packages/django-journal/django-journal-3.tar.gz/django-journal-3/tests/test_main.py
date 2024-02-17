import pytest
from django.contrib.auth.models import Group, User
from django.db import transaction
from django.test import TestCase
from django.utils.encoding import force_text

from django_journal.actions import export_as_csv_generator
from django_journal.journal import error_record, record
from django_journal.models import Journal, Tag


class JournalTestCase(TestCase):
    def setUp(self):
        self.users = []
        self.groups = []
        with transaction.atomic():
            for i in range(20):
                self.users.append(User.objects.create(username='user%s' % i))
            for i in range(20):
                self.groups.append(Group.objects.create(name='group%s' % i))
            for i in range(20):
                record('login', '{user} logged in', user=self.users[i])
            for i in range(20):
                record(
                    'group-changed',
                    '{user1} gave group {group} to {user2}',
                    user1=self.users[i],
                    group=self.groups[i],
                    user2=self.users[(i + 1) % 20],
                )
            for i in range(20):
                record('logout', '{user} logged out', user=self.users[i])

    def test_login(self):
        for i, event in zip(range(20), Journal.objects.for_tag('login').order_by('id')):
            self.assertEqual(force_text(event), f'user{i} logged in')

    def test_groups(self):
        for i, event in zip(range(40), Journal.objects.for_tag('group-changed').order_by('id')):
            self.assertEqual(
                force_text(event), 'user{0} gave group group{0} to user{1}'.format(i, (i + 1) % 20)
            )

    def test_logout(self):
        for i, event in zip(range(20), Journal.objects.for_tag('logout').order_by('id')):
            self.assertEqual(force_text(event), f'user{i} logged out')

    def test_export_as_csv(self):
        qs = Journal.objects.all()
        l = list(export_as_csv_generator(qs))
        self.assertEqual(
            set(l[0]),
            {
                'time',
                'tag',
                'message',
                'group',
                'group__id',
                'user',
                'user__id',
                'user1',
                'user1__id',
                'user2',
                'user2__id',
            },
        )
        l = list(export_as_csv_generator(qs[:5]))
        self.assertEqual(set(l[0]), {'time', 'tag', 'message', 'user', 'user__id'})
        for user in self.users:
            user.delete()
        qs = Journal.objects.all()
        l = list(export_as_csv_generator(qs))
        self.assertEqual(l[1]['user'], '<deleted>')


@pytest.mark.django_db(databases=['default', 'error'])
def test_error_record(transactional_db):
    error_record('error', 'error message')
    journal = Journal.objects.first()
    assert journal.tag.name == 'error'
    assert journal.message == 'error message'

    # specifying None as database use the defaut one
    error_record('error', 'error message', using=None)
    assert Journal.objects.count() == 2


@pytest.mark.django_db(databases=['default', 'error'])
def test_error_record_with_db_obj(transactional_db):
    tag = Tag.objects.create(name='some-tag')
    journal = error_record('error', 'error message', someobj=tag)
    objdata = journal.objectdata_set.first()
    assert objdata.object_id == tag.pk

    # If journal is not deleted test_export_as_csv crashes
    # probably some db rollback not done since error_record
    # uses a different db router
    # to be investigated
    journal.delete()
