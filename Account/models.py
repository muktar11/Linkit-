from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone number must be set')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user( phone, password, **extra_fields)



class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    roles = models.CharField(max_length=15)
    code = models.CharField(max_length=6, blank=True, null=True)
    coins = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    image_url = models.FileField(max_length=255,blank=True,null=True, default='defaults/icons.png')
    passport = models.FileField(max_length=255, blank=True, null=True, default='')
    two_factor_authentication =  models.BooleanField(default=False)
    two_factor_auth_code = models.IntegerField(default=0)
    two_factor_auth_code_expiration = models.DateTimeField(blank=True, null=True)  # Expiration time for 2FA code
    objects = CustomUserManager()  # Use the custom user manager
    USERNAME_FIELD = 'phone'  # Set phone as the username field
    def __str__(self):
        return self.phone

class Activity(models.Model):
    TAP = 'tap'
    WATCH_VIDEO = 'watch_video'
    ACTIVITY_TYPE_CHOICES = [(TAP, 'Tap'),(WATCH_VIDEO, 'Watch Video'),]
    activity_type = models.CharField(max_length=20,choices=ACTIVITY_TYPE_CHOICES,default=TAP)
    coins_earned = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        return f"{self.activity_type} - {self.coins_earned} coins"
=======
        return self.id
>>>>>>> 2b11a5b (first commit)

class CashWithdraw(models.Model):
    paypal_email_address = models.EmailField(max_length=255, blank=True, null=True, default="")
    amount_to_send = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=10, default="")
    recepient_name = models.CharField(max_length=255, default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="cash_withdraws")

    def __str__(self):
        return f"CashWithdraw by {self.user} - {self.amount_to_send} {self.currency}"

'''
Most Traded Currencies:
    USD (United States Dollar)
    EUR (Euro)
    JPY (Japanese Yen)
    GBP (British Pound Sterling)
    AUD (Australian Dollar)
    CAD (Canadian Dollar)
    CHF (Swiss Franc)
    CNY (Chinese Yuan)
    HKD (Hong Kong Dollar)
    NZD (New Zealand Dollar)
    Other Major Currencies:
    INR (Indian Rupee)
    BRL (Brazilian Real)
    RUB (Russian Ruble)
    ZAR (South African Rand)
   
    AED (United Arab Emirates Dirham)
    SAR (Saudi Riyal)
    MXN (Mexican Peso)
    SGD (Singapore Dollar)
    KRW (South Korean Won)
    THB (Thai Baht)
    African & Regional Currencies:
    ETB (Ethiopian Birr)
    KES (Kenyan Shilling)
    NGN (Nigerian Naira)
    TZS (Tanzanian Shilling)
    GHS (Ghanaian Cedi)
    UGX (Ugandan Shilling)
    XAF (Central African CFA Franc)
    XOF (West African CFA Franc)
'''
class CashRate(models.Model):
    USD = models.IntegerField(blank=True, null=True, default=0)
    EUR = models.IntegerField(blank=True, null=True, default=0)
    JPY = models.IntegerField( blank=True, null=True, default=0)
    
    GBP = models.IntegerField( blank=True, null=True, default=0)
    AUD = models.IntegerField( blank=True, null=True, default=0)
    CAD = models.IntegerField( blank=True, null=True, default=0)
    
    CHF = models.IntegerField( blank=True, null=True, default=0)
    CNY = models.IntegerField( blank=True, null=True, default=0)
    HKD = models.IntegerField( blank=True, null=True, default=0)
    
    NZD = models.IntegerField( blank=True, null=True, default=0)
    INR = models.IntegerField( blank=True, null=True, default=0)
    BRL = models.IntegerField( blank=True, null=True, default=0)
    RUB = models.IntegerField( blank=True, null=True, default=0)
    ZAR = models.IntegerField (blank=True, null=True, default=0)
    
    AED = models.IntegerField( blank=True, null=True, default=0)
    SAR = models.IntegerField( blank=True, null=True, default=0)
    MXN = models.IntegerField( blank=True, null=True, default=0)
    SHD = models.IntegerField( blank=True, null=True, default=0)
    KRW = models.IntegerField( blank=True, null=True, default=0)
    ETB = models.IntegerField( blank=True, null=True, default=0)
    
    KES = models.IntegerField( blank=True, null=True, default=0)
    TZS = models.IntegerField( blank=True, null=True, default=0)
    GHS = models.IntegerField( blank=True, null=True, default=0)
    UGX = models.IntegerField( blank=True, null=True, default=0)
    XAF = models.IntegerField( blank=True, null=True, default=0)
    XOF = models.IntegerField( blank=True, null=True, default=0)
    timestamp = models.DateTimeField(default=now)

