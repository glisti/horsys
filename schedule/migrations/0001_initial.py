# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Log'
        db.create_table(u'schedule_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('auth', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('horse', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'schedule', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Log'
        db.delete_table(u'schedule_log')


    models = {
        u'schedule.log': {
            'Meta': {'object_name': 'Log'},
            'auth': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'horse': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['schedule']