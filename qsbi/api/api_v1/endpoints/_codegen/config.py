from module import APIModule

get_by_attrs_id = [
    {'name': 'id', 'type': 'int'},
]

get_by_attrs_id_name = [
    {'name': 'id', 'type': 'int'},
    {'name': 'name', 'type': 'str'}
]

get_by_attrs_id_login = [
    {'name': 'id', 'type': 'int'},
    {'name': 'login', 'type': 'str'}
]

get_by_attrs_currency = [
    {'name': 'id', 'type': 'int'},
    {'name': 'name', 'type': 'str'},
    {'name': 'nickname', 'type': 'str'},
    {'name': 'code', 'type': 'str'}
]

APIModule("account", "Account", get_by_attrs_id_name),
APIModule("account_type", "AccountType", get_by_attrs_id_name),
APIModule("audit_log", "AuditLog", get_by_attrs_id),
APIModule("bank", "Bank", get_by_attrs_id_name),
APIModule("category", "Category", get_by_attrs_id_name),
APIModule("currency", "Currency", get_by_attrs_currency),
APIModule("currency_link", "CurrencyLink", get_by_attrs_id),
APIModule("party", "Party", get_by_attrs_id_name),
APIModule("payment", "Payment", get_by_attrs_id),
APIModule("payment_type", "PaymentType", get_by_attrs_id_name),
APIModule("reconcile", "Reconcile", get_by_attrs_id),
APIModule("scheduled", "Scheduled", get_by_attrs_id),
APIModule("sub_category", "SubCategory", get_by_attrs_id),
APIModule("transact", "Transact", get_by_attrs_id),
#APIModule("user", "User", get_by_attrs_id_login), - user moved to admin
