from odoo import fields, models


class CommonModelMix(models.AbstractModel):
    _name = 'common.model.mix'
    _description = 'Common Model'

    def _default_sequence(self):
        return (self.search([], order="sequence desc", limit=1).sequence or 0) + 1

    active = fields.Boolean(string='Active', default=True)
    sequence = fields.Integer(string='Sequence', default=_default_sequence)

    def unlink(self):
        for record in self:
            record.active = False

        return True
