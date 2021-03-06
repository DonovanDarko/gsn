# Generated by Django 2.1.5 on 2019-02-21 23:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_unexabs', models.IntegerField(null=True)),
                ('total_exabs', models.IntegerField(null=True)),
                ('total_tardies', models.IntegerField(null=True)),
                ('avg_daily_attendance', models.FloatField()),
                ('term_final_value', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Behavior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('context', models.TextField(null=True)),
                ('incident_type_program', models.CharField(max_length=50, null=True)),
                ('incident_result_program', models.CharField(max_length=50, null=True)),
                ('incident_type_school', models.CharField(max_length=50, null=True)),
                ('incident_result_school', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('term', models.CharField(choices=[('SPR', 'Spring'), ('SMR', 'Summer'), ('FLL', 'Fall')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=15)),
                ('subject', models.CharField(choices=[('MTH', 'Math'), ('SCI', 'Science'), ('HIS', 'History'), ('SST', 'Social Studies'), ('CED', 'Computer Education'), ('PHS', 'Physical Education'), ('RDG', 'Reading'), ('WRT', 'Writing'), ('STH', 'Study Hall'), ('SPE', 'Special Education'), ('ENG', 'English'), ('ESL', 'English As a Second Language'), ('ESP', 'Spanish'), ('CHI', 'Chinese'), ('FRN', 'French'), ('GER', 'German'), ('JAP', 'Japanese'), ('LTN', 'Latin'), ('SNL', 'Subject Not Listed')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('city', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('grade', models.FloatField()),
                ('term_final_value', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MTL', 'Mental Health'), ('DAC', 'Drug & Alcohol/Addictions Counseling'), ('DHS', 'Social Services (Department of Human Services)'), ('YSC', 'Division of Youth Services/Corrections'), ('CPS', 'Childcare/Preschool Services'), ('FMR', 'Family Resources'), ('M/C', 'Meals/Clothing'), ('HOU', 'Housing'), ('SIP', 'Specialized School Intervention Program'), ('TRN', 'Transportation'), ('WFC', 'Work Force Center'), ('IOG', 'Interagency Oversight Group (IOG)'), ('OTH', 'Other')], max_length=3)),
                ('date_given', models.DateField(default=django.utils.timezone.now)),
                ('reference_name', models.CharField(max_length=100, null=True)),
                ('reference_phone', models.BigIntegerField(null=True)),
                ('reference_address', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=150)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gsndb.District')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('middle_name', models.CharField(max_length=35, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'NonBinary')], max_length=2)),
                ('birth_date', models.DateField()),
                ('state_id', models.IntegerField(null=True)),
                ('grade_year', models.SmallIntegerField(choices=[(0, 'Kindergarten'), (1, 'First Grade'), (2, 'Second Grade'), (3, 'Third Grade'), (4, 'Fourth Grade'), (5, 'Fifth Grade'), (6, 'Sixth Grade'), (7, 'Seventh Grade'), (8, 'Eighth Grade'), (9, 'Ninth Grade'), (10, 'Tenth Grade'), (11, 'Eleventh Grade'), (12, 'Twelfth Grade')])),
                ('program', models.CharField(choices=[('EA', 'Expelled and At-Risk Student Servies')], max_length=2)),
                ('reason_in_program', models.TextField()),
                ('current_school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gsndb.School')),
            ],
        ),
        migrations.AddField(
            model_name='referral',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gsndb.Student'),
        ),
    ]
