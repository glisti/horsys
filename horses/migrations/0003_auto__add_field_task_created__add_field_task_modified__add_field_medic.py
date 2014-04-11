# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Task.created'
        db.add_column(u'horses_task', 'created',
                      self.gf('horses.models.AutoDateTimeField')(default=datetime.datetime(2014, 4, 10, 0, 0)),
                      keep_default=False)

        # Adding field 'Task.modified'
        db.add_column(u'horses_task', 'modified',
                      self.gf('horses.models.AutoDateTimeField')(default=datetime.datetime(2014, 4, 10, 0, 0)),
                      keep_default=False)

        # Adding field 'MedicalRecord.created'
        db.add_column(u'horses_medicalrecord', 'created',
                      self.gf('horses.models.AutoDateTimeField')(default=datetime.datetime(2014, 4, 10, 0, 0)),
                      keep_default=False)

        # Adding field 'MedicalRecord.modified'
        db.add_column(u'horses_medicalrecord', 'modified',
                      self.gf('horses.models.AutoDateTimeField')(default=datetime.datetime(2014, 4, 10, 0, 0)),
                      keep_default=False)

        # Adding field 'Note.created'
        db.add_column(u'horses_note', 'created',
                      self.gf('horses.models.AutoDateTimeField')(default=datetime.datetime(2014, 4, 10, 0, 0)),
                      keep_default=False)

        # Adding field 'Horse.created'
        db.add_column(u'horses_horse', 'created',
                      self.gf('horses.models.AutoDateTimeField')(default=datetime.datetime(2014, 4, 10, 0, 0)),
                      keep_default=False)

        # Adding field 'Horse.modified'
        db.add_column(u'horses_horse', 'modified',
                      self.gf('horses.models.AutoDateTimeField')(default=datetime.datetime(2014, 4, 10, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Task.created'
        db.delete_column(u'horses_task', 'created')

        # Deleting field 'Task.modified'
        db.delete_column(u'horses_task', 'modified')

        # Deleting field 'MedicalRecord.created'
        db.delete_column(u'horses_medicalrecord', 'created')

        # Deleting field 'MedicalRecord.modified'
        db.delete_column(u'horses_medicalrecord', 'modified')

        # Deleting field 'Note.created'
        db.delete_column(u'horses_note', 'created')

        # Deleting field 'Horse.created'
        db.delete_column(u'horses_horse', 'created')

        # Deleting field 'Horse.modified'
        db.delete_column(u'horses_horse', 'modified')


    models = {
        u'horses.horse': {
            'Meta': {'object_name': 'Horse'},
            'am_amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'beet_pulp': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'blanketing_instructions': ('django.db.models.fields.TextField', [], {}),
            'created': ('horses.models.AutoDateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hay': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'STALLS'", 'max_length': '6'}),
            'modified': ('horses.models.AutoDateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pm_amount': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rice_bran': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'supplements': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'turnout': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'horses.medicalrecord': {
            'Meta': {'object_name': 'MedicalRecord'},
            'created': ('horses.models.AutoDateTimeField', [], {}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['horses.Horse']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('horses.models.AutoDateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'horses.note': {
            'Meta': {'object_name': 'Note'},
            'created': ('horses.models.AutoDateTimeField', [], {}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['horses.Horse']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'horses.task': {
            'Meta': {'object_name': 'Task'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('horses.models.AutoDateTimeField', [], {}),
            'horse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['horses.Horse']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('horses.models.AutoDateTimeField', [], {}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'task': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['horses']