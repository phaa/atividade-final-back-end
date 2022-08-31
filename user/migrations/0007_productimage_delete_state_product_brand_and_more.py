# Generated by Django 4.0.5 on 2022-08-31 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_category_productcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('default', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('AR', 'Armani'), ('CT', 'Cartier'), ('CS', 'Casio'), ('CP', 'Champion'), ('MB', 'Montblanc'), ('MM', 'Mormaii'), ('RX', 'Rolex'), ('TH', 'Tommy Hilfighter'), ('WP', 'Wempe')], default='AR', max_length=2, verbose_name='Marca'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='', verbose_name='Descrição'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='total_sales',
            field=models.IntegerField(default=0, verbose_name='Total Sales'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('AV', 'Aviador'), ('ML', 'Militar'), ('CR', 'Corredor'), ('MR', 'Mergulhador'), ('CM', 'Campo'), ('FS', 'Fashion'), ('LX', 'Luxuoso'), ('ST', 'Smart'), ('FT', 'Fitness'), ('BS', 'Bolso'), ('MD', 'Médico'), ('ES', 'Esportivo'), ('RS', 'Rústico'), ('FR', 'Formal')], max_length=2, verbose_name='Categoria'),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.product'),
        ),
    ]