class PurchaseCoin(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_purchase_coins')
    no_of_coins = models.IntegerField(blank=True, null=True, default=0)
    is_paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=now)


class WireCoin(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='wire_user_coins')
    recepient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recepient_user_coins')
    no_of_coins = models.IntegerField(blank=True, null=True, default=0)
    is_paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=now)

class Coin(models.Model):
    code = models.CharField(max_length=255, default='', blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expiry_date = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    @staticmethod
    def delete_expired_coins():
        expired_coins = Coin.objects.filter(expiry_date__lt=now())
        count = expired_coins.count()
        expired_coins.delete()
        return count

    def __str__(self):
        return f"{self.code} - {self.value}"


class OnlineShop(models.Model):
    item_name = models.CharField(max_length=255, blank=True, null=True)
    item_image = models.FileField(max_length=255,blank=True,null=True, default='defaults/icons.png')
    stock_balance = models.IntegerField(blank=True,null=True, default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.item_name

class CustomerPurchase(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='used_user')
    shop = models.ForeignKey(OnlineShop, on_delete=models.CASCADE, related_name='used_shop')
    is_paid = models.BooleanField(default=False)
    is_deliverd = models.BooleanField(default=False) 
    timestamp = models.DateTimeField(default=now)   

class UsedCoin(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='used_coins')
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)

    class Meta:
        unique_together = ('user', 'coin')  # Prevent duplicate entries
        
class Exchange(models.Model):
    currencytype = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expiry_date = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Exchange {self.currencytype} - Value: {self.value}"

class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='messages')
    receiver = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='messagesreceiver')

    def __str__(self):
        return f"Message from {self.user} at {self.timestamp}"

