# Generated by Django 3.0.5 on 2020-04-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cargo',
            field=models.CharField(blank=True, choices=[('Software developer', 'Software developer'), ('Designer', 'Designer'), ('Film maker', 'Film maker'), ('Innovation consultant', 'Innovation consultant'), ('HR manager', 'HR manager'), ('CFO', 'CFO'), ('International Manager', 'International Manager'), ('CEO', 'CEO'), ('CIO', 'CIO'), ('COO', 'COO'), ('CTO', 'CTO')], max_length=50, null=True),
        ),
    ]
