# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class InnType(models.Model):
    _name = 'inn.type'
    _description = '房型'
    _inherit = 'common.model.mix'

    name = fields.Char(string='名称', required=True)
    state = fields.Selection(selection=[('deactivate', '停用'), ('enable', '启用')], default='enable')
    rooms_num = fields.Integer(string='房间数', compute='_compute_rooms_num', store=True)
    price = fields.Float(string='单价', default=0.00)

    room_ids = fields.One2many(comodel_name='inn.room', inverse_name='inn_id', string='房间号')

    # 计算该类型房间的总数
    @api.depends('room_ids')
    def _compute_rooms_num(self):
        for record in self:
            record.rooms_num = len(record.room_ids)

    # 停用按钮
    def button_deactivate(self):
        if self.state not in ['enable']:
            pass

        self.state = 'deactivate'

    # 启用按钮
    def button_enable(self):
        if self.state not in ['deactivate']:
            pass

        self.state = 'enable'


class InnRoom(models.Model):
    _name = 'inn.room'
    _description = '房间'
    _inherit = 'common.model.mix'

    name = fields.Char(string='名称', required=True)

    inn_id = fields.Many2one(comodel_name='inn.type', string='房型类型')
