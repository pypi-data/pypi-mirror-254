from flask import Flask, request, jsonify
import xmlrpc.client

class CreateRentalLibrary:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.route('/create_rental_order', methods=['POST'])(self.create_rental_order)

    def create_rental_order(self):
        data = request.get_json()

        # Extract necessary data from the request
        customer_id = data.get('customer_id')
        product_id = data.get('product_id')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        quantity = data.get('quantity')

        # Odoo XML-RPC API configuration
        odoo_url = data.get('odoo_server_url')
        database = data.get('database_name')
        username = data.get('odoo_username')
        password = data.get('odoo_password')

        common = xmlrpc.client.ServerProxy(f'{odoo_url}/xmlrpc/2/common')
        uid = common.authenticate(database, username, password, {})

        models = xmlrpc.client.ServerProxy(f'{odoo_url}/xmlrpc/2/object')

        rentalObjDynamicPayload = []
        for i in range(len(product_id)):
            rentalObjDynamicPayload.append((0, 0, {
                'product_template_id': data['product_template_id'][i],
                'product_id': product_id[i],
                'product_uom_qty': data['quantity'][i],
                'qty_delivered_method': data.get('qty_delivered_method')
            }))
        # Create rental order in Odoo using XML-RPC
        rentalObj = {
            'partner_id': customer_id,  # ID of the customer
            'l10n_in_gst_treatment': data.get('gst_treatment'),  # GST Treatment
            'pricelist_id': 1,  # ID of the pricelist
            'is_rental_order': 1,  # Is it Rental order or Sale order
            'order_line': rentalObjDynamicPayload,
        }
        order_id = models.execute_kw(database, uid, password, 'sale.order', 'create', [rentalObj])

        return jsonify({'order_id': order_id})

    def run(self):
        # Run the Flask app
        self.app.run()
