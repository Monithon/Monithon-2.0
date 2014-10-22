# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.description'
        db.add_column(u'projects_project', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Good.description'
        db.add_column(u'projects_good', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Monitorable.description'
        db.delete_column(u'projects_monitorable', 'description')


    def backwards(self, orm):
        # Deleting field 'Project.description'
        db.delete_column(u'projects_project', 'description')

        # Deleting field 'Good.description'
        db.delete_column(u'projects_good', 'description')

        # Adding field 'Monitorable.description'
        db.add_column(u'projects_monitorable', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    models = {
        u'projects.geo': {
            'Meta': {'object_name': 'Geo'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'projects.good': {
            'Meta': {'object_name': 'Good', '_ormbases': [u'projects.Monitorable']},
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'monitorable_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.Monitorable']", 'unique': 'True', 'primary_key': 'True'}),
            'paid_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'paid_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'projects.layer': {
            'Meta': {'object_name': 'Layer'},
            'icon': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'layers'", 'symmetrical': 'False', 'to': u"orm['projects.Monitorable']"})
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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.MonitorableCategory']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Location']", 'symmetrical': 'False'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Subject']", 'symmetrical': 'False'})
        },
        u'projects.monitorablecategory': {
            'Meta': {'object_name': 'MonitorableCategory'},
            'icon': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project', '_ormbases': [u'projects.Monitorable']},
            'cup': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
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
        u'projects.tags': {
            'Meta': {'object_name': 'Tags'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'tagtype': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']