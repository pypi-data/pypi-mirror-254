S_INVOICE_CUSTOMER_CREATE = {
    "name": {"type": "string", "required": False},
    "firstname": {"type": "string", "required": False},
    "lastname": {"type": "string", "required": False},
    "email": {"type": "string", "required": False},
    "phone": {"type": "string", "required": False},
    "reference": {"type": "string", "required": True, "empty": False},
    "address": {"type": "string", "required": False},
    "postalCode": {"type": "string", "required": False},
    "city": {"type": "string", "required": False},
    "country": {"type": "string", "required": False},
}
S_INVOICE_LINE_CREATE = {
    "itemId": {"type": "string", "required": False},
    "description": {"type": "string", "required": True},
    "quantity": {"type": "integer", "required": True, "empty": False},
    "price": {"type": "float", "required": True, "empty": False}
}
S_INVOICE_PAYMENT_INFO_CREATE = {
    "method": {"type": "string", "required": True},
    "reference": {"type": "string", "required": False},
    "date": {"type": "string", "required": True}
}
S_CS_INVOICE_CREATE = {
    "customer": {
        "type": "dict",
        "schema": S_INVOICE_CUSTOMER_CREATE,
        "required": True
    },
    "items": {
        "type": "list",
        "empty": True,
        "schema": {
            "type": "dict",
            "schema": S_INVOICE_LINE_CREATE
        }
    },
    "description": {"type": "string", "required": False},
    "reference": {"type": "string", "required": True},
    "comments": {"type": "list", "empty": True},
    "date": {"type": "string", "required": True},
    "payment": {
        "type": "dict",
        "schema": S_INVOICE_PAYMENT_INFO_CREATE,
        "required": False
    }
}

S_CS_INVOICE_UPDATE = {
    "id": {"type": "integer", "required": True}
}
