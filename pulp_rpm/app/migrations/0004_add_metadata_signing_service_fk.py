# Generated by Django 4.2.17 on 2024-12-05 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpm', '0003_DATA_incorrect_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpmrepository',
            name='metadata_signing_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rpm_rpmrepository', to='core.asciiarmoreddetachedsigningservice'),
        ),
    ]
