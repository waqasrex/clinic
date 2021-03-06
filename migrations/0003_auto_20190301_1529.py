# Generated by Django 2.1.7 on 2019-03-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20190301_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doc_id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='pat_id',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='doc_id',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='pat_id',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='vis_ID',
        ),
        migrations.AddField(
            model_name='doctor',
            name='emp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='enroll',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='emp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='enroll',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
