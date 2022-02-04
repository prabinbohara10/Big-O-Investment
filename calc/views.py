from asyncio.windows_events import NULL
from symtable import Symbol
from django.shortcuts import render
from django.http import HttpResponse
#from calc.models import TSLA
from calc.models import fundamental
from calc.models import a
from calc.models import technical1
from calc.models import technical2,signup_detail
import pandas as pd
import matplotlib.pyplot as plt

from prophet import Prophet
import plotly.graph_objects as go
import os


fs1=''
fs2=''
# Create your views here.
def home(request):
    return render(request,'home.html')


def market(request):
    return render(request,'market.html')

def forecast(request):
    forecast_query= fundamental.objects.all()
    return render(request,'forecast.html',{'forecast_query':forecast_query})

def comparator_comp1_search(request):
    if request.method == "POST":
        fs1= request.POST.get('comparator_comp1_search_name')
        fs= request.POST.get('comparator_comp2_search_name')
        fcomparator_comp1_search_query=fundamental.objects.all().filter(companies=fs1)
        fcomparator_comp2_search_query=fundamental.objects.all().filter(companies=fs)
        tcomparator_comp1_search_query=technical2.objects.all().filter(symbol=fs1)
        tcomparator_comp2_search_query=technical2.objects.all().filter(symbol=fs)   
        return render(request,'table1.html',{'fcomparator_comp1_search_query':fcomparator_comp1_search_query,'fcomparator_comp2_search_query':fcomparator_comp2_search_query,'tcomparator_comp1_search_query':tcomparator_comp1_search_query,'tcomparator_comp2_search_query':tcomparator_comp2_search_query})



def technical_screener(request):
    return render(request,'technical_screener.html')


def fundamental_screener(request):
    return render(request,'fundamental_screener.html')

def comparator(request):
    return render(request,'comparator.html')

def forecast_search(request):
    #os.remove("static\image\prophetplot.png")
    forecast_query= fundamental.objects.all()
    if request.method == "POST":
        fs1= request.POST.get('forecast_close_search')
        print(fs1)
        fsq1= a.objects.all() 
        df1 = pd.DataFrame()
        nabil1 = pd.DataFrame()
        df1 = pd.DataFrame(list(a.objects.all().values())) 
        print(df1) 
        
        import time

        # def countdown(time_sec):
        #     while time_sec:
        #         mins, secs = divmod(time_sec, 60)
        #         timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #         print(timeformat, end='\r')
        #         time.sleep(1)
        #         time_sec -= 1

        #         print("stop")
                
        # countdown(4)


        #forecast model:
       
        
        #df=pd.read_csv('Tesla.csv')
        #df=df[::-1]
        #data Cleaning
        df1=df1.dropna()
        nabil1=df1[["date","adj_close"]]
        nabil1.columns = ['ds','y']
        forecast_date='2021-01-01'
        forecast_time=30  #in days:

        plt.plot(nabil1['ds'], nabil1['y'],'r')
        plt.savefig('static\image\prophetplot40.png')
        plt.close()


        #graph_div = go.offline.plot(fig1, auto_open = False, output_type="div")
        return render(request,'forecast.html',{'fsq':fsq1,'forecast_query':forecast_query,'stock':fs1,'to_check_value':1})
        
