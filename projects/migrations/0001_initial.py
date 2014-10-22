# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Monitorable'
        db.create_table(u'projects_monitorable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'projects', ['Monitorable'])

        # Adding M2M table for field subjects on 'Monitorable'
        m2m_table_name = db.shorten_name(u'projects_monitorable_subjects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('monitorable', models.ForeignKey(orm[u'projects.monitorable'], null=False)),
            ('subject', models.ForeignKey(orm[u'projects.subject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['monitorable_id', 'subject_id'])

        # Adding M2M table for field locations on 'Monitorable'
        m2m_table_name = db.shorten_name(u'projects_monitorable_locations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('monitorable', models.ForeignKey(orm[u'projects.monitorable'], null=False)),
            ('location', models.ForeignKey(orm[u'projects.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['monitorable_id', 'location_id'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'monitorable_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Monitorable'], unique=True, primary_key=True)),
            ('cup', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('oc_slug', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('oc_url', self.gf('django.db.models.fields.URLField')(max_length=400, null=True, blank=True)),
            ('total_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('paid_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('paid_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('date_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding model 'Good'
        db.create_table(u'projects_good', (
            (u'monitorable_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Monitorable'], unique=True, primary_key=True)),
            ('total_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('paid_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('paid_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('date_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Good'])

        # Adding model 'Location'
        db.create_table(u'projects_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('nat', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='nat', null=True, to=orm['projects.Geo'])),
            ('reg', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='reg', null=True, to=orm['projects.Geo'])),
            ('pro', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pro', null=True, to=orm['projects.Geo'])),
            ('mun', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mun', null=True, to=orm['projects.Geo'])),
        ))
        db.send_create_signal(u'projects', ['Location'])

        # Adding model 'Geo'
        db.create_table(u'projects_geo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('code', self.gf('django.db.models.fields.IntegerField')()),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.GeometryField')()),
        ))
        db.send_create_signal(u'projects', ['Geo'])

        # Adding model 'Subject'
        db.create_table(u'projects_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=400)),
        ))
        db.send_create_signal(u'projects', ['Subject'])

        # Adding model 'Tags'
        db.create_table(u'projects_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('tagtype', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=400, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Tags'])

        # Adding model 'Layer'
        db.create_table(u'projects_layer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('icon', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'projects', ['Layer'])

        # Adding M2M table for field projects on 'Layer'
        m2m_table_name = db.shorten_name(u'projects_layer_projects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('layer', models.ForeignKey(orm[u'projects.layer'], null=False)),
            ('monitorable', models.ForeignKey(orm[u'projects.monitorable'], null=False))
        ))
        db.create_unique(m2m_table_name, ['layer_id', 'monitorable_id'])


    def backwards(self, orm):
        # Deleting model 'Monitorable'
        db.delete_table(u'projects_monitorable')

        # Removing M2M table for field subjects on 'Monitorable'
        db.delete_table(db.shorten_name(u'projects_monitorable_subjects'))

        # Removing M2M table for field locations on 'Monitorable'
        db.delete_table(db.shorten_name(u'projects_monitorable_locations'))

        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Deleting model 'Good'
        db.delete_table(u'projects_good')

        # Deleting model 'Location'
        db.delete_table(u'projects_location')

        # Deleting model 'Geo'
        db.delete_table(u'projects_geo')

        # Deleting model 'Subject'
        db.delete_table(u'projects_subject')

        # Deleting model 'Tags'
        db.delete_table(u'projects_tags')

        # Deleting model 'Layer'
        db.delete_table(u'projects_layer')

        # Removing M2M table for field projects on 'Layer'
        db.delete_table(db.shorten_name(u'projects_layer_projects'))


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