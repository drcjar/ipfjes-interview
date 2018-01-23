# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def migrate_forwards(apps, schema_editor):
    SocCode = apps.get_model("ipfjes", "SocCode")
    SocJob = apps.get_model("ipfjes", "SocJob")
    OccupationalHistory = apps.get_model("ipfjes", "OccupationalHistory")
    # all oc histories which don't have a
    oc_histories = OccupationalHistory.objects.all().filter(soc_code=None)

    for oc_history in oc_histories:
        soc_job = SocJob.objects.filter(
            id=oc_history.soc_job_fk_id
        ).first()
        if soc_job and SocCode.objects.filter(title=soc_job.name).count() == 1:
            soc_code = SocCode.objects.get(title=soc_job.name)
            oc_history.soc_code = soc_code
            oc_history.save()


def migrate_backwards(app, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0040_occupationalhistory_soc_code'),
    ]

    operations = [
        migrations.RunPython(
            migrate_forwards, reverse_code=migrate_backwards
        ),
    ]
