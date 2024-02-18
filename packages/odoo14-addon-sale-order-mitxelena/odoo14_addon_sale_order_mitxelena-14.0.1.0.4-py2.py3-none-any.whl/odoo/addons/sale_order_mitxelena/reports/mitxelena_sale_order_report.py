from odoo import _, api, models
from odoo.exceptions import UserError

class SaleOrderReport(models.AbstractModel):
    _name = "report.sale_order_mitxelena.report_sale_order_template"

    @api.model
    def _get_report_values(self, docids, data=None):
        if not data.get("form_data"):
            raise UserError(
                _("Form content is missing, this report cannot be printed.")
            )
                
        if not data["form_data"].get('langs'):
            raise UserError(
                _("Please select one or more langs.")
            )
        
        selected_langs = self.env['res.lang'].browse(data["form_data"].get('langs'))
        lang_codes = []
        for l in selected_langs:
            lang_codes.append(l.code)

        template = data["form_data"].get("template")
 
        docids = data.get("active_ids")
        sale_orders = self.env['sale.order'].browse(docids)
        data = {        
            'langs': lang_codes,
            'template': template
        } 
        return {
            "doc_ids": docids,
            "doc_model": "sale.order",
            "docs": sale_orders,
            "data": data,            
        }
