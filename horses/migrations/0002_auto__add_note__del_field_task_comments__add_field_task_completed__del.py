# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Note'
        db.create_table(u'horses_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('horse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horses.Horse'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'horses', ['Note'])

        # Deleting field 'Task.comments'
        db.delete_column(u'horses_task', 'comments')

        # Adding field 'Task.completed'
        db.add_column(u'horses_task', 'completed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Horse.notes'
        db.delete_column(u'horses_horse', 'notes')


    def backwards(self, orm):
        # Deleting model 'Note'
        db.delete_table(u'horses_note')

        # Adding field 'Task.comments'
        db.add_column(u'horses_task', 'comments',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Task.completed'
        db.delete_column(u'horses_task', 'completed')

        # Adding field 'Horse.notes'
        db.add_column(u'horses_horse', 'notes',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


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
        },
        u'horses.note': {
            'Meta': {'object_name': 'Note'},
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['horses.Horse']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'horses.task': {
            'Meta': {'object_name': 'Task'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['horses.Horse']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'task': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['horses']