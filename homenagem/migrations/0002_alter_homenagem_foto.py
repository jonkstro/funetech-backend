# Generated by Django 4.1.3 on 2022-11-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homenagem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homenagem',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='homenagem'),
        ),
    ]