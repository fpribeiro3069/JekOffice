# Generated by Django 2.2.10 on 2020-04-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200405_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cargo',
            field=models.CharField(blank=True, choices=[('Software developer', 'Software developer'), ('Designer', 'Designer'), ('Film maker', 'Film maker'), ('Innovation consultant', 'Innovation consultant'), ('HR manager', 'HR manager'), ('CFO', 'CFO'), ('International Manager', 'International Manager'), ('CEO', 'CEO'), ('CIO', 'CIO'), ('COO', 'COO'), ('CTO', 'CTO')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='curso',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]