def apply_discount(product, discount):
    product_new_price = product['price'] * (1 - discount)
    assert 0 <= product_new_price <= product['price'], 'Wrong discount'
    return product_new_price

shoe = {'name': 'Fancy Boot', 'price': 2300}
print(apply_discount(shoe, 1.25))