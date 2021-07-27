#!/usr/bin/python

import pandas as pd
import numpy as np
import pickle
import sys
import os

def predict_proba(Year, Mileage, State, Make, Model):

    modelo =  pickle.load(open(os.path.dirname(__file__) + '/precio_cars.pkl', 'rb'))

    new_ob1 = pd.DataFrame([Year,Mileage], columns =['Year','Mileage'])
    print(new_ob)
    # Create features
    State1 = 'State_'+State
    new_obS = pd.DataFrame(np.zeros((1,32)), columns = ['State_ AK','State_ AL','State_ AR','State_ CT','State_ DC','State_ DE','State_ HI','State_ IA','State_ ID','State_ KS','State_ LA','State_ ME','State_ MI','State_ MN','State_ MS','State_ MT','State_ ND','State_ NE','State_ NH','State_ NM','State_ NV','State_ OK','State_ OR','State_ RI','State_ SC','State_ SD','State_ UT','State_ VT','State_ WI','State_ WV','State_ WY','State_Otros'])

    new_obS.loc[0,State1]=1
    
    Make1='Make_'+Make

    new_obM = pd.Dataframe(np.zeros((1,28)), columns=['Make_Acura','Make_Audi','Make_Bentley','Make_Buick','Make_Cadillac','Make_Chrysler','Make_FIAT','Make_Freightliner','Make_INFINITI','Make_Jaguar','Make_Land','Make_Lincoln','Make_MINI','Make_Mazda','Make_Mercedes-Benz','Make_Mercury','Make_Mitsubishi','Make_Nissan','Make_Pontiac','Make_Porsche','Make_Ram','Make_Scion','Make_Subaru','Make_Suzuki','Make_Tesla','Make_Volkswagen','Make_Volvo','Make_Otros'])
    
    new_obM.loc[0,Make1]=1

    Model1='Model_'+Model

    new_obMod = pd.Dataframe(np.zeros((1,347)), columns=['Model_1','Model_15002WD','Model_1500Laramie','Model_1500Tradesman','Model_200LX','Model_200S','Model_200Touring','Model_25002WD','Model_300300S','Model_3004dr','Model_300Base','Model_300Limited','Model_300Touring','Model_35004WD','Model_350Z2dr','Model_4Runner2WD','Model_4Runner4dr','Model_4RunnerLimited','Model_4RunnerRWD','Model_4RunnerTrail','Model_500Pop','Model_6','Model_911','Model_9112dr','Model_A34dr','Model_A44dr','Model_A64dr','Model_A8','Model_Accent4dr','Model_AccordEX','Model_AccordLX-S','Model_AccordSE','Model_Armada2WD','Model_Armada4WD','Model_Avalanche2WD','Model_Avalanche4WD','Model_Avalon4dr','Model_AvalonLimited','Model_AvalonTouring','Model_Azera4dr','Model_Boxster2dr','Model_C-ClassC350','Model_C702dr','Model_CC4dr','Model_CR-V2WD','Model_CR-VSE','Model_CR-ZEX','Model_CT','Model_CTCT','Model_CTS-V','Model_CTS4dr','Model_CX-7FWD','Model_CX-9AWD','Model_CX-9FWD','Model_CX-9Grand','Model_CX-9Touring','Model_Caliber4dr','Model_CamryBase','Model_CamryL','Model_Canyon2WD','Model_Canyon4WD','Model_CanyonCrew','Model_CanyonExtended','Model_CayenneAWD','Model_Cayman2dr','Model_CherokeeSport','Model_CivicEX-L','Model_CivicSi','Model_Cobalt2dr','Model_Cobalt4dr','Model_Colorado2WD','Model_Colorado4WD','Model_ColoradoExtended','Model_Compass4WD','Model_CompassLimited','Model_Continental','Model_CorvetteConvertible','Model_CorvetteCoupe','Model_CruzeLT','Model_DTS4dr','Model_Dakota2WD','Model_Dakota4WD','Model_Durango2WD','Model_Durango4dr','Model_DurangoSXT','Model_E-ClassE','Model_E-ClassE320','Model_Eclipse3dr','Model_EdgeSE','Model_EdgeSport','Model_Element2WD','Model_Element4WD','Model_EnclaveConvenience','Model_EnclavePremium','Model_Eos2dr','Model_Escalade2WD','Model_Escalade4dr','Model_EscaladeAWD','Model_Escape4dr','Model_EscapeLImited','Model_EscapeLimited','Model_EscapeS','Model_EscapeXLT','Model_Excursion137"','Model_Expedition2WD','Model_Expedition4WD','Model_ExpeditionLimited','Model_ExpeditionXLT','Model_Explorer','Model_Explorer4dr','Model_ExplorerBase','Model_ExplorerEddie','Model_F-150FX2','Model_F-150FX4','Model_F-150King','Model_F-150Limited','Model_F-150Platinum','Model_F-150STX','Model_F-250King','Model_F-250Lariat','Model_F-250XL','Model_F-250XLT','Model_F-350King','Model_F-350Lariat','Model_F-350XL','Model_F-350XLT','Model_FJ','Model_FX35AWD','Model_FiestaS','Model_FiestaSE','Model_FitSport','Model_FlexLimited','Model_FlexSE','Model_FlexSEL','Model_Focus4dr','Model_Focus5dr','Model_FocusS','Model_FocusSEL','Model_FocusST','Model_FocusTitanium','Model_Forester2.5X','Model_Forester4dr','Model_Forte','Model_ForteEX','Model_ForteSX','Model_Frontier','Model_Frontier2WD','Model_Frontier4WD','Model_FusionS','Model_FusionSEL','Model_G35','Model_G64dr','Model_GLI4dr','Model_GSGS','Model_GTI2dr','Model_GTI4dr','Model_GXGX','Model_Galant4dr','Model_Genesis','Model_Highlander','Model_Highlander4WD','Model_Highlander4dr','Model_HighlanderBase','Model_HighlanderLimited','Model_HighlanderSE','Model_ImpalaLS','Model_Impreza2.0i','Model_ImprezaSport','Model_JourneyAWD','Model_LS','Model_LSLS','Model_LX','Model_LXLX','Model_LaCrosse4dr','Model_LaCrosseAWD','Model_Lancer4dr','Model_Land','Model_Legacy','Model_Legacy3.6R','Model_Liberty4WD','Model_LibertyLimited','Model_LibertySport','Model_Lucerne4dr','Model_MDX4WD','Model_MKXAWD','Model_MKXFWD','Model_MKZ4dr','Model_MX5','Model_Matrix5dr','Model_Mazda34dr','Model_Mazda35dr','Model_Mazda64dr','Model_Milan4dr','Model_Model','Model_Monte','Model_MuranoS','Model_MustangBase','Model_MustangDeluxe','Model_MustangPremium','Model_MustangShelby','Model_Navigator','Model_Navigator2WD','Model_Navigator4WD','Model_Navigator4dr','Model_New','Model_OdysseyEX','Model_OdysseyLX','Model_Optima4dr','Model_OptimaSX','Model_Outback3.6R','Model_Outlander2WD','Model_Outlander4WD','Model_PT','Model_PacificaLimited','Model_PacificaTouring','Model_Passat','Model_Pathfinder2WD','Model_PathfinderS','Model_PathfinderSE','Model_Patriot4WD','Model_PatriotLimited','Model_Pilot2WD','Model_PilotEX','Model_PilotLX','Model_PilotSE','Model_PilotTouring','Model_PriusBase','Model_PriusFive','Model_PriusFour','Model_PriusOne','Model_Q5quattro','Model_Q7quattro','Model_QX562WD','Model_QX564WD','Model_Quest4dr','Model_RAV4','Model_RAV44dr','Model_RAV4Base','Model_RAV4FWD','Model_RAV4Sport','Model_RDXAWD','Model_RDXFWD','Model_RX-84dr','Model_Ranger2WD','Model_Ranger4WD','Model_RangerSuperCab','Model_Regal4dr','Model_RegalGS','Model_RegalPremium','Model_RegalTurbo','Model_RidgelineRTL','Model_RidgelineSport','Model_RioLX','Model_RogueFWD','Model_S2000Manual','Model_S44dr','Model_S60T5','Model_S804dr','Model_SC','Model_SL-ClassSL500','Model_SLK-ClassSLK350','Model_STS4dr','Model_Savana','Model_Sedona4dr','Model_SedonaEX','Model_Sentra4dr','Model_Sequoia4WD','Model_Sequoia4dr','Model_SequoiaLimited','Model_SequoiaPlatinum','Model_SequoiaSR5','Model_SiennaLE','Model_SiennaLimited','Model_SiennaSE','Model_SonicHatch','Model_Sorento2WD','Model_SorentoEX','Model_SorentoSX','Model_SoulBase','Model_Sportage2WD','Model_SportageAWD','Model_SportageEX','Model_SportageSX','Model_Sprinter','Model_Suburban4dr','Model_TL4dr','Model_TLAutomatic','Model_TSXAutomatic','Model_TT2dr','Model_TacomaPreRunner','Model_Tahoe4dr','Model_TahoeLS','Model_Taurus4dr','Model_TaurusLimited','Model_TaurusSE','Model_TaurusSHO','Model_Tiguan2WD','Model_TiguanS','Model_TiguanSE','Model_TiguanSEL','Model_Titan','Model_Titan2WD','Model_Titan4WD','Model_Touareg4dr','Model_TucsonAWD','Model_TucsonLimited','Model_Tundra2WD','Model_Tundra4WD','Model_TundraBase','Model_TundraLimited','Model_VeracruzAWD','Model_VeracruzFWD','Model_Versa4dr','Model_Versa5dr','Model_Vibe4dr','Model_WRXBase','Model_WRXLimited','Model_WRXPremium','Model_WRXSTI','Model_Wrangler2dr','Model_WranglerRubicon','Model_WranglerSahara','Model_WranglerX','Model_X1xDrive28i','Model_X3AWD','Model_XC60AWD','Model_XC60FWD','Model_XC60T6','Model_XC704dr','Model_XC90AWD','Model_XC90FWD','Model_XC90T6','Model_XF4dr','Model_XJ4dr','Model_XK2dr','Model_Xterra2WD','Model_Xterra4WD','Model_Xterra4dr','Model_Yaris','Model_Yaris4dr','Model_YarisBase','Model_YarisLE','Model_Yukon4dr','Model_tC2dr','Model_xB5dr','Model_xD5dr','Model_Otros']) 
    
    new_obMod.loc[0,Model1]=1
    
    new_ob = pd.concat([new_ob1,new_obS,new_obM,new_obMod], axis = 1)
    print(new_ob)
    
    # Make prediction
    p1 = clf.predict(new_ob))[0,1]

    return p1


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please enter car features')
        
    else:
        
        print('Estimated Price: ', p1)
        