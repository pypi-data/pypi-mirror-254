from flask import Flask, request, jsonify
import xmlrpc.client

class ResPartnerModel:
    def __init__(self):
        # Allow passing an external Flask app instance or create a new one
        self.app = Flask(__name__)
        self.register_routes()

    def register_routes(self):
        self.app.route('/create_contact', methods=['POST'])(self.create_contact)
        self.app.route('/get_contact_data', methods=['POST'])(self.get_contact_data)

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
    
    def create_contact(self, data):
        models, uid, database, password = self.connect_to_odoo(data)
        # Initialize Variables
        country_name = None
        country_id = None
        state_name = None
        state_id = None
        parent_name = None
        parent_id = None
        title = None
        title_id = None
        tags = None
        tags_id = None

        # Get Country ID from Country Name
        if data.get('country'):
            country_name = data.get('country')  # Optional
            country_id = models.execute_kw(database, uid, password, 'res.country', 'search', [[["name", "=", country_name]]])
            data['country_id'] = country_id[0]

        # Get State ID from State Name
        if data.get('state'):
            if not data.get('country'):
                return jsonify({"Error": "Country name must be provided with state name."}), 400
            else:
                state_name = data.get('state')  # Optional
                state_id = models.execute_kw(database, uid, password, 'res.country.state', 'search', [[['name', '=', state_name], ['country_id', '=', country_id]]])
                data['state_id'] = state_id[0]

        # Get parent_id from 'Company Name'
        if data.get('company_name'):
            parent_name = data.get('company_name')  # Optional
            parent_id = models.execute_kw(database, uid, password, 'res.partner', 'search', [[["name", "=", parent_name]]])
            data['parent_id'] = parent_id[0]

        # Get title_id from 'title'
        if data.get('title'):
            title = data.get('title')  # Optional
            title_id = models.execute_kw(database, uid, password, 'res.partner.title', 'search', [[["name", "=", title]]])
            data['title_id'] = title_id[0]

        # Get tags_id from 'tag'
        if data.get('tags'):
            tags = data.get('tags')  # Optional
            tags_id = models.execute_kw(database, uid, password, 'res.partner.title', 'search', [[["name", "=", tags]]])
            data['tags_id'] = tags_id

        # Extract necessary data from the request
        company_type = data.get('company_type') #Optional (SELECTION: person/company)
        name = data.get('contact_name') #Mandatory
        partner_id = parent_id #Optional
        type = data.get('address_type') #Optional
        street = data.get('street1') #Optional
        street2 = data.get('street2') #Optional
        city = data.get('city') #Optional
        state_id = state_id #Optional
        zip = data.get('zip') #Optional
        country_id = country_id #Optional
        l10n_in_gst_treatment = data.get('gst_treatment') #Optional (SELECTION: regular/composition/unregistered/consumer/overseas/special_economic_zone/deemed_export)
        vat = data.get('vat') #Optional
        function = data.get('job_position') #Optional
        phone = data.get('phone') #Optional
        mobile = data.get('mobile') #Optional
        email = data.get('email') #Optional
        website = data.get('website') #Optional
        title = title_id #Optional
        category_id = tags_id #Optional

        # Initialize an empty dictionary for contactObj
        contactObj = {}

        # Define a mapping of optional fields to their corresponding keys in data
        optional_fields_mapping = {
            'name': 'contact_name',
            'company_type': 'company_type',
            'parent_id': 'parent_id',
            'type': 'address_type',
            'street': 'street1',
            'street2': 'street2',
            'city': 'city',
            'state_id': 'state_id',
            'zip': 'zip',
            'country_id': 'country_id',
            'l10n_in_gst_treatment': 'gst_treatment',
            'vat': 'vat',
            'function': 'job_position',
            'phone': 'phone',
            'mobile': 'mobile',
            'email': 'email',
            'website': 'website',
            'title_id': 'title_id',
            'category_id': 'tags_id'
        }

        # Iterate through optional fields and add them to contactObj if present in data
        for field_key, data_key in optional_fields_mapping.items():
            if data.get(data_key):
                contactObj[field_key] = data[data_key]

        # Create Contact Object
        createContact = models.execute_kw(database, uid, password, 'res.partner', 'create', [contactObj])

        return jsonify({'contact_id': createContact})
    
    def get_contact_data(self, data):
        models, uid, database, password = self.connect_to_odoo(data)

        try:
            phone = data.get('phone')
            name = data.get('name')

            if not phone and not name:
                return jsonify({'error': 'Missing phone and name in the request'}), 400

            # Fetch contact data
            search_domain = []
            if name and name != '':
                search_domain.append([["name", "=", name]])
            if phone:
                search_domain.append(['|', ["phone", "=", phone], ["mobile", "=", phone]])
            contact_data = models.execute_kw(database, uid, password, 'res.partner', 'search_read', search_domain)
            
            if not contact_data:
                if name and not phone:
                    return jsonify({'error': f'Contact with Name: {name} not found'}), 404
                elif phone and not name:
                    return jsonify({'error': f'Contact with Phone: {phone} not found'}), 404
            return jsonify({'contact_data' : contact_data})
        
        except xmlrpc.client.Fault as e:
            return jsonify({'error': f'Error fetching contact data - {str(e)}'}), 500
    def run(self, run_server=False):
        # Run the Flask app only if explicitly requested
        if run_server:
            self.app.run()