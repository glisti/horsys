# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Horse'
        db.create_table(u'horses_horse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('owner_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(default='STALLS', max_length=6)),
            ('feed', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('am_amount', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pm_amount', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('beet_pulp', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('rice_bran', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('supplements', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hay', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('turnout', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('blanketing_instructions', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'horses', ['Horse'])

        # Adding model 'MedicalRecord'
        db.create_table(u'horses_medicalrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('horse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horses.Horse'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'horses', ['MedicalRecord'])


    def backwards(self, orm):
        # Deleting model 'Horse'
        db.delete_table(u'horses_horse')

        # Deleting model 'MedicalRecord'
        db.delete_table(u'horses_medicalrecord')


    models = {
        u'horses.horse': {
            'Meta': {'object_name': 'Horse'},
            'am_amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'beet_pulp': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'blanketing_instructions': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hay': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'STALLS'", 'max_length': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pm_amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rice_bran': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'supplements': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'turnout': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'horses.medicalrecord': {
            'Meta': {'object_name': 'MedicalRecord'},
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['horses.Horse']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['horses']