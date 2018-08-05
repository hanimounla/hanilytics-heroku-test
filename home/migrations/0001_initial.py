# Generated by Django 2.0.6 on 2018-07-21 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url_title', models.CharField(max_length=100, null=True)),
                ('text', models.CharField(max_length=10000)),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to='home/static/images/articles_images')),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Article_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'articles_categories',
            },
        ),
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url_title', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to='home/static/images/case_studies_images')),
            ],
            options={
                'db_table': 'case_studies',
            },
        ),
        migrations.CreateModel(
            name='CaseStudy_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'case_studies_categories',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('e_mail', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='casestudy',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CaseStudy_Category'),
        ),
        migrations.AddField(
            model_name='casestudy',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Client'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Article_Category'),
        ),
    ]