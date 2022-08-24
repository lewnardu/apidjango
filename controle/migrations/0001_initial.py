# Generated by Django 3.2.15 on 2022-08-24 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Formas de pagamento',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('data', models.DateField()),
                ('frete', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='ProdutoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('desconto', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='controle.pedido')),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
            options={
                'verbose_name_plural': 'Produtos Pedidos',
            },
        ),
    ]
