# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactInfo'
        db.create_table('customers_contactinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('City', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('State', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')()),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone_num', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('customers', ['ContactInfo'])

        # Adding model 'Owners'
        db.create_table('customers_owners', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_info', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['customers.ContactInfo'], unique=True)),
            ('vet_pref', self.gf('django.db.models.fields.TextField')()),
            ('farrier_pref', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('customers', ['Owners'])

        # Adding model 'Boarders'
        db.create_table('customers_boarders', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('boarder', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('checks_paid', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_info', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['customers.ContactInfo'], unique=True)),
            ('liab_waivers', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('customers', ['Boarders'])


    def backwards(self, orm):
        # Deleting model 'ContactInfo'
        db.delete_table('customers_contactinfo')

        # Deleting model 'Owners'
        db.delete_table('customers_owners')

        # Deleting model 'Boarders'
        db.delete_table('customers_boarders')


    models = {
        'customers.boarders': {
            'Meta': {'object_name': 'Boarders'},
            'boarder': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'checks_paid': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_info': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['customers.ContactInfo']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liab_waivers': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'customers.contactinfo': {
            'City': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'ContactInfo'},
            'State': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_num': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {})
        },
        'customers.owners': {
            'Meta': {'object_name': 'Owners'},
            'contact_info': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['customers.ContactInfo']", 'unique': 'True'}),
            'farrier_pref': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vet_pref': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['customers']