# Generated by Django 3.0.8 on 2020-07-17 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200717_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.Question'),
            preserve_default=False,
        ),
    ]