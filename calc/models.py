from pyexpat import model
from django.db import models

# Create your models here.

# class TSLA(models.Model):
#     Date = models.DateField()
#     Open = models.FloatField(max_length=20)
#     High = models.FloatField(max_length=20)
#     Low = models.FloatField(max_length=20)
#     Close = models.FloatField(max_length=20)
#     Adjusted_Close = models.FloatField(max_length=20)
#     Volume = models.IntegerField()

class fundamental(models.Model):
    companies = models.TextField()
    trailing_PE = models.FloatField(max_length=20)
    return_on_equity = models.FloatField(max_length=20)
    return_on_assets = models.FloatField(max_length=20)
    book_value = models.FloatField(max_length=20)
    trailing_EPS = models.FloatField(max_length=20)
    price_to_book = models.FloatField(max_length=20)
    sector = models.TextField()
    payout_ratio = models.FloatField(max_length=20)
    market_cap = models.BigIntegerField()
    trailing_peg_ratio = models.FloatField(max_length=20)

    def __str__(self):
      return self.companies

class technical1(models.Model):
    companies = models.TextField()
    rsi = models.FloatField(max_length=20)
    macd = models.TextField()
    bollingerband = models.TextField()

    def __str__(self):
      return self.companies

class technical2(models.Model):
    sn=models.IntegerField()
    business_date = models.DateField()
    security_id = models.IntegerField()
    symbol = models.TextField()
    security_name = models.TextField()
    open_price = models.FloatField(max_length=20)
    high_price = models.FloatField(max_length=20)
    low_price = models.FloatField(max_length=20)
    close_price = models.FloatField(max_length=20)
    total_traded_quantity=models.IntegerField()
    total_traded_value = models.FloatField(max_length=20)
    previous_day_close_price = models.FloatField(max_length=20)
    fiftytwo_week_high_price = models.FloatField(max_length=20)
    fiftytwo_week_low_price = models.FloatField(max_length=20)
    last_updated_time= models.DateTimeField()
    last_updated_price = models.FloatField(max_length=20)
    total_trades=models.IntegerField()
    average_traded_price = models.FloatField(max_length=20)
    market_capitalization = models.FloatField(max_length=20)
    rsi = models.FloatField(max_length=20)
    macd = models.TextField()
    t50_v_20_ema = models.TextField()
    t20sma_v_price = models.TextField()
    t50sma_v_price = models.TextField()
    t200sma_v_price = models.TextField()
    ltp=models.IntegerField()
    bollingerband = models.TextField()
    status = models.BooleanField(default=False)
    holdings = models.IntegerField()

    def __str__(self):
      return self.symbol



class signup_detail(models.Model):

    Firstname = models.TextField()
    Lastname = models.TextField()
    Username = models.TextField()
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    watchlist = models.JSONField(default ='{}')
    portfolio = models.JSONField(default ='{}')


class nepse(models.Model):

    symbol = models.TextField()
    date = models.DateField()
    open = models.FloatField(max_length=20)
    high = models.FloatField(max_length=20)
    low = models.FloatField(max_length=20)
    close = models.FloatField(max_length=20)
    percentage_change = models.FloatField(max_length=20)
    volume = models.IntegerField()
    
    
    

    def __str__(self):
      return 'A'

class tsla(models.Model):

    date = models.DateField()
    open = models.FloatField(max_length=20)
    high = models.FloatField(max_length=20)
    low = models.FloatField(max_length=20)
    close = models.FloatField(max_length=20)
    adj_close = models.FloatField(max_length=20)
    volume = models.IntegerField()
    rsi = models.FloatField(max_length=20)
    macd = models.TextField()
    bollingerband_signal = models.TextField()
    

    def __str__(self):
      return 'TSLA'