<<<<<<< HEAD
class Video(models.Model):
    PLATFORM_CHOICES = [
        ('YouTube', 'YouTube'),
        ('TikTok', 'TikTok'),
        ('FaceBook', 'FaceBook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
    ]
=======
class Publish(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    parent = models.ForeignKey(CustomUser, models.CASCADE, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    submission_type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    key_features_and_goals = models.CharField(max_length=255, blank=True, null=True)
    target_audience = models.CharField(max_length=255, blank=True, null=True)
    development_stage = models.CharField(max_length=255, blank=True, null=True)
    amount_needed = models.CharField(max_length=255, blank=True, null=True)
    how_will_funds_will_be_used = models.CharField(max_length=255, blank=True, null=True)
    market_overview = models.CharField(max_length=255, blank=True, null=True)
    competitors = models.CharField(max_length=255, blank=True, null=True)
    potential_user_impact = models.CharField(max_length=255, blank=True, null=True)
    uniqueness = models.CharField(max_length=255, blank=True, null=True)
    no_of_photos = models.IntegerField(default=0, blank=True, null=True)  # Changed to IntegerField
    no_of_videos = models.IntegerField(default=0, blank=True, null=True)  # Changed to IntegerField
    no_of_payments = models.IntegerField(default=0, blank=True, null=True)  # Changed to IntegerField
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

# Model for storing photos
class Photo(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    parent = models.ForeignKey(Publish, related_name='photos', on_delete=models.CASCADE)
    image_url = models.FileField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Photo for {self.parent.title}"

# Model for storing videos
class Video(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    parent = models.ForeignKey(Publish, related_name='videos', on_delete=models.CASCADE)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Video for {self.parent.title}"
    
# Model for storing videos
class PaymentInfo(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    parent = models.ForeignKey(Publish, related_name='payments', on_delete=models.CASCADE)
    bank_info = models.CharField(max_length=255, blank=True, null=True)
    bank_account = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Video for {self.parent.title}"
>>>>>>> 2b11a5b (first commit)

    url = models.CharField(max_length=6000, unique=True, null=False)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES, null=False)

    def __str__(self):
        return f"{self.platform} - {self.url}"

class DailyCombo(models.Model):    
    activity_one = models.CharField(max_length=255, blank=True, null=True)
    activity_two = models.CharField(max_length=255, blank=True, null=True)
    activity_three = models.CharField(max_length=255, blank=True, null=True)
    activity_four = models.CharField(max_length=255, blank=True, null=True)
    activity_five = models.CharField(max_length=255, blank=True, null=True)
    deadline = models.DateTimeField()
    accomplishment_value = models.IntegerField(default=0, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

<<<<<<< HEAD
class DailyComboClaim(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    combo = models.ForeignKey(DailyCombo, on_delete=models.CASCADE)
    is_claimed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
=======


class Invest(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    parent = models.ForeignKey(CustomUser, models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    investment_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)  

class LikeInvest(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, related_name='like_invest', on_delete=models.CASCADE)
    parent = models.ForeignKey(Invest, related_name='likes', on_delete=models.CASCADE)
    likes = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return f"Like for {self.parent.title}"


class RateInvest(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, related_name='rate_invest', on_delete=models.CASCADE)
    parent = models.ForeignKey(Invest, related_name='rate', on_delete=models.CASCADE)
    no_of_rating = models.IntegerField(default=0, blank=True, null=True)
    rate = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
>>>>>>> 2b11a5b (first commit)
    
class HomePage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    daily_reward = models.DecimalField(max_digits=255, decimal_places=2, blank=True, null=True)
    daily_cipher = models.DecimalField(max_digits=255, decimal_places=2, blank=True, null=True)
    daily_combo = models.DecimalField(max_digits=255, decimal_places=2, blank=True, null=True)

<<<<<<< HEAD
    def __str__(self):
        return f"{self.user}"

class CoinMine(models.Model):
    miner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="mined_coins")
    coin_value = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.miner.username} mined {self.coin_value} coins on {self.timestamp}"

    @classmethod
    def mine_coin(cls, miner, coin_value):
        """
        Method to handle the coin mining process.
        - Adds a new record in the CoinMine table.
        - Updates the miner's total coin count.
        """
        if coin_value <= 0:
            raise ValueError("Coin value must be greater than zero.")

        # Add the mined coin to the CoinMine table
        cls.objects.create(miner=miner, coin_value=coin_value)

        # Update the miner's total coins
        miner.coins += coin_value
        miner.save()

        return miner.coins
=======
class CommentPublish(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, related_name='commenter', on_delete=models.CASCADE)
    parent = models.ForeignKey(Publish, related_name='commentspublish', on_delete=models.CASCADE, blank=True, null=True)
    parent_comment = models.ForeignKey('self', related_name='repliespublish', on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    photos = models.FileField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user} on {self.parent or 'a comment'}"


class CommentInvest(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, related_name='comment_invest', on_delete=models.CASCADE)
    parent = models.ForeignKey(Invest, related_name='commentinvest', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', related_name='repliesinvest', on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    photos = models.FileField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user} on {self.parent or 'a comment'}"

    




class Settings(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    parent = models.ForeignKey(CustomUser, models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    enable_notifications = models.BooleanField(max_length=255, blank=True, null=True)
    enable_dark_mode = models.BooleanField(max_length=255, blank=True, null=True)
    make_profile_public = models.BooleanField(max_length=255, blank=True, null=True)
    show_online_status = models.BooleanField(max_length=255, blank=True, null=True)
    two_factor_authentication = models.BooleanField(max_length=255, blank=True, null=True)
>>>>>>> 2b11a5b (first commit)
