from flask import Flask, request, jsonify
import xmlrpc.client

class SaleOrderModel:
    def __init__(self):
        # Allow passing an external Flask app instance or create a new one
        self.app = Flask(__name__)
        self.register_routes()

    def register_routes(self):
        self.app.route('/create_sale_order', methods=['POST'])(self.create_sale_order)
        self.app.route('/get_sale_order_data', methods=['POST'])(self.get_sale_order_data)

    def connect_to_odoo(self, data):
        odoo_url = data.get('odoo_server_url')
        database = data.get('database_name')
        username = data.get('odoo_username')
        password = data.get('odoo_password')

        if not all([odoo_url, database, username, password]):
            return jsonify({'error': 'Missing Odoo XML-RPC configuration data'}), 400

        common = xmlrpc.client.ServerProxy(f'{odoo_url}/xmlrpc/2/common')
        uid = common.authenticate(database, username, password, {})
        models = xmlrpc.client.ServerProxy(f'{odoo_url}/xmlrpc/2/object')

        return models, uid, database, password

    def create_sale_order(self, data):
        models, uid, database, password = self.connect_to_odoo(data)

        try:
            if 'customerId' in data or 'customerNumber' in data:
                partnerId = data.get('customerId') or models.execute_kw(database, uid, password, 'res.partner', 'search',
                                                                    [['|', ["phone", "=", data.get('customerNumber')],
                                                                      ["mobile", "=", data.get('customerNumber')]]])
        except xmlrpc.client.Fault as e:
            partnerId = None  # Set to None if an exception occurs

        try:
            if 'resellerId' in data or 'resellerNumber' in data:
                resellerId = data.get('resellerId') or models.execute_kw(database, uid, password, 'res.partner', 'search',
                                                                         [['|', ["phone", "=", data.get('resellerNumber')],
                                                                           ["mobile", "=", data.get('resellerNumber')]]])
            else:
                resellerId = None
        except xmlrpc.client.Fault as e:
            resellerId = None  # Set to None if an exception occurs

        saleObj = {
            **({'name': str(data.get('name')) } if 'name' in data and data['name'] else {}),
            **({'partner_id': partnerId[0] } if partnerId is not None else {}),
            **({'l10n_in_reseller_partner_id': resellerId[0] } if resellerId is not None else {}),
            **({'validity_date': data.get('expirationDate')} if 'expirationDate' in data and data['expirationDate'] else {}),
            **({'date_order': data.get('quotationDate')} if 'quotationDate' in data and data['quotationDate'] else {}),
            **({'pricelist_id': (models.execute_kw(database, uid, password, 'product.pricelist', 'search',
                                                    [[["name", "=", data.get('pricelist')]]])
                                 if 'pricelist' in data else None)} if 'pricelist' in data and data['pricelist'] else {}),
            'order_line': [],
        }

        # Add order lines if order line data is provided
        productIdsArray = []
        productVariantIdsArray = []

        if 'orderLine_productNames' in data:
            for productName in data.get('orderLine_productNames'):
                if productName != '':
                    productId = models.execute_kw(database, uid, password, 'product.template', 'search_read',
                                                  [[["name", "=", productName]]])
                    productIdsArray.append(productId[0]['id'])
                    productVariantIdsArray.append(productId[0]['product_variant_id'][0])

        if 'orderLine_productId' in data:
            for productIdd in data.get('orderLine_productId'):
                if productIdd != '':
                    productId = models.execute_kw(database, uid, password, 'product.template', 'search_read',
                                                  [[["id", "=", productIdd]]])
                    productIdsArray.append(productId[0]['id'])
                    productVariantIdsArray.append(productId[0]['product_variant_id'][0])

        description = data.get('orderLine_description', [])
        quantity = data.get('orderLine_quantity', [])
        unitPrice = data.get('orderLine_unitPrice', [])
        taxes = data.get('orderLine_taxes', [])
        discount = data.get('orderLine_discount', [])

        salesObjDynamicPayload = []

        for index in range(max(len(description), len(quantity), len(unitPrice), len(taxes), len(discount),
                               len(productIdsArray), len(productVariantIdsArray))):
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

    def get_sale_order_data(self, data):
        models, uid, database, password = self.connect_to_odoo(data)

        try:
            order_id = data.get('orderID')
            if not order_id:
                return jsonify({'error': 'Missing orderID in the request'}), 400

            # Fetch sales order data
            sale_order_data = models.execute_kw(database, uid, password, 'sale.order', 'search_read', [[["name", "=", order_id]]])

            if not sale_order_data:
                return jsonify({'error': f'Sale order with ID {order_id} not found'}), 404

            # You can process the sale_order_data as needed
            return jsonify({'sale_order_data': sale_order_data})

        except xmlrpc.client.Fault:
            return jsonify({'error': 'Error fetching sale order data'}), 500

    def run(self, run_server=False):
        # Run the Flask app only if explicitly requested
        if run_server:
            self.app.run()
