# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Form'
        db.create_table(u'customforms_form', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'customforms', ['Form'])

        # Adding model 'FormField'
        db.create_table(u'customforms_formfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'customforms', ['FormField'])

        # Adding model 'FormFieldOption'
        db.create_table(u'customforms_formfieldoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fields', to=orm['customforms.Form'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hint', self.gf('django.db.models.fields.TextField')()),
            ('form_field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customforms.FormField'])),
            ('list_field', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('obligatory', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('options', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'customforms', ['FormFieldOption'])


    def backwards(self, orm):
        # Deleting model 'Form'
        db.delete_table(u'customforms_form')

        # Deleting model 'FormField'
        db.delete_table(u'customforms_formfield')

        # Deleting model 'FormFieldOption'
        db.delete_table(u'customforms_formfieldoption')


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
            'Meta': {'object_name': 'FormFieldOption'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': u"orm['customforms.Form']"}),
            'form_field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customforms.FormField']"}),
            'hint': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'list_field': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obligatory': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['customforms']