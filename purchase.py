import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

from osv import osv, fields
import netsvc
import pooler
from tools.translate import _
import decimal_precision as dp
from osv.orm import browse_record, browse_null

class purchase_order_line(osv.osv):
    _inherit  = 'purchase.order.line'
    
    # imposta le posizioni dei decimali a seconda del prezzo di acquisto 
    
    
    _columns = {
                'product_qty': fields.float('Quantity', required=True, digits_compute= dp.get_precision('Purchase Price'))
                }
    
    
    
    
purchase_order_line()