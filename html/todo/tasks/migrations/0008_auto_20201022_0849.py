# Generated by Django 3.1.1 on 2020-10-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20201022_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='endereco',
            field=models.CharField(max_length=500),
        ),
    ]
