# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Horse'
        db.create_table(u'logs_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=1023)),
            ('auth', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'logs', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Horse'
        db.delete_table(u'logs_log')


    models = {
        u'logs.log': {
            'Meta': {'object_name': 'Log'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1023'}),
            'auth': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['logs']