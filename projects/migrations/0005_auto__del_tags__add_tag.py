# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Tags'
        db.delete_table(u'projects_tags')

        # Adding model 'Tag'
        db.create_table(u'projects_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('tagtype', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=400, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Tag'])

        # Adding M2M table for field tags on 'Monitorable'
        m2m_table_name = db.shorten_name(u'projects_monitorable_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('monitorable', models.ForeignKey(orm[u'projects.monitorable'], null=False)),
            ('tag', models.ForeignKey(orm[u'projects.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['monitorable_id', 'tag_id'])


    def backwards(self, orm):
        # Adding model 'Tags'
        db.create_table(u'projects_tags', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=400, null=True, blank=True)),
            ('tagtype', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'projects', ['Tags'])

        # Deleting model 'Tag'
        db.delete_table(u'projects_tag')

        # Removing M2M table for field tags on 'Monitorable'
        db.delete_table(db.shorten_name(u'projects_monitorable_tags'))


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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Tag']", 'null': 'True', 'blank': 'True'}),
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
        u'projects.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'tagtype': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']