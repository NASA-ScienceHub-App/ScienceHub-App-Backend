# Generated by Django 4.2.6 on 2023-10-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('perfil_publico', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=127)),
                ('apelido', models.CharField(editable=False, max_length=127, primary_key=True, serialize=False)),
                ('idade', models.IntegerField()),
                ('entrada_plataforma', models.DateTimeField(auto_now_add=True)),
                ('sobre_mim', models.CharField(max_length=255)),
                ('inidicacoes', models.IntegerField(default=0)),
                ('contra_indicacoes', models.IntegerField(default=0)),
                ('contribuicoes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Pesquisador',
                'verbose_name_plural': 'Pesquisadores',
            },
        ),
    ]
