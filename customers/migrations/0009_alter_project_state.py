# Generated by Django 3.2.7 on 2021-09-30 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_alter_project_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.task'),
        ),
    ]
