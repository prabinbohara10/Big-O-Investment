from email import header
from pickle import TRUE
from django.contrib import admin
#from calc.models import TSLA
from calc.models import fundamental
from calc.models import technical1
from calc.models import technical2,signup_detail
from calc.models import a
#from calc.models import fundamental1

from django.urls import path
from django.shortcuts import render
from django import forms

from .models import fundamental
from .models import technical1
from .models import technical2
from .models import a,tsla

#from .models import fundamental1
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Register your models here.
# admin.site.register(TSLA)
#admin.site.register(technical2)



class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()
# # yo chai tesla ko data lina ko lagi ho hai
# class TSLAAdmin(admin.ModelAdmin):
#     list_display = ('Date', 'Open' ,'High' , 'Low','Close','Adjusted_Close','Volume')

#     def get_urls(self):
#         urls = super().get_urls()
#         new_urls = [path('upload-csv/', self.upload_csv),]
#         return new_urls + urls

#     def upload_csv(self, request):

#         if request.method == "POST":
#             csv_file = request.FILES["csv_upload"]
            
#             if not csv_file.name.endswith('.csv'):
#                 messages.warning(request, 'The wrong file type was uploaded')
#                 return HttpResponseRedirect(request.path_info)
            
#             file_data = csv_file.read().decode("utf-8")
#             csv_data = file_data.split("\n")
#             #next(csv_data,None)
#             #print(csv_data.len())
#             skip_first =True
#             for x in csv_data:
#                 if skip_first==True :
#                     skip_first=False
#                     continue
#                 fields = x.split(",")
#                 print('mishan')
                
                
#                 try:
#                     created = TSLA.objects.update_or_create(
#                     Date = fields[0],
#                     Open = fields[1],
#                     High =fields[2],
#                     Low = fields[3],
#                     Close = fields[4],
#                     Adjusted_Close = fields[5],
#                     Volume = fields[6],
#                     )
#                 except:
#                     pass
#             url = reverse('admin:index')
#             return HttpResponseRedirect(url)

#         form = CsvImportForm()
#         data = {"form": form}
#         return render(request, "admin/csv_upload.html", data)

# admin.site.register(TSLA, TSLAAdmin)

# # yo chai fundamental ko data halna hai 
class fundamentalAdmin(admin.ModelAdmin):
    list_display1 = ('companies','trailing PE', 'return on equity' ,'return on assets' , 'book value','trailing EPS','price to book','sector','payout ratio','market cap','trailing peg ratio')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            #next(csv_data,None)
            #print(csv_data.len())
            skip_first =True
            for x in csv_data:
                if skip_first==True :
                    skip_first=False
                    continue
                fields = x.split(",")
                print('mishan')
                
                
                try:
                    created = fundamental.objects.update_or_create(
                    companies = fields[0],
                    trailing_PE = fields[1],
                    return_on_equity = fields[2],
                    return_on_assets =fields[3],
                    book_value = fields[4],
                    trailing_EPS = fields[5],
                    price_to_book = fields[6],
                    sector = fields[7],
                    payout_ratio = fields[8],
                    market_cap = fields[9],
                    trailing_peg_ratio = fields[10],
                    )
                except:
                    pass
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(fundamental, fundamentalAdmin)


# yo chai technical ko data halna hai 
class technical2Admin(admin.ModelAdmin):
    list_display4 = ('sn','business_date','security_id','symbol' , 'security_name', 'open_price', 'high_price',
     'close_price', 'total_traded_quantity', 'total_traded_value', 'previous_day_close_price', 'fiftytwo_week_high_price',
     'fiftytwo_week_high_price', 'fiftytwo_week_low_price', 'last_updated_time', 'last_updated_price', 'total_trades', 
     'average_traded_price', 'market_capitalization', 'rsi', 'macd', 't50_v_20_ema', 't20sma_v_price',
      't50sma_v_price', 't200sma_v_price', 'ltp', 'bollingerband')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            #next(csv_data,None)
            #print(csv_data.len())
            skip_first =True
            for x in csv_data:
                if skip_first==True :
                    skip_first=False
                    continue
                fields = x.split(",")
                print('mishan')
                
                
                try:
                    created = technical2.objects.update_or_create(
                    sn = fields[0],
                    business_date = fields[1],
                    security_id = fields[2],
                    symbol =fields[3],
                    security_name = fields[4],
                    open_price = fields[5],
                    high_price = fields[6],
                    low_price = fields[7],
                    close_price = fields[8],
                    total_traded_quantity = fields[9],
                    total_traded_value= fields[10],
                    previous_day_close_price = fields[11],
                    fiftytwo_week_high_price = fields[12],
                    fiftytwo_week_low_price = fields[13],
                    last_updated_time= fields[14],
                    last_updated_price =fields[15],
                    total_trades = fields[16],
                    average_traded_price= fields[17],
                    market_capitalization= fields[18],
                    rsi= fields[19],
                    macd = fields[20],
                    t50_v_20_ema = fields[21],
                    t20sma_v_price= fields[22],
                    t50sma_v_price= fields[23],
                    t200sma_v_price =fields[24],
                    ltp= fields[25],
                    bollingerband= fields[26],
                    )
                except:
                    pass
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(technical2,technical2Admin)
admin.site.register(technical1)

# for a company ko lagi hai
class aAdmin(admin.ModelAdmin):
    list_display2 = ('date','open','high','low','close','adj_close','volume','rsi','macd','bollingerband_signal')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            #next(csv_data,None)
            #print(csv_data.len())
            skip_first =True
            for x in csv_data:
                if skip_first==True :
                    skip_first=False
                    continue
                fields = x.split(",")
                print('mishan')
                
                
                try:
                    created = a.objects.update_or_create(
                    date = fields[0],
                    open = fields[1],
                    high = fields[2],
                    low =fields[3],
                    close = fields[4],
                    adj_close = fields[5],
                    volume = fields[6],
                    rsi = fields[7],
                    macd = fields[8],
                    bollingerband_signal = fields[9],
                    )
                except:
                    pass
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(a, aAdmin)
admin.site.register(signup_detail)
admin.site.register(tsla)