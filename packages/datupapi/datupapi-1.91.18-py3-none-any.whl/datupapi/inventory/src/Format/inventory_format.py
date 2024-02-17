import json
import pandas as pd
import numpy as np
import os.path as path

'''with open('conf/formatBase.json') as file:
    base = json.load(file)'''


class InventoryFormat():
    def __init__(self, df) ->None:
        self.df = df

    def format_and_type(self,  FormatType:int=None):
        #formatType : 1 - Format_and_clean Function format (sort the values at the end of the function and do not fill the nans with 0 at the beginning)
        #formatType : 2 - format_tblinv Function format (fill the nans with 0 at the beginning and do not sort the df at the end)
        
        cleanAndFormatIndicators = ["Item","ItemDescription","Location","LocationDescription","Inventory","Transit", "Transfer","Committed",
                                    "InventoryTransit","InventoryTransitForecast","StockoutDays","InvTransStockoutDays","DemandHistory",
                                    "SuggestedForecast","MinSuggestedForecast","BackSuggestedForecast","NextSuggestedForecast","ForecastStockoutDays",
                                    "Ranking","AvgDailyUsage","MaxDailyUsage","AvgLeadTime","MaxLeadTime","LeadTimeDemand","SecurityStock","SecurityStockDays",
                                    "MinReorderPoint","ReorderPoint","ReorderPointDays","ReorderFreq","MinCoverage","MaxCoverage","ReorderStatus","ReorderQtyBase","ReorderQty",
                                    "BackReorderQtyBase","BackReorderQty","NextReorderQtyBase","NextReorderQty","PurchaseFactor","ReorderQtyFactor","Provider",
                                    "ProviderDescription","UM","MinOrderQty","MaxOrderQty","DeliveryFactor","PurchaseOrderUnit","PalletFactor","SecurityStockDaysRef",
                                    "Exhibitions","UnitCost","TotalCost","LastCost","UnitPrice","Stability","Customer","Country","ProductType","Weight","Dimension","Color","Origen","Gama",
                                    "Marca","MateriaPrima","JefeProducto","JefeProductoDescription","GrupoCompra","Familia","Seccion","Categoria", "Linea","Canal",
                                    "InventoryUnit","Comments"]

        cleanAndFormatCols = ["Inventory","ReorderFreq","MinCoverage","MaxCoverage","Transit","Committed","Transfer","DemandHistory","SuggestedForecast",
                              "MinSuggestedForecast","BackSuggestedForecast","NextSuggestedForecast","InventoryTransit","InventoryTransitForecast",
                              "SecurityStock","SecurityStockDays","SecurityStockDaysRef","Exhibitions","MinReorderPoint","ReorderPoint",
                              "ReorderPointDays","ReorderQtyBase","ReorderQty","BackReorderQtyBase","BackReorderQty","NextReorderQtyBase","NextReorderQty",
                              "ReorderQtyFactor","StockoutDays","ForecastStockoutDays","InvTransStockoutDays"]
        
        tblInvIndicators = ["Item","ItemDescription", "Location", "Country", "Inventory", 
                            "Transit", "TransitDate", "TransitAdditional", "Committed",
                            "UM", "InventoryTransit", "StockoutDays", "InvTransStockoutDays",
                            "Ranking", "Provider", "ProductType",  "Customer", "JefeProducto",
                            "GrupoCompra", "Seccion", "Origen", "Color", "Marca", "MateriaPrima", "Gama"]
        
        tblInvCols = ["Inventory","Transit", "Committed","InventoryTransit","StockoutDays","InvTransStockoutDays" ]

        df = self.df
        if FormatType == 2:
            df=df.fillna(0) 
            indicators = tblInvIndicators
            cols = tblInvCols
        elif FormatType == 1:
            indicators= cleanAndFormatIndicators
            cols = cleanAndFormatCols
        
        try:
            # Cambiado de enumerate a For in , ya que el val no se estaba usando
            for name in indicators:
                if name not in df.columns:
                    df[name] = "N/A"
            
            for a in cols:
                df[a] = df[a].astype(str).replace("N/A",'0')
                df[a] = df[a].astype(float) 
                df[a] = df[a].apply(np.ceil)
                df[a] = df[a].astype(int) 

            cols =  df.select_dtypes(['float']).columns
            df[cols] =  df[cols].apply(lambda x: round(x, 3))
            
            df = df[indicators]
            df = df.drop_duplicates().reset_index(drop=True) 
            if FormatType == 1:
                df = df.sort_values(by=['Ranking','Item']).drop_duplicates().reset_index(drop=True) 

        except KeyError as err:
            self.logger.exception(f'No column found. Please check columns names: {err}')
            print(f'No column found. Please check columns names')
            raise
        return df

    def general_indicators_format(self,Column:str=None):
        try:
            df=self.df               
            
            df.loc[:,Column] = df.loc[:,Column].fillna(0)
            df.loc[:,Column] = df.loc[:,Column].map(lambda x: 0 if x < 0 else x)
            df.loc[:,Column] = df.loc[:,Column].astype(str).str.replace('-inf', '0').str.replace('inf', '0').str.replace('nan', '0')
            df.loc[:,Column] = df.loc[:,Column].astype(float)
            
        except KeyError as err:
            self.logger.exception(f'No column found. Please check columns names: {err}')
            print(f'No column found. Please check columns names')
            raise         
        return df  

