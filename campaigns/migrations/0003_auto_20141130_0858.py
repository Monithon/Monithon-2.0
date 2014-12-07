# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20141022_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignform',
            name='form',
            field=models.ForeignKey(related_name='campaigns', to='customforms.Form'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaignproject',
            name='campaign',
            field=models.ForeignKey(related_name='projects', to='campaigns.Campaign'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaignproject',
            name='project',
            field=models.ForeignKey(related_name='campaigns', to='projects.Monitorable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaignreport',
            name='campaign',
            field=models.ForeignKey(related_name='reports', to='campaigns.Campaign'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaignreport',
            name='report',
            field=models.ForeignKey(related_name='campaigns', to='reports.Report'),
            preserve_default=True,
        ),
    ]
