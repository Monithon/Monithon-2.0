# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Deleting model 'Good'
        db.delete_table(u'projects_good')

        # Adding field 'Monitorable.description'
        db.add_column(u'projects_monitorable', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Monitorable.cup'
        db.add_column(u'projects_monitorable', 'cup',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Monitorable.oc_slug'
        db.add_column(u'projects_monitorable', 'oc_slug',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Monitorable.oc_url'
        db.add_column(u'projects_monitorable', 'oc_url',
                      self.gf('django.db.models.fields.URLField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Monitorable.total_amount'
        db.add_column(u'projects_monitorable', 'total_amount',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Monitorable.paid_amount'
        db.add_column(u'projects_monitorable', 'paid_amount',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Monitorable.paid_percent'
        db.add_column(u'projects_monitorable', 'paid_percent',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Monitorable.date_from'
        db.add_column(u'projects_monitorable', 'date_from',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Monitorable.date_to'
        db.add_column(u'projects_monitorable', 'date_to',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'projects_project', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            (u'monitorable_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Monitorable'], unique=True, primary_key=True)),
            ('date_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('paid_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('paid_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('oc_slug', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('date_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cup', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('oc_url', self.gf('django.db.models.fields.URLField')(max_length=400, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding model 'Good'
        db.create_table(u'projects_good', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            (u'monitorable_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Monitorable'], unique=True, primary_key=True)),
            ('date_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('paid_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('paid_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Good'])

        # Deleting field 'Monitorable.description'
        db.delete_column(u'projects_monitorable', 'description')

        # Deleting field 'Monitorable.cup'
        db.delete_column(u'projects_monitorable', 'cup')

        # Deleting field 'Monitorable.oc_slug'
        db.delete_column(u'projects_monitorable', 'oc_slug')

        # Deleting field 'Monitorable.oc_url'
        db.delete_column(u'projects_monitorable', 'oc_url')

        # Deleting field 'Monitorable.total_amount'
        db.delete_column(u'projects_monitorable', 'total_amount')

        # Deleting field 'Monitorable.paid_amount'
        db.delete_column(u'projects_monitorable', 'paid_amount')

        # Deleting field 'Monitorable.paid_percent'
        db.delete_column(u'projects_monitorable', 'paid_percent')

        # Deleting field 'Monitorable.date_from'
        db.delete_column(u'projects_monitorable', 'date_from')

        # Deleting field 'Monitorable.date_to'
        db.delete_column(u'projects_monitorable', 'date_to')


    models = {
        u'projects.geo': {
            'Meta': {'object_name': 'Geo'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.TextField', [], {})
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
            'cup': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Location']", 'null': 'True', 'blank': 'True'}),
            'oc_slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'oc_url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'paid_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'paid_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Subject']", 'null': 'True', 'blank': 'True'}),
            'total_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'projects.monitorablecategory': {
            'Meta': {'object_name': 'MonitorableCategory'},
            'icon': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
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