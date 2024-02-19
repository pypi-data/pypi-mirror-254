from odoo import api, fields, models


class MailWizardInvite(models.TransientModel):
    _inherit = "mail.wizard.invite"

    commercial_contact_id = fields.Many2one(
        string="Commercial Contact",
        comodel_name="res.partner",
        domain=[
            ("parent_id", "=", False),
        ],
        required=False,
    )
    contact_group_id = fields.Many2one(
        comodel_name="partner_contact_group", string="Contact Group", required=False
    )

    @api.onchange("commercial_contact_id")
    def onchange_commercial_contact_id(self):
        self.contact_group_id = False

    @api.onchange("contact_group_id")
    def onchange_contact_group_id(self):
        self.partner_ids = self.contact_group_id.contact_ids
