# Generated by Django 4.2.3 on 2023-08-02 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes')),
                ('estado', models.CharField(max_length=20)),
                ('editorial', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField()),
                ('vendedor', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artista', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes')),
                ('disco', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField()),
                ('vendedor', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes')),
                ('estado', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField()),
                ('vendedor', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
