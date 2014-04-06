# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Placement'
        db.create_table('horses_placement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('front_pasture', self.gf('django.db.models.fields.TextField')()),
            ('back_pasture', self.gf('django.db.models.fields.TextField')()),
            ('pony_pasture', self.gf('django.db.models.fields.TextField')()),
            ('stalls', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('horses', ['Placement'])


    def backwards(self, orm):
        # Deleting model 'Placement'
        db.delete_table('horses_placement')


    models = {
        'horses.horse': {
            'Meta': {'object_name': 'Horse'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'breed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'feet': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inches': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '6'})
        },
        'horses.placement': {
            'Meta': {'object_name': 'Placement'},
            'back_pasture': ('django.db.models.fields.TextField', [], {}),
            'front_pasture': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pony_pasture': ('django.db.models.fields.TextField', [], {}),
            'stalls': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['horses']