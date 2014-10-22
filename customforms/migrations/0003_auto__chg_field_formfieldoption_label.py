# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FormFieldOption.label'
        db.alter_column(u'customforms_formfieldoption', 'label', self.gf('django.db.models.fields.CharField')(max_length=5000))

    def backwards(self, orm):

        # Changing field 'FormFieldOption.label'
        db.alter_column(u'customforms_formfieldoption', 'label', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'customforms.form': {
            'Meta': {'object_name': 'Form'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'customforms.formfield': {
            'Meta': {'object_name': 'FormField'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'customforms.formfieldoption': {
            'Meta': {'ordering': "['weight']", 'object_name': 'FormFieldOption'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': u"orm['customforms.Form']"}),
            'form_field': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'config'", 'to': u"orm['customforms.FormField']"}),
            'hint': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'list_field': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obligatory': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        }
    }

    complete_apps = ['customforms']