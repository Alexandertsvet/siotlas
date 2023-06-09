# Generated by Django 4.1 on 2023-03-16 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название группы', max_length=200, verbose_name='название')),
                ('slug', models.SlugField(help_text='Введите уникальный фрагмент URL-адреса для группы', unique=True, verbose_name='уникальный фрагмент URL-адреса')),
                ('description', models.TextField(help_text='Введите описание группы', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'група',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',), 'verbose_name': 'пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.group', verbose_name='название группы'),
        ),
    ]
