# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_campaignuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignuser',
            name='campaign',
            field=models.ForeignKey(related_name='users', to='campaigns.Campaign'),
            preserve_default=True,
        ),
    ]
