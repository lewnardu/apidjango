# Generated by Django 3.2.15 on 2022-08-24 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('codigo', models.CharField(max_length=255)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('preco_custo', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('preco_venda', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('status_inventario', models.BooleanField()),
                ('avaliacao', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.categoria')),
            ],
            options={
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
