import os
import re
import pandas as pd
import numpy as np
from datupapi.configure.config import Config
from datupapi.inventory.src.Format.inventory_format import InventoryFormat


class FunctionsInventory(InventoryFormat):
    """
        Class for return a dataframe with all the indicators         
        : param df_inv: Inventory's Dataframe with the columns Item, Location(Optional), Inventory, Transit, DemandHistory  SuggestedForecast AvgDailyUsage MaxDailyUsage
        : param committed: Boolean to enable InventoryTransit computation including Committed
        : param min_inv: Boolean to allow the minimum amount of inventory in location
        : param div_purfac: Boolean to allow data divided by purchase days 
        : param ref_secstock: Boolean to allow Security Stock Ref 
        : param exhibitions: Boolean to allow Exhibitions

        >>> df_inv = FunctionsInventory(df_inv,committed=True, min_inv=False, div_purfac=False, ref_secstock=False, exhibitions=False).functions_inventory()
    """

    def __init__(self, df_inv, committed, min_inv, ref_secstock, exhibitions, seasonality=False) -> None:      
        self.df_inv = df_inv
        self.committed = committed
        self.min_inv = min_inv        
        self.ref_secstock = ref_secstock
        self.exhibitions = exhibitions
        self.seasonality = seasonality

    def inventory(self,df):
        if (self.committed==True):
            df['InventoryTransit'] = df['Inventory'] + df['Transit'] - df['Committed']
        else:
            df['InventoryTransit'] = df['Inventory'] + df['Transit']
        
        df['InventoryTransitForecast'] = df['InventoryTransit'] - df['SuggestedForecast']
        df['LeadTimeDemand'] = df['SuggestedForecast']
        return df


    def stock(self , df):

        if ((self.ref_secstock==False) & (self.exhibitions==False) & (self.seasonality==False)):
            df['SecurityStock'] = ((df['MaxDailyUsage']*df['MaxLeadTime']) - (df['AvgDailyUsage']*df['AvgLeadTime']))
        
        elif ((self.ref_secstock==True) & (self.exhibitions==False) & (self.seasonality==False)):
            df['SecurityStock'] = df['SecurityStockDaysRef'] * df['AvgDailyUsage']
        
        elif ((self.ref_secstock==False) & (self.exhibitions==True) & (self.seasonality==False)):
            df['SecurityStock'] = (((df['MaxDailyUsage']*df['MaxLeadTime']) - (df['AvgDailyUsage']*df['AvgLeadTime']))) + df['Exhibitions']
        
        elif ((self.ref_secstock==True) & (self.exhibitions==True) & (self.seasonality==False)):
            df['SecurityStock'] = (df['SecurityStockDaysRef'] * df['AvgDailyUsage']) + df['Exhibitions']                  
        

        elif ((self.ref_secstock==False) & (self.exhibitions==False) & (self.seasonality==True)):
            df['SecurityStock'] = ((df['MaxDailyUsageSeasonality']*df['MaxLeadTime']) - (df['AvgDailyUsageSeasonality']*df['AvgLeadTime']))
        
        elif ((self.ref_secstock==True) & (self.exhibitions==False) & (self.seasonality==True)):
            df['SecurityStock'] = df['SecurityStockDaysRef'] * df['AvgDailyUsageSeasonality']
        
        elif ((self.ref_secstock==False) & (self.exhibitions==True) & (self.seasonality==True)):
            df['SecurityStock'] = (((df['MaxDailyUsageSeasonality']*df['MaxLeadTime']) - (df['AvgDailyUsageSeasonality']*df['AvgLeadTime']))) + df['Exhibitions']
        
        elif ((self.ref_secstock==True) & (self.exhibitions==True) & (self.seasonality==True)):
            df['SecurityStock'] = (df['SecurityStockDaysRef'] * df['AvgDailyUsageSeasonality']) + df['Exhibitions']      


        df['SecurityStock'] = df['SecurityStock'].fillna(0)
        df['SecurityStock'] = df['SecurityStock'].map(lambda x: 0 if x < 1 else x)
        
        df['SecurityStockDays'] = (df['SecurityStock']) / (df['AvgDailyUsage'])
        InventoryFormat(df).general_indicators_format('SecurityStockDays')

        df['StockoutDays'] = (df['Inventory']-df['SecurityStock'])/df['AvgDailyUsage']
        InventoryFormat(df).general_indicators_format('StockoutDays')

        df['InvTransStockoutDays'] = (df['InventoryTransit']-df['SecurityStock'])/df['AvgDailyUsage']
        InventoryFormat(df).general_indicators_format('InvTransStockoutDays')
        
        df['ForecastStockoutDays'] = (df['InventoryTransitForecast']-df['SecurityStock'])/df['AvgDailyUsage']
        InventoryFormat(df).general_indicators_format('ForecastStockoutDays')
        return df


    def reorder(self,df):        
        df['ReorderPoint'] = (df['LeadTimeDemand'] + df['SecurityStock']).map(lambda x: 0 if x < 0 else x) 
        df['MinReorderPoint'] = (df['MinSuggestedForecast'] + df['SecurityStock']).map(lambda x: 0 if x < 0 else x)                                
        df['ReorderPointDays'] = df['ReorderPoint'] / (df['AvgDailyUsage'])
        InventoryFormat(df).general_indicators_format('ReorderPointDays')

        df['ReorderStatus'] = df[['InventoryTransit','MinReorderPoint','SecurityStock']].apply(lambda x: 'Order' if (x['InventoryTransit'] < x['MinReorderPoint'] or x['InventoryTransit'] < x['SecurityStock']) else 'Hold', axis=1)
        df['ReorderStatus'] = df[['InventoryTransit','MinReorderPoint','ReorderStatus']].apply(lambda x: 'Hold' if (((x['MinReorderPoint'] - x['InventoryTransit']) <1 ) & ((x['MinReorderPoint'] - x['InventoryTransit']) >0 ) & (x['ReorderStatus']=='Order')) else x['ReorderStatus'], axis=1)
                
        if self.min_inv == False:
            df['RQty'] = (df['ReorderPoint'] - df['InventoryTransit'] ).map(lambda x: 0 if x < 1 else x)
            df['ReorderQty'] = df[['ReorderStatus','RQty']].apply(lambda x: x['RQty'] if (x['ReorderStatus']=='Order') else 0 , axis=1 )
            df['ReorderQty'] = df[['ReorderQty','ReorderStatus']].apply(lambda x: (0 if (x['ReorderQty'] < 1) else x['ReorderQty']) if(x['ReorderStatus']=='Order') else x['ReorderQty'], axis=1)
            
        if self.min_inv == True:
            df['RQty'] = (df['ReorderPoint'] - df['InventoryTransit']).map(lambda x: 0 if x < 1 else x)
            df['ReorderQty'] = df[['ReorderStatus','RQty','DemandHistory']].apply(lambda x: x['RQty'] if (x['ReorderStatus']=='Order') else x['DemandHistory'] , axis=1 )
            df['ReorderQty'] = df[['ReorderQty','ReorderStatus']].apply(lambda x: (0 if (x['ReorderQty'] < 1) else x['ReorderQty']), axis=1)
        return df 


    def minmax(self, df):                    
        df['MinQty'] = (df['BackSuggestedForecast'] + df['SecurityStock']- df['InventoryTransit']).map(lambda x: 0 if x < 1 else x)   
        df['MaxQty'] = (df['NextSuggestedForecast'] + df['SecurityStock']- df['InventoryTransit'] ).map(lambda x: 0 if x < 1 else x)        
        
        df['MinReorderQty'] = df[['ReorderStatus','MinQty','MaxQty']].apply(lambda x: (x['MinQty'] if (x['MinQty']<x['MaxQty']) else x['MaxQty']) if (x['ReorderStatus']=='Order') else 0 , axis=1 )
        df['MinReorderQty'] = df[['MinReorderQty','ReorderStatus']].apply(lambda x: (0 if (x['MinReorderQty'] < 1) else x['MinReorderQty']) if(x['ReorderStatus']=='Order') else x['MinReorderQty'], axis=1)
        
        df['MaxReorderQty'] = df[['ReorderStatus','MinQty','MaxQty']].apply(lambda x: (x['MinQty'] if (x['MinQty']>x['MaxQty']) else x['MaxQty']) if (x['ReorderStatus']=='Order') else 0 , axis=1 )
        df['MaxReorderQty'] = df[['MaxReorderQty','ReorderStatus']].apply(lambda x: (0 if (x['MaxReorderQty'] < 1 )else x['MaxReorderQty']) if(x['ReorderStatus']=='Order') else x['MaxReorderQty'], axis=1)        

        return df


    def purchase_factor(self,df):
        df['ReorderQtyBase'] = df['ReorderQty']
        df['BackReorderQtyBase'] = df['MinReorderQty']
        df['NextReorderQtyBase'] = df['MaxReorderQty']        
        df['ReorderQty'] = ((df['ReorderQty']/df['PurchaseFactor']).apply(np.ceil))*df['PurchaseFactor']
        df['BackReorderQty'] = ((df['MinReorderQty']/df['PurchaseFactor']).apply(np.ceil))*df['PurchaseFactor']
        df['NextReorderQty'] = ((df['MaxReorderQty']/df['PurchaseFactor']).apply(np.ceil))*df['PurchaseFactor']

        df['ReorderQtyFactor'] = round(df['ReorderQty']/df['PurchaseFactor'])

        return df

             
    def functions_inventory(self):
        """
            Return a dataframe with all the indicators         
            : param df_inv: Inventory's Dataframe with the columns Item, Location(Optional), Inventory, Transit, DemandHistory  SuggestedForecast AvgDailyUsage MaxDailyUsage
            : param committed: Boolean to enable InventoryTransit computation including Committed
            : param min_inv: Boolean to allow the minimum amount of inventory in location            
            : param ref_secstock: Boolean to allow Security Stock Ref 
            : param exhibitions: Boolean to allow Exhibitions

            >>> df_inv = functions_inventory(df_inv,min_inv=False,div_purfac=False,ref_secstock=False,exhibitions=False)  
        """
        try:            
            df = self.df_inv         
            df = self.inventory(df)
            df = self.stock(df)
            df = self.reorder(df)
            df = self.minmax(df)                                   
            df = self.purchase_factor(df)  
            df.drop(columns=['RQty','MinQty','MaxQty'], inplace=True) 

            if 'UnitCost' not in df.columns:
                df.loc[:,'UnitCost'] = 0           

            if 'TotalCost' not in df.columns:        
                df.loc[:,'TotalCost'] = df['UnitCost'] * df['ReorderQty']
            
        except KeyError as err:
            self.logger.exception(f'No column found. Please check columns names: {err}')
            print(f'No column found. Please check columns names')
            raise         
        return df 