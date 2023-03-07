# Generated by Django 4.0.7 on 2023-03-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pedido realizado', 'Pedido Realizado'), ('Pedido em andamento', 'Em Andamento'), ('Pedido entregue', 'Entregue')], default='Pedido realizado', max_length=20)),
            ],
        ),
    ]