# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class SocialaccountSocialaccount(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class YeonsonamActor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=10)
    actor_photo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yeonsonam_actor'


class YeonsonamDiscount(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name_of_discount = models.CharField(max_length=20)
    discounted_price = models.IntegerField()
    rate_of_discount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'yeonsonam_discount'


class YeonsonamDrama(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    place = models.ForeignKey('YeonsonamPlace', models.DO_NOTHING)
    open_date = models.DateField(db_column='open_Date')  # Field name made lowercase.
    end_date = models.DateField(db_column='end_Date')  # Field name made lowercase.
    content = models.TextField()
    seat_photo = models.ForeignKey('YeonsonamSeatPhoto', models.DO_NOTHING)
    title = models.CharField(max_length=30)
    running_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'yeonsonam_drama'


class YeonsonamDramaActor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    drama = models.ForeignKey(YeonsonamDrama, models.DO_NOTHING)
    actor = models.ForeignKey(YeonsonamActor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'yeonsonam_drama_Actor'
        unique_together = (('drama', 'actor'),)


class YeonsonamDramaGenre(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    drama = models.ForeignKey(YeonsonamDrama, models.DO_NOTHING)
    genre = models.ForeignKey('YeonsonamGenre', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'yeonsonam_drama_genre'
        unique_together = (('drama', 'genre'),)


class YeonsonamDramaPrice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    drama = models.ForeignKey(YeonsonamDrama, models.DO_NOTHING)
    price = models.ForeignKey('YeonsonamPrice', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'yeonsonam_drama_price'
        unique_together = (('drama', 'price'),)


class YeonsonamDramaSequence(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    drama = models.ForeignKey(YeonsonamDrama, models.DO_NOTHING)
    sequence = models.ForeignKey('YeonsonamSequence', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'yeonsonam_drama_sequence'
        unique_together = (('drama', 'sequence'),)


class YeonsonamGenre(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    kind_of_genre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'yeonsonam_genre'


class YeonsonamPlace(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    place = models.CharField(max_length=20)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yeonsonam_place'


class YeonsonamPrice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    price = models.IntegerField()
    discount = models.ForeignKey(YeonsonamDiscount, models.DO_NOTHING)
    site = models.ForeignKey('YeonsonamSiteReservation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'yeonsonam_price'


class YeonsonamSeatPhoto(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    main_seat_photo = models.CharField(max_length=100)
    sub_seat_photo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'yeonsonam_seat_photo'


class YeonsonamSequence(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sequence_num = models.CharField(max_length=10)
    sequence_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'yeonsonam_sequence'


class YeonsonamSiteReservation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    site_name = models.CharField(max_length=20)
    site_url = models.CharField(max_length=200)
    site_location = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'yeonsonam_site_reservation'
