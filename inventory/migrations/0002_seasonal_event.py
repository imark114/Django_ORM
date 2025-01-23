# Generated by Django 5.1.5 on 2025-01-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonalEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'inventory_seasonal_event',
            },
        ),

        migrations.RunSQL("""
            ALTER TABLE inventory_seasonal_event
            ADD CONSTRAINT inventory_seasonal_event_chck_empty_name
            CHECK (name <> '' AND name is NOT NULL);
        """),
        
        migrations.RunSQL("""
            CREATE OR REPLACE FUNCTION lowercase_name_trigger()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.name = LOWER(NEW.name);
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
            
            CREATE TRIGGER seasonal_even_lowercase_name_trigger
            BEFORE INSERT OR UPDATE ON inventory_seasonal_event
            FOR EACH ROW
            EXECUTE FUNCTION lowercase_name_trigger();
        """),

    ]
