# Generated by Django 4.0.2 on 2022-02-13 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_scope_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlescope',
            old_name='scope',
            new_name='tag',
        ),
    ]
