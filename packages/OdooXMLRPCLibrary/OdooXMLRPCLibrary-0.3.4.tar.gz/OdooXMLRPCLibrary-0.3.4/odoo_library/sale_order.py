from flask import Flask, request, jsonify
import xmlrpc.client

class SaleOrderModel:
    def __init__(self):
        # Allow passing an external Flask app instance or create a new one
        self.app = Flask(__name__)
        self.register_routes()

    def register_routes(self):
        self.app.route('/create_sale_order', methods=['POST'])(self.create_sale_order)

    def create_sale_order(self, data):
        # Odoo XML-RPC API configuration
        odoo_url = data.get('odoo_server_url')  # Mandatory
        database = data.get('database_name')    # Mandatory
        username = data.get('odoo_username')    # Mandatory
        password = data.get('odoo_password')    # Mandatory

        # Check if Odoo XML-RPC configuration data is given
        if not all([odoo_url, database, username, password]):
            # If any of the required data is missing, return an error
            return jsonify({'error': 'Missing Odoo XML-RPC configuration data'}), 400

        # Make Odoo XML-RPC Connection
        common = xmlrpc.client.ServerProxy(f'{odoo_url}/xmlrpc/2/common')
        uid = common.authenticate(database, username, password, {})
        models = xmlrpc.client.ServerProxy(f'{odoo_url}/xmlrpc/2/object')

        try:
            partnerId = data.get('customerId') or models.execute_kw(database, uid, password, 'res.partner', 'search',
                                                                     [['|', ["phone", "=", data.get('customerNumber')],
                                                                       ["mobile", "=", data.get('customerNumber')]]])
        except xmlrpc.client.Fault as e:
            partnerId = None  # Set to None if an exception occurs

        try:
            resellerId = data.get('resellerId') or models.execute_kw(database, uid, password, 'res.partner', 'search',
                                                                      [['|', ["phone", "=", data.get('resellerNumber')],
                                                                        ["mobile", "=", data.get('resellerNumber')]]])
        except xmlrpc.client.Fault as e:
            resellerId = None  # Set to None if an exception occurs

        saleObj = {
            **({'name': str(data.get('name')) } if 'name' in data and data['name'] else {}),
            **({'partner_id': partnerId[0] } if partnerId is not None else {}),  # ID of the customer
            **({'l10n_in_reseller_partner_id': resellerId[0] } if resellerId is not None else {}),
            **({'validity_date': data.get('expirationDate')} if 'expirationDate' in data and data['expirationDate'] else {}),
            **({'date_order': data.get('quotationDate')} if 'quotationDate' in data and data['quotationDate'] else {}),
            **({'pricelist_id': (models.execute_kw(database, uid, password, 'product.pricelist', 'search',
                                                   [[["name", "=", data.get('pricelist')]]])
                                 if 'pricelist' in data else None)} if 'pricelist' in data and data['pricelist'] else {}),
            'order_line': [],
        }

        # Add order lines if order line data is provided
        if 'orderLine_productNames' in data:
            productIdsArray = []
            productVariantIdsArray = []

            for productName in data.get('orderLine_productNames'):
                if productName != '':
                    productId = models.execute_kw(database, uid, password, 'product.template', 'search_read',
                                                  [[["name", "=", productName]]])
                    productIdsArray.append(productId[0]['id'])
                    productVariantIdsArray.append(productId[0]['product_variant_id'][0])

            description = data.get('orderLine_description', [])
            quantity = data.get('orderLine_quantity', [])
            unitPrice = data.get('orderLine_unitPrice', [])
            taxes = data.get('orderLine_taxes', [])
            discount = data.get('orderLine_discount', [])

            salesObjDynamicPayload = []

            for index in range(max(len(description), len(quantity), len(unitPrice), len(taxes), len(discount), len(productIdsArray), len(productVariantIdsArray))):
                product_id = productIdsArray[index] if index < len(productIdsArray) else False
                variant_id = productVariantIdsArray[index] if index < len(productVariantIdsArray) else False
                description_val = description[index] if index < len(description) else ''
                quantity_val = quantity[index] if index < len(quantity) else 0.0
                unit_price_val = unitPrice[index] if index < len(unitPrice) else 0.0
                tax_id_val = [(6, 0, [taxes[index]])] if index < len(taxes) and taxes[index] else []
                discount_val = discount[index] if index < len(discount) else 0.0

                salesObjDynamicPayload.append((0, 0, {
                    'product_id': int(variant_id),
                    **({'name': str(description_val) } if description_val is not None else {}),
                    **({'product_uom_qty': float(quantity_val) } if quantity_val is not None else 1.0),
                    **({'price_unit': float(unit_price_val) } if unit_price_val is not None else {}),
                    'tax_id': tax_id_val,
                    **({'discount': float(discount_val) } if discount_val is not None else 0.0)
                }))

            saleObj['order_line'] = salesObjDynamicPayload

        createSalesOrder = models.execute_kw(database, uid, password, 'sale.order', 'create', [saleObj])

        return jsonify({'sale_order_id': createSalesOrder})

    def run(self, run_server=False):
        # Run the Flask app only if explicitly requested
        if run_server:
            self.app.run()
