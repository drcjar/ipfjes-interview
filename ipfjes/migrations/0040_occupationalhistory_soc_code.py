# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0039_auto_20180119_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupationalhistory',
            name='soc_code',
            field=models.ForeignKey(blank=True, to='ipfjes.SocCode', null=True),
        ),
    ]
