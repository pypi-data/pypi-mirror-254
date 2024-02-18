from odoo import _,models,fields

class SaleOrderReportWizard(models.TransientModel):
    _name = "sale_order.report.wizard"           

    langs = fields.Many2many("res.lang", string=_("Language"), default=lambda self:self.env['res.lang'].search([]).ids)
    template = fields.Selection(string=_("Template"), selection=[('normal', _('Normal')), ('no_delivery_times', _('No delivery times'))], default='normal')
    zipped = fields.Boolean(string=_("Zip"), default=True)
   
    def action_print_report(self):        
        data = {
            "form_data": self.read()[0],
            "active_id": self.env.context.get('active_id'),
            "active_ids": self.env.context.get('active_ids'),
        }
        
        report_action = self.env.ref("sale_order_mitxelena.action_report_sale_order").report_action(self, data=data)
        report_action['close_on_report_download']=True
        
        return report_action