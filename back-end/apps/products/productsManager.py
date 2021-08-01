from apps.products.models import PurchaseProduct, Product

class ProductPruchase:
    
    def puchase_get_products_by_list(self, products_purchase):
        """
            puchase_get_products_by_list valida primero si el
            producto que se intenta comprar existe en el inventario,
            si existe lo agrega a la compra de lo contrario lanzara 
            el error correspondiente.
            Argumentos:
                products_purchase(list) - listado de productos que se van a comprar
            Retorna:
                error(dict - None)
                products(list - None)
        """
        products = []
        for item in products_purchase:
            try: 
                product = Product.objects.get(id = item.get("product_id", ""))
            except Product.DoesNotExist:
                return { "status": 400,
                            "message": """El producto elegido no se encuentra en 
                                            nuestro inventario, intenta lo de nuevo con otro productos"""
                            },[]
            else:
                purchase_product = PurchaseProduct(product = product, amount=item.get("amount"))
                purchase_product.save()
                products.append(purchase_product)
        return None, products