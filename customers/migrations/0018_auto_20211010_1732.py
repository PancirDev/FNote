# Generated by Django 3.2.7 on 2021-10-10 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0017_rename_name_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.project'),
        ),
    ]