def forecast_applied(request):
    #os.remove("static\image\prophetplot.png")
    forecast_query= fundamental.objects.all()
    if request.method == "POST":
        stock_name= request.POST.get('stock')

        # forecast_date=request.POST.get('forecast_date')
        # forecast_time=int(request.POST.get('forecast'))
        # lookback_days=int(request.POST.get('lookback'))
        # accuracy_range=int(request.POST.get('accuracy_range'))/100
        forecast_date='2021-01-01'
        forecast_time=30  #in days:
        lookback_days=1000
        accuracy_range=0.8

        print(forecast_date, forecast_time,lookback_days)


        
        fsq= a.objects.all() 
        df = pd.DataFrame()
        nabil = pd.DataFrame()
        df = pd.DataFrame(list(a.objects.all().values())) 
        print(df) 
        

        #forecast model:
       
        
        #df=pd.read_csv('Tesla.csv')
        #df=df[::-1]
        #data Cleaning
        df=df.dropna()
        nabil=df[["date","adj_close"]]
        nabil.columns = ['ds','y']
       

        nabil.index=pd.to_datetime(nabil.ds)
        nabil=nabil['y'][:forecast_date]
        nabil = nabil.to_frame().reset_index()
        nabil=nabil[len(nabil)-lookback_days : ]
        nabil_train=nabil[:-30]
        nabil_test=nabil[len(nabil)-30:]
        
        fbp=Prophet(daily_seasonality=False, changepoint_range=accuracy_range)
        fbp.fit(nabil_train)
        future=fbp.make_future_dataframe(periods=forecast_time)
        forecast=fbp.predict(future)
        print(forecast)
        from fbprophet.plot import plot_plotly, plot_components_plotly
        fig1 = fbp.plot(forecast)
        fig1.savefig('static\image\prophetplot45.png')
        


        #graph_div = go.offline.plot(fig1, auto_open = False, output_type="div")
        return render(request,'forecast.html',{'fsq':fsq,'forecast_query':forecast_query,'stock':stock_name,'to_check_value':2})

        
        
        


# search bar ma searcha huda
def search(request):
    if request.method == "POST":
        a= request.POST.get('searched')
        if a == "PCBL":
            return render(request,'pcbl.html')
    # if request.GET['searched']=="PCBL" :
    #         return render(request,'pcbl.html')
    # elif request.GET['searched']=="AA":
    #     return render(request,'AA.html')


# for technical screnner hai
def technical_screener_search(request):
    if request.method == "POST":
        rsi_min =request.POST.get('rsi_min_search')
        rsi_max =request.POST.get('rsi_max_search')
        rsi_def =request.POST.get('rsi_defined_search')
        macd_def =request.POST.get('macd_defined_search')
        bbs_def =request.POST.get('bbs_defined_search')
        ltp_min =request.POST.get('ltp_min_search')
        ltp_max =request.POST.get('ltp_max_search')
        ltp_def =request.POST.get('ltp_defined_search')
        t20v20p_def =request.POST.get('t20v20p_defined_search')
        t50v20p_def =request.POST.get('t50v20p_defined_search')
        t200v20p_def =request.POST.get('t200v20p_defined_search')
        t50v20e_def =request.POST.get('t50v20e_defined_search')
        technical2_query= technical2.objects.all()
        if macd_def !='' and macd_def is not None:
            technical2_query= technical2_query.filter(macd= macd_def)
        if bbs_def !='' and bbs_def is not None:
            technical2_query= technical2_query.filter(bollingerband = bbs_def)
        if rsi_min !='' and rsi_min is not None:
            technical2_query= technical2_query.filter(rsi__gte= rsi_min)
        if rsi_max !='' and rsi_max is not None:
            technical2_query= technical2_query.filter(rsi__lte= rsi_max)
        if rsi_def !='' and rsi_def is not None:
            if rsi_def == 1:
                technical2_query= technical2_query.filter(rsi__lte= 30)
            elif rsi_def == 2 :
                technical2_query= technical2_query.filter(rsi__lte= 70)
                technical2_query= technical2_query.filter(rsi__gte= 30)
            else :
                technical2_query= technical2_query.filter(rsi__gte= 70)
        if t20v20p_def !='' and t20v20p_def is not None:
            technical2_query= technical2_query.filter(t20sma_v_price= t20v20p_def)
        if t50v20p_def !='' and t50v20p_def is not None:
            technical2_query= technical2_query.filter(t50sma_v_price= t50v20p_def)
        if t200v20p_def !='' and t200v20p_def is not None:
            technical2_query= technical2_query.filter(t200sma_v_price= t200v20p_def)        
        if t50v20e_def !='' and t50v20e_def is not None:
            technical2_query= technical2_query.filter(t50_v_20_ema = t50v20e_def)
        if ltp_min !='' and ltp_min is not None:
            technical2_query= technical2_query.filter(ltp__gte= ltp_min)
        if ltp_max !='' and ltp_max is not None:
            technical2_query= technical2_query.filter(ltp__lte= ltp_max)
        if ltp_def !='' and ltp_def is not None:
            if ltp_def == 1:
                technical2_query= technical2_query.filter(ltp__lte= 300)
            elif ltp_def == 2 :
                technical2_query= technical2_query.filter(ltp__lte= 500)
            else :
                technical2_query= technical2_query.filter(ltp__gte= 500)
        
        return render(request,'technical_screener.html',{'tq':technical2_query})


