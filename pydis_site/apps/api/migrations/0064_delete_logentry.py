# Generated by Django 3.0.9 on 2020-10-03 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0063_Allow_blank_or_null_for_nomination_reason'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogEntry',
        ),
    ]