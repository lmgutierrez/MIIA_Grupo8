#!/usr/bin/python

import pandas as pd
from numpy import zeros as zr
from numpy import sum as npsum
import joblib
import sys
import os
import pickle

##Year=2016
##Mileage= 78000
##State= ' CA'
##Make= 'Cadillac'
##Model = 'CayenneAWD'

def predict_price_lr(Year,Mileage,State,Make,Model):

    ##modelo =  pickle.load(open('modelo_lr.pkl', 'rb'))
    modelo =  pickle.load(open(os.path.dirname(__file__) + '/modelo_lr.pkl', 'rb'))
    data=pd.DataFrame({'Year':[Year],
            'Mileage':[Mileage],
            'State':[State],
            'Make':[Make],
            'Model':[Model]})
    
    states = [' CA',' FL',' TX','Otros']
    makes = ['Acura','BMW','Cadillac','Dodge','Ford','GMC','Honda','Hyundai','Jeep','Kia','Land','Lexus','Lincoln','Mercedes-Benz','Nissan','Otros','Porsche','Ram','Toyota','Volkswagen','Volvo']
    models = ['25004WD','3','CayenneAWD','CorollaLE','Corvette2dr','CorvetteCoupe','CruzeSedan','Escalade','EscapeSE','F-1504WD','F-150Lariat','F-150SuperCrew','F-150XLT','F-250Lariat','F-350Lariat','FiestaSE','FocusSE','FusionSE','Grand','MalibuLT','Model','Otros','Rover','Sierra','Silverado','Suburban2WD','Suburban4WD','Super','Tacoma4WD','Tahoe2WD','Tahoe4WD','TahoeLT','TerrainAWD','TerrainFWD','Tundra','TundraSR5','Wrangler','Yukon']
    for state in states:
            data['State_' + state] = data.State.str.contains(state).astype(int)
    for make in makes:
            data['Make_' + make] = data.Make.str.contains(make).astype(int)
    for model in models:
            data['Model_' + model] = data.Model.str.contains(model).astype(int)
    data.drop(['State','Make','Model'], axis=1, inplace=True)
    
    p1 = modelo.predict(data)[0]

    return p1


#if __name__ == "__main__":
    
 #   if len(sys.argv) == 1:
  #      print('Please add an URL')
        
   # else:
#        url = sys.argv[1]

    #    p1 = predict_proba(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
        
     #   print(url)
      #  print('Estimate car price: ', p1)