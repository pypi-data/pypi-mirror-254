from odoo_library.res_partner import ResPartnerModel
from odoo_library.sale_order import SaleOrderModel

# You can also instantiate the libraries if you want to provide pre-configured instances

res_partner_model_instance = ResPartnerModel()
sale_order_model_instance = SaleOrderModel()

# Running the Flask apps by default when the package is imported

res_partner_model_instance.run()
sale_order_model_instance.run()
