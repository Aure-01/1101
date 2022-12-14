# Generated by Django 3.2.3 on 2022-11-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pastel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pastel', models.IntegerField()),
                ('sabor', models.CharField(blank=True, max_length=20, null=True)),
                ('disenio', models.CharField(blank=True, max_length=20, null=True)),
                ('tamanio', models.CharField(blank=True, max_length=20, null=True)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pizza', models.IntegerField()),
                ('ingredientes', models.CharField(blank=True, max_length=50, null=True)),
                ('especialidad', models.CharField(blank=True, max_length=20, null=True)),
                ('tamanio', models.CharField(blank=True, max_length=20, null=True)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
