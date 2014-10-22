# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Report.project'
        db.alter_column(u'reports_report', 'project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Monitorable']))

    def backwards(self, orm):

        # Changing field 'Report.project'
        db.alter_column(u'reports_report', 'project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project']))

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
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': u"orm['projects.Monitorable']"})
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