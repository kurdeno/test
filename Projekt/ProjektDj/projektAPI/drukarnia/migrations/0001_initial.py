# Generated by Django 3.1.3 on 2021-01-17 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('nr_telefonu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=45)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
                ('pesel', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('nr_telefonu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=45)),
                ('data', models.DateField()),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drukarnia.klient')),
                ('pracownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drukarnia.pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc', models.IntegerField()),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drukarnia.oferta')),
                ('zamowienie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drukarnia.zamowienie')),
            ],
        ),
    ]
