# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def migrate_forwards(apps, schema_editor):
    AsbestosExposureHistory = apps.get_model(
        "ipfjes", "AsbestosExposureHistory"
    )
    asbestos_exposure_histories = AsbestosExposureHistory.objects.all()

    for asbestos_exposure_history in asbestos_exposure_histories:
        related_occupation = asbestos_exposure_history.related_occupation

        if related_occupation:
            # this is related to an occupation
            episode = asbestos_exposure_history.episode
            if not related_occupation.asbestosexposurescreening_set.exists():
                related_occupation.asbestosexposurescreening_set.create(
                    exposed='Yes', episode=episode
                )
        else:
            if not episode.asbestosexposurescreening_set.filter(
                related_occupation=None
            ).exists():
                episode.asbestosexposurescreening_set.create(
                    exposed='Yes'
                )


def migrate_backwards(app, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0038_reasonforremoval_removalreason'),
    ]

    operations = [
        migrations.RunPython(
            migrate_forwards, reverse_code=migrate_backwards
        )
    ]
