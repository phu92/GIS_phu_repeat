# Generated by Django 3.2.4 on 2021-08-27 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
        ('articleapp', '0003_article_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='projectapp.project'),
        ),
    ]
