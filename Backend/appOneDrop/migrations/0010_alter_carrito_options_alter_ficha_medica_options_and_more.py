# Generated by Django 4.2.1 on 2023-05-17 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOneDrop', '0009_alter_paciente_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrito',
            options={'verbose_name': 'Carrito', 'verbose_name_plural': 'Carritos'},
        ),
        migrations.AlterModelOptions(
            name='ficha_medica',
            options={'verbose_name': 'Ficha medica', 'verbose_name_plural': 'Fichas medicas'},
        ),
        migrations.AlterModelOptions(
            name='paquete',
            options={'verbose_name': 'Paquete', 'verbose_name_plural': 'Paquetes'},
        ),
        migrations.AlterModelOptions(
            name='prestador',
            options={'verbose_name': 'Prestador', 'verbose_name_plural': 'Prestadores'},
        ),
        migrations.AlterModelOptions(
            name='registro_glucemia',
            options={'verbose_name': 'Registro glucemia', 'verbose_name_plural': 'Registros glucemia'},
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AddField(
            model_name='paquete',
            name='nombre_paquete',
            field=models.CharField(default='paquete', max_length=50),
        ),
        migrations.AddField(
            model_name='prestador',
            name='nombre_usuario_prestador',
            field=models.CharField(default='Prestador', max_length=100),
        ),
        migrations.AlterModelTable(
            name='carrito',
            table='Carrito',
        ),
        migrations.AlterModelTable(
            name='ficha_medica',
            table='Ficha_medica',
        ),
        migrations.AlterModelTable(
            name='paquete',
            table='Paquete',
        ),
        migrations.AlterModelTable(
            name='prestador',
            table='Prestador',
        ),
        migrations.AlterModelTable(
            name='registro_glucemia',
            table='Registro_glucemia',
        ),
        migrations.AlterModelTable(
            name='servicio',
            table='Servicio',
        ),
    ]