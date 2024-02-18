odoo.define("sale_order_mitxelena.sale_order_line", function (require) {
    "use strict";    
    var ListRenderer = require("web.ListRenderer");
    ListRenderer.include({
        _renderRow: function (record) {
            let row = this._super(record);
            var self = this;
            if (record.model == "sale.order.line") {
                row.addClass('o_list_no_open');
                // add click event
                row.bind({
                    click: function (ev) {                        
                        ev.preventDefault();
                        ev.stopPropagation();
                        self.do_action({
                            type: "ir.actions.act_window",
                            res_model: "sale.order",
                            res_id: record.data.order_id.data.id,
                            views: [[false, "form"]],
                            target: "target",
                            context: record.context || {},
                        });
                    }
                });
            }
            return row
        },
    });
});