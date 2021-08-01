from apps.products import apps


from apps.purchases.apiGraphQl.mutations import NewPurchase

class PurchaseMutation():
    newPurchase = NewPurchase.Field()