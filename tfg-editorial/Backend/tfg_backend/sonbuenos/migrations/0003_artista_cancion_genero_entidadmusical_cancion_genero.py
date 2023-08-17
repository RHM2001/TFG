# Generated by Django 4.2.4 on 2023-08-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sonbuenos', '0002_rename_artistas_sonbuenos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EntidadMusical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('artistas', models.ManyToManyField(to='sonbuenos.artista')),
                ('canciones', models.ManyToManyField(to='sonbuenos.cancion')),
                ('genero', models.ManyToManyField(to='sonbuenos.genero')),
            ],
        ),
        migrations.AddField(
            model_name='cancion',
            name='genero',
            field=models.ManyToManyField(to='sonbuenos.genero'),
        ),
    ]
