# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_monitorable_cup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitorable',
            old_name='CUP',
            new_name='cup',
        ),
    ]
