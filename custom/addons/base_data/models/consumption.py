# -*- coding: utf-8 -*-
import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ConsumptionItems(models.Model):
    _name = 'consumption.items'
    _inherit = 'common.model.mix'

    name = fields.Char(string='名称', required=True)
    consumption_type = fields.Selection(selection=[('in', '收入'), ('out', '支出')], required=True)

    line_ids = fields.One2many(comodel_name='consumption.items.line', inverse_name='item_id', string='明细行')


class ConsumptionItemsLine(models.Model):
    _name = 'consumption.items.line'
    _inherit = 'common.model.mix'

    name = fields.Char(string='名称')
    price = fields.Float(string='单价')

    item_id = fields.Many2one(comodel_name='consumption.items', string='项目管理 ID')
