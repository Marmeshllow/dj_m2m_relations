# Generated by Django 4.0.2 on 2022-02-13 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articlescope_alter_article_options_scope_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематика статей'},
        ),
        migrations.RenameField(
            model_name='articlescope',
            old_name='is_basic',
            new_name='is_main',
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.scope'),
        ),
    ]
