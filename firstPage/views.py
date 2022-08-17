from pymongo import MongoClient
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.
import joblib
reloadedModel = joblib.load('./models/RandomForestModel.pkl')


def index(request):
    temp = {}
    temp['LP_CustomerPrincipalPayments'] = request.POST.get(
        'LP_CustomerPrincipalPaymentsVal')
    temp['LP_CustomerPayments'] = request.POST.get('LP_CustomerPaymentsVal')
    temp['BorrowerAPR'] = request.POST.get('BorrowerAPRVal')
    temp['EstimatedEffectiveYield'] = request.POST.get(
        'EstimatedEffectiveYieldVal')
    temp['LoanMonthsSinceOrigination'] = request.POST.get(
        'LoanMonthsSinceOriginationVal')
    temp['DateCreditPulledYear'] = request.POST.get('DateCreditPulledYearVal')
    temp['ListingCreationDateYear'] = request.POST.get(
        'ListingCreationDateYearVal')
    temp['LoanOriginationDateYear'] = request.POST.get(
        'LoanOriginationDateYearVal')
    temp['EstimatedReturn'] = request.POST.get('EstimatedReturnVal')
    temp['EstimatedLoss'] = request.POST.get('EstimatedLossVal')
    temp['BorrowerRate'] = request.POST.get('BorrowerRateVal')
    temp['LenderYield'] = request.POST.get('LenderYieldVal')
    context = {'temp': temp}
    return render(request, 'index.html', context)
    # return HttpResponse({'a':1})


def predictMPG(request):
    print(request)
    if request.method == 'POST':
        temp = {}
        temp['LP_CustomerPrincipalPayments'] = request.POST.get(
            'LP_CustomerPrincipalPaymentsVal')
        temp['LP_CustomerPayments'] = request.POST.get(
            'LP_CustomerPaymentsVal')
        temp['BorrowerAPR'] = request.POST.get('BorrowerAPRVal')
        temp['EstimatedEffectiveYield'] = request.POST.get(
            'EstimatedEffectiveYieldVal')
        temp['LoanMonthsSinceOrigination'] = request.POST.get(
            'LoanMonthsSinceOriginationVal')
        temp['DateCreditPulledYear'] = request.POST.get(
            'DateCreditPulledYearVal')
        temp['ListingCreationDateYear'] = request.POST.get(
            'ListingCreationDateYearVal')
        temp['LoanOriginationDateYear'] = request.POST.get(
            'LoanOriginationDateYearVal')
        temp['EstimatedReturn'] = request.POST.get('EstimatedReturnVal')
        temp['EstimatedLoss'] = request.POST.get('EstimatedLossVal')
        temp['BorrowerRate'] = request.POST.get('BorrowerRateVal')
        temp['LenderYield'] = request.POST.get('LenderYieldVal')
    testDtaa = pd.DataFrame({'x': temp}).transpose()
    testDtaa = testDtaa[['LP_CustomerPrincipalPayments', 'LP_CustomerPayments', 'BorrowerAPR',
                         'EstimatedEffectiveYield', 'LoanMonthsSinceOrigination',
                        'DateCreditPulledYear', 'ListingCreationDateYear', 'EstimatedReturn',
                         'LoanOriginationDateYear', 'EstimatedLoss', 'BorrowerRate',
                         'LenderYield']]
    scoreVal = reloadedModel.predict(testDtaa)[0]
    context = {'scoreVal': scoreVal, 'temp': temp}
    return render(request, 'index.html', context)


# client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['mpgDataBase']
collectionD = db['mpgTable']


def updateDataBase(request):
    temp = {}
    temp['LP_CustomerPrincipalPayments'] = request.POST.get(
        'LP_CustomerPrincipalPaymentsVal')
    temp['LP_CustomerPayments'] = request.POST.get('LP_CustomerPaymentsVal')
    temp['BorrowerAPR'] = request.POST.get('BorrowerAPRVal')
    temp['EstimatedEffectiveYield'] = request.POST.get(
        'EstimatedEffectiveYieldVal')
    temp['LoanMonthsSinceOrigination'] = request.POST.get(
        'LoanMonthsSinceOriginationVal')
    temp['DateCreditPulledYear'] = request.POST.get('DateCreditPulledYearVal')
    temp['ListingCreationDateYear'] = request.POST.get(
        'ListingCreationDateYearVal')
    temp['LoanOriginationDateYear'] = request.POST.get(
        'LoanOriginationDateYearVal')
    temp['EstimatedReturn'] = request.POST.get('EstimatedReturnVal')
    temp['EstimatedLoss'] = request.POST.get('EstimatedLossVal')
    temp['BorrowerRate'] = request.POST.get('BorrowerRateVal')
    temp['LenderYield'] = request.POST.get('LenderYieldVal')
    collectionD.insert_one(temp)
    countOfrow = collectionD.find().count()

    context = {'countOfrow': countOfrow}
    return render(request, 'viewDB.html', context)
