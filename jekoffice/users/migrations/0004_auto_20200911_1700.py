# Generated by Django 2.2.10 on 2020-09-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200429_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mac_adress',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]