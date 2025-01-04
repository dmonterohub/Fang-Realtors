from django.db import models
import os

def file_path(instance, filename):
    base, extension = os.path.splitext(filename)
    return '{model.object_number} - {model.object_name}{extension}'.format(
        model=instance.model, extension=extension)

# Create your models here.

class Agent(models.Model):
    agentid = models.IntegerField(db_column='agentID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    license_field = models.CharField(db_column='license#', max_length=45)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'agent'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class Contact(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=75, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Featuredlistings(models.Model):
    listingid = models.OneToOneField('Listings', models.DO_NOTHING, db_column='listingID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'featuredlistings'


class Features(models.Model):
    featureid = models.IntegerField(db_column='featureID', primary_key=True)  # Field name made lowercase.
    featuredescription = models.TextField(db_column='featureDescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'features'


# class HomepageFanglistings(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     agent_id = models.IntegerField()
#     mls_number = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     location_id = models.IntegerField()
#     price = models.CharField(max_length=200)
#     sold_status = models.CharField(max_length=200)
#     market_date = models.CharField(max_length=200)
#     year_built = models.CharField(max_length=200)
#     last_updated = models.CharField(max_length=200)
#     property_type_id = models.IntegerField()
#     home_size = models.IntegerField()
#     lot_size = models.FloatField()
#     beds = models.IntegerField()
#     baths = models.FloatField()
#     feature_id = models.IntegerField()
#     dist_id = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'homepage_fanglistings'


class Image(models.Model):
    imageid = models.AutoField(db_column='imageID', primary_key=True)  # Field name made lowercase.
    listingid = models.ForeignKey('Listings', models.DO_NOTHING, db_column='listingID')  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'image'


class Listingfeatures(models.Model):
    featureid = models.OneToOneField(Features, models.DO_NOTHING, db_column='FeatureID', primary_key=True)  # Field name made lowercase. The composite primary key (FeatureID, ListingID) found, that is not supported. The first column is selected.
    listingid = models.ForeignKey('Listings', models.DO_NOTHING, db_column='ListingID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'listingfeatures'
        unique_together = (('featureid', 'listingid'),)


class Listings(models.Model):
    listingid = models.IntegerField(db_column='listingID', primary_key=True)  # Field name made lowercase. The composite primary key (listingID, distID) found, that is not supported. The first column is selected.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='agentID')  # Field name made lowercase.
    mls_field = models.CharField(db_column='mls#', max_length=45)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    title = models.CharField(max_length=45)
    description = models.TextField()
    locationid = models.ForeignKey('Location', models.DO_NOTHING, db_column='locationID')  # Field name made lowercase.
    price = models.IntegerField(blank=True, null=True)
    soldstatus = models.CharField(db_column='soldStatus', max_length=45)  # Field name made lowercase.
    marketdate = models.CharField(db_column='marketDate', max_length=45)  # Field name made lowercase.
    yearbuilt = models.CharField(db_column='yearBuilt', max_length=45)  # Field name made lowercase.
    lastupdated = models.CharField(db_column='lastUpdated', max_length=45)  # Field name made lowercase.
    propertytypeid = models.ForeignKey('Propertytype', models.DO_NOTHING, db_column='propertyTypeID')  # Field name made lowercase.
    homesize = models.IntegerField(db_column='homeSize')  # Field name made lowercase.
    lotsize = models.FloatField(db_column='lotSize')  # Field name made lowercase.
    beds = models.IntegerField()
    baths = models.FloatField()
    featureid = models.IntegerField(db_column='featureID', blank=True, null=True)  # Field name made lowercase.
    distid = models.IntegerField(db_column='distID')  # Field name made lowercase.

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'listings'
        unique_together = (('listingid', 'distid'),)

class ListingImage(models.Model):
    listingid = models.ForeignKey(Listings, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='C:/projects/senior project/backendDesign/homepage/static/img')

    class Meta:
        managed = False
        db_table = 'listingimage'


class Location(models.Model):
    locationid = models.IntegerField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    county = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'location'


class Propertytype(models.Model):
    propertytypeid = models.IntegerField(db_column='propertyTypeID', primary_key=True)  # Field name made lowercase.
    propertytype = models.CharField(db_column='propertyType', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propertytype'


class Schooldist(models.Model):
    distid = models.IntegerField(db_column='distID', blank=True, null=True)  # Field name made lowercase.
    distname = models.CharField(db_column='distName', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schooldist'