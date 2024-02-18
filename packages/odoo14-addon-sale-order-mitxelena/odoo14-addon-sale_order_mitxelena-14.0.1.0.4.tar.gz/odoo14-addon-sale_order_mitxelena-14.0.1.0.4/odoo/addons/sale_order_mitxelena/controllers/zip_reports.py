# -*- coding: utf-8 -*-
import json, zipfile, io, time
import odoo.addons.web.controllers.main as main
from odoo.tools.safe_eval import safe_eval, time
from werkzeug.urls import url_decode
from odoo.http import content_disposition, request
from odoo import http

class ZipReports(main.ReportController):
    @http.route(['/report/download/'], type='http', auth="user")
    def report_download(self, data, token):
        zipped = docids = decoded_data = ids = False
        url, format = json.loads(data)

        conv = 'pdf' if (format == 'qweb-pdf') else 'text'
        ext = 'pdf' if (format == 'qweb-pdf') else 'txt'

        report_name = url.split("/report/%s/" % conv)[1].split('?')[0]
                
        if '/' in report_name:
            report_name, docids = report_name.split('/')
            ids = [int(x) for x in docids.split(",")]

        elif '?' in url:
            url_data = url.split('?')

            decoded_data = url_decode(url_data[1]).items()
            decoded_data = dict(decoded_data)
            if decoded_data.get('options'):
                decoded_data.update(json.loads(decoded_data.pop('options')))
                ids = decoded_data['active_ids']

        report = request.env['ir.actions.report']._get_report_from_name(report_name)

        print_report_name = report.name
        file_name = "%s." % print_report_name                 

        obj = request.env[report.model].browse(ids)
        if report.print_report_name and len(obj) == 1:
            print_report_name = safe_eval(report.print_report_name, {'object': obj, 'time': time})
            file_name = print_report_name

        if decoded_data:
            zipped = decoded_data['form_data']['zipped']
            file_name += '.zip' if zipped else ext
            context = dict(request.env.context)

            if zipped:
                lang_ids = decoded_data['form_data']['langs']
                langs = request.env['res.lang'].browse(lang_ids)
                
                mem_zip = io.BytesIO()
                with zipfile.ZipFile(mem_zip, mode="w",compression=zipfile.ZIP_DEFLATED) as zf:
                    for lang in langs:
                        pdf_name = "%s_%s.%s" % (print_report_name, lang.code, ext)

                        decoded_data['form_data']['langs'] = lang.id
                        pdf = report.with_context(context)._render_qweb_pdf(None, data=decoded_data)[0]
                        zf.writestr(pdf_name, pdf)                
                res = request.make_response(mem_zip.getvalue(), headers=[('Content-Type', 'application/octet-stream')])

        if not zipped:
            if docids:
                res = self.report_routes(report_name, docids=docids, converter=conv)
            else:
                data = url_decode(url.split('?')[1]).items()
                res = self.report_routes(report_name, converter=conv, **dict(data))

        res.headers.add('Content-Disposition', content_disposition(file_name))
        res.set_cookie('fileToken', token)
        return res 