def fundamental_screener_search(request):
    if request.method == "POST":
        # putting all the inputed datas in vaiable
        bv_min =request.POST.get('bv_min_search')
        bv_max =request.POST.get('bv_max_search')
        eps_min =request.POST.get('eps_min_search')
        eps_max =request.POST.get('eps_max_search')
        mc_min =request.POST.get('mc_min_search')
        mc_max =request.POST.get('mc_max_search')
        por_min =request.POST.get('por_min_search')
        por_max =request.POST.get('por_max_search')
        pb_min =request.POST.get('pb_min_search')
        pb_max =request.POST.get('pb_max_search')
        pe_min =request.POST.get('pr_min_search')
        pe_max =request.POST.get('pe_max_search')
        pgr_min =request.POST.get('pgr_min_search')
        pgr_max =request.POST.get('pgr_max_search')
        roa_min =request.POST.get('roa_min_search')
        roa_max =request.POST.get('roa_max_search')
        roe_min =request.POST.get('roe_min_search')
        roe_max =request.POST.get('roe_max_search')
        # defined value start
        bv_def =request.POST.get('bv_defined_search')
        eps_def =request.POST.get('eps_defined_search')
        mc_defined =request.POST.get('mc_defined_search')
        por_defined =request.POST.get('por_defined_search')
        pb_defined =request.POST.get('pb_defined_search')
        pe_defined =request.POST.get('pr_defined_search')
        pgr_defined =request.POST.get('pgr_defined_search')
        roa_defined =request.POST.get('roa_defined_search')
        roe_defined =request.POST.get('roe_defined_search')
        
        #defined value end
        fundamental_query= fundamental.objects.all()
        if bv_def !='' and bv_def is not None:
            fundamental_query= fundamental_query.filter(book_value__gte= bv_def)
        if eps_def !='' and eps_def is not None:
            fundamental_query= fundamental_query.filter(trailing_EPS__gte= eps_def)
        if mc_defined !='' and mc_defined is not None:
            fundamental_query= fundamental_query.filter(market_cap__gte= mc_defined)
        if por_defined !='' and por_defined is not None:
            fundamental_query= fundamental_query.filter(payout_ratio__gte= por_defined)
        if pb_defined !='' and pb_defined is not None:
            fundamental_query= fundamental_query.filter(price_to_book__gte= pb_defined)
        if pe_defined !='' and pe_defined is not None:
            fundamental_query= fundamental_query.filter(trailing_PE__gte= pe_defined)
        if pgr_defined !='' and pgr_defined is not None:
            fundamental_query= fundamental_query.filter(trailing_peg_ratio__gte= pgr_defined)
        if roa_defined !='' and roa_defined is not None:
            fundamental_query= fundamental_query.filter(return_on_assets__lte= roa_defined)
        if roe_defined !='' and roe_defined is not None:
            fundamental_query= fundamental_query.filter(return_on_equity__lte= roe_defined)
        if bv_min !='' and bv_min is not None:
            fundamental_query= fundamental_query.filter(book_value__gte= bv_min)
        if bv_max !='' and bv_max is not None:
            fundamental_query= fundamental_query.filter(book_value__lte= bv_max)
        if eps_min !='' and eps_min is not None:
            fundamental_query= fundamental_query.filter(trailing_EPS__gte= eps_min)
        if eps_max !='' and eps_max is not None:
            fundamental_query= fundamental_query.filter(trailing_EPS__lte= eps_max)
        if mc_min !='' and mc_min is not None:
            fundamental_query= fundamental_query.filter(market_cap__gte= mc_min)
        if mc_max !='' and mc_max is not None:
            fundamental_query= fundamental_query.filter(market_cap__lte= mc_max)
        if por_min !='' and por_min is not None:
            fundamental_query= fundamental_query.filter(payout_ratio__gte= por_min)
        if por_max !='' and por_max is not None:
            fundamental_query= fundamental_query.filter(payout_ratio__lte= por_max)
        if pb_min !='' and pb_min is not None:
            fundamental_query= fundamental_query.filter(price_to_book__gte= pb_min)
        if pb_max !='' and pb_max is not None:
            fundamental_query= fundamental_query.filter(price_to_book__lte= pb_max)
        if pe_min !='' and pe_min is not None:
            fundamental_query= fundamental_query.filter(trailing_PE__gte= pe_min)
        if pe_max !='' and pe_max is not None:
            fundamental_query= fundamental_query.filter(trailing_PE__lte= pe_max)
        if pgr_min !='' and pgr_min is not None:
            fundamental_query= fundamental_query.filter(trailing_peg_ratio__gte= pgr_min)
        if pgr_max !='' and pgr_max is not None:
            fundamental_query= fundamental_query.filter(trailing_peg_ratio__lte= pgr_max)
        if roa_min !='' and roa_min is not None:
            fundamental_query= fundamental_query.filter(return_on_assets__gte= roa_min)
        if roa_max !='' and roa_max is not None:
            fundamental_query= fundamental_query.filter(return_on_assets__lte= roa_max)
        if roe_min !='' and roe_min is not None:
            fundamental_query= fundamental_query.filter(return_on_equity__gte= roe_min)
        if roe_max !='' and roe_max is not None:
            fundamental_query= fundamental_query.filter(return_on_equity__lte= roe_max)
        print(fundamental_query)
        return render(request,'fundamental_screener.html',{'fq':fundamental_query})






