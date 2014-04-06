# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blanketing'
        db.create_table('horses_blanketing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('horse_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('instructions', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('horses', ['Blanketing'])


    def backwards(self, orm):
        # Deleting model 'Blanketing'
        db.delete_table('horses_blanketing')


    models = {
        'horses.blanketing': {
            'Meta': {'object_name': 'Blanketing'},
            'horse_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {})
        },
        'horses.feedings': {
            'Meta': {'object_name': 'Feedings'},
            'beet_pulp': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'f_am': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'f_pm': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'feed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hay': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'horse_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '6', 'default': "'STALLS'"}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rice_bran': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'supplements': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'turnout': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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