# Generated by Django 4.1.2 on 2023-01-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tisdac_app', '0029_alter_department_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='image2',
            field=models.FileField(null=True, upload_to='service'),
        ),
    ]