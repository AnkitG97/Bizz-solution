import pandas as pd #Python data analysis library
import numpy as np #Python scientific computing
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

trainDf = pd.read_csv("../data/raw/order_products__train.csv")
orderDf = pd.read_csv("../data/raw/orders.csv")
productDf = pd.read_csv("../data/raw/products.csv")

priorDf = pd.read_csv("../data/raw/order_products__prior.csv")
trainDf = trainDf.append(priorDf,ignore_index = True)

trainDf['reordered'] = 1 

productCountDf = trainDf.groupby("product_id",as_index = False)["order_id"].count()

topLev = 100
productCountDf = productCountDf.sort_values("order_id",ascending = False)

topProdFrame = productCountDf.iloc[0:topLev,:]
topProdFrame = topProdFrame.merge(productDf,on = "product_id")
productId= topProdFrame.loc[:,["product_id"]]

df = trainDf[0:0]
for i in range(0,99):
    pId = productId.iloc[i]['product_id'] 
    stDf = trainDf[trainDf.product_id == pId ]
    df = df.append(stDf,ignore_index = False)

df.head()
basket = df.groupby(['order_id', 'product_id'])['reordered'].sum().unstack().reset_index().fillna(0).set_index('order_id')

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1   

basket_sets = basket.applymap(encode_units)
basket_sets.head()
basket_sets.size
frequent_itemsets = apriori(basket_sets, min_support=0.01, use_colnames=True)

frequent_itemsets

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules

rules[ (rules['lift'] >= 2) &
       (rules['confidence'] >= 0.1) ]            