def login_user(request):
    

    if request.method == "POST":
        Username = request.POST['username']
        Password=request.POST['password']
        user_detail = signup_detail.objects.all()
        for user in user_detail:
            
            if user.Username == Username and user.Password == Password:
                
                print(type(user.watchlist))
                print(user.watchlist['company'])
                request.session['username']=Username
                #return JsonResponse({'user':user.watchlist})
                return render(request,'dashboard.html',{'user': user})

                
        # pop message wrong information message
        return render(request,'login.html')
                
                
            

    

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'register.html')


def signup_user(request):
    if request.method=="POST":
        Already_present = False
        Firstname = request.POST['first_name']
        Lastname = request.POST['last_name']
        Username = request.POST['user_name']
        
        Email=request.POST['email']
        Password=request.POST['password']
        user_detail = signup_detail.objects.all()
        for user in user_detail:
            if user.Username == Username:
                Already_present = True
        
        if Already_present == False:
            signup_detail.objects.create(Firstname = Firstname,Lastname=Lastname,Username = Username,Email = Email,Password=Password)
        else:
            
            #message pop up already registered
            return render(request,'register.html')

        
        
        return render(request,'login.html')
    



def dashboard(request):
    Username1 = request.session['username']
    user_detail = signup_detail.objects.all()
    for user in user_detail:
            
        if user.Username == Username1:

            return render(request,'dashboard.html',{'user':user})

    

def portfolio(request):
        lis1 = []
        Username1 = request.session['username']
        user_detail = signup_detail.objects.all()
        for user in user_detail:
            
            if user.Username == Username1:
                
                

                for company in user.watchlist['company']:
                    
                    
                    for ss in technical2.objects.filter(symbol = company):
                            
                        if company == ss.symbol:
                            lis1.append(ss)
                

                
                
                return render(request,'portfolio.html',{'user':user,'ss':lis1})



def watchlist(request):
        lis = []
        Username = request.session['username']
        user_detail = signup_detail.objects.all()
        for user in user_detail:
            print(user)
            
            if user.Username == Username:
              

                for company in user.watchlist['company']:
                    
                    
                        for ss in technical2.objects.filter(symbol = company):
                            
                            
                            if company == ss.symbol:
                                lis.append(ss)
                

               
                
                return render(request,'watchlist.html',{'user':user,'ss':lis})


#alert ko lagi: 
#status: url mapping kei gareko chaina; just function ho
def market(request):
    todays_technical_query= fundamental.objects.all()
    return render(request,'forecast.html',{'forecast_query':forecast_query})
 