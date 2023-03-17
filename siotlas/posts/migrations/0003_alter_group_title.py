# Generated by Django 4.1 on 2023-03-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_group_alter_post_options_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(choices=[('Басни', 'Басни'), ('Сказки', 'Сказки'), ('Стихотверения', 'Стихотверения')], help_text='Выберите группу', max_length=200, verbose_name='название'),
        ),
    ]