products = []
current_id = 1


def get_all_products():
    return products


def get_product_by_id(product_id):
    return next((p for p in products if p["id"] == product_id), None)


def create_product(data):
    global current_id

    existing_product = next((p for p in products if p["name"] == data["name"]), None)

    if existing_product:
        return None

    product = {"id": current_id, "name": data["name"], "quantity": data["quantity"]}

    products.append(product)
    current_id += 1

    return product


def update_product(product_id, data):
    product = get_product_by_id(product_id)

    if not product:
        return None

    product["name"] = data["name"]
    product["quantity"] = data["quantity"]

    return product


def delete_product(product_id):
    global products

    products = [p for p in products if p["id"] != product_id]
