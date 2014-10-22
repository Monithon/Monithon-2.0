# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Report'
        db.create_table(u'reports_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports', to=orm['monitor.MonitoringTeam'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports', to=orm['projects.Project'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Report'])

        # Adding model 'ReportForm'
        db.create_table(u'reports_reportform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(related_name='forms', to=orm['reports.Report'])),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customforms.Form'])),
        ))
        db.send_create_signal(u'reports', ['ReportForm'])

        # Adding model 'ReportFormField'
        db.create_table(u'reports_reportformfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report_form', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fields', to=orm['reports.ReportForm'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customforms.FormField'])),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'reports', ['ReportFormField'])


    def backwards(self, orm):
        # Deleting model 'Report'
        db.delete_table(u'reports_report')

        # Deleting model 'ReportForm'
        db.delete_table(u'reports_reportform')

        # Deleting model 'ReportFormField'
        db.delete_table(u'reports_reportformfield')


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
        u'monitor.monitoringteam': {
            'Meta': {'object_name': 'MonitoringTeam'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'projects.geo': {
            'Meta': {'object_name': 'Geo'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'projects.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mun': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mun'", 'null': 'True', 'to': u"orm['projects.Geo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'nat'", 'null': 'True', 'to': u"orm['projects.Geo']"}),
            'pro': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pro'", 'null': 'True', 'to': u"orm['projects.Geo']"}),
            'reg': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reg'", 'null': 'True', 'to': u"orm['projects.Geo']"}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'projects.monitorable': {
            'Meta': {'object_name': 'Monitorable'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Location']", 'symmetrical': 'False'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Subject']", 'symmetrical': 'False'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project', '_ormbases': [u'projects.Monitorable']},
            'cup': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'monitorable_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.Monitorable']", 'unique': 'True', 'primary_key': 'True'}),
            'oc_slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'oc_url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'paid_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'paid_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'projects.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400'})
        },
        u'reports.report': {
            'Meta': {'object_name': 'Report'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': u"orm['monitor.MonitoringTeam']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': u"orm['projects.Project']"})
        },
        u'reports.reportform': {
            'Meta': {'object_name': 'ReportForm'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customforms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'forms'", 'to': u"orm['reports.Report']"})
        },
        u'reports.reportformfield': {
            'Meta': {'object_name': 'ReportFormField'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customforms.FormField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report_form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': u"orm['reports.ReportForm']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['reports']