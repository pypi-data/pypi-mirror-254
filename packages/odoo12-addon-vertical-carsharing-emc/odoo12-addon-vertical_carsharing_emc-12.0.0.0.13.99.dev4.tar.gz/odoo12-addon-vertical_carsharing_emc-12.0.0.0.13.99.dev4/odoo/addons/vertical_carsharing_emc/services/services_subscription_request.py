import json

import logging
from odoo.addons.component.core import Component

from odoo import fields
from odoo.tools.translate import _

from odoo.exceptions import ValidationError
from odoo.http import Response
from . import schemas
from werkzeug.exceptions import BadRequest
from odoo.addons.base_rest.http import wrapJsonException

from odoo.addons.sm_maintenance.models.models_api_services_utils import api_services_utils

_logger = logging.getLogger(__name__)


class SubscriptionRequestService(Component):
    _inherit = "subscription.request.services"

    def _prepare_create(self, params):
        utils = api_services_utils.get_instance()
        attributes = self._get_attributes_list()
        sr_create_values = utils.generate_create_dictionary(params, attributes)

        address = params["address"]
        country = self._get_country(address["country"])
        state_id = self._get_state(address["state"], country.id)
        sr_create_values_address = {
            "address": address["street"],
            "zip_code": address["zip_code"],
            "city": address["city"],
            "country_id": country.id,
            "state_id": state_id,
            "share_product_id": params["share_product"]
        }
        automatic_validation = params.get('automatic_validation')
        if automatic_validation:
            sr_create_values['automatic_validation'] = automatic_validation
            sr_create_values['skip_control_ng'] = True
        try:
            birthdate = "{} 00:00:00".format(params["birthdate"])
            sr_create_values_address["birthdate"] = birthdate
        except:
            print("company registration - no birthdate")

        return {**sr_create_values, **sr_create_values_address}

    def _validator_create(self):
        create_schema = super()._validator_create()
        create_schema.update(schemas.S_SUBSCRIPTION_REQUEST_CREATE_SC_FIELDS)
        return create_schema

    def _validator_return_create(self):
        create_return_schema = super()._validator_return_create()
        create_return_schema.update(schemas.S_SUBSCRIPTION_REQUEST_RETURN_CREATE)
        return create_return_schema

    def _to_dict(self, sr):
        result = super()._to_dict(sr)
        result["payment_mode_id"] = sr.payment_mode_id.id
        result["subscription_request_db_id"] = sr.id
        return result

    def _get_state(self, state, country_id):
        state_id = self.env['res.country.state'].search([
            ('code', '=', state),
            ('country_id', '=', country_id),
        ]).id
        if not state_id:
            raise wrapJsonException(
                BadRequest(
                    'State %s not found' % (state)
                ),
                include_description=True,
            )
        return state_id

    def _get_attributes_list(self):
        return [
            "name",
            "firstname",
            "lastname",
            "email",
            "phone",
            "lang",
            "iban",
            "ordered_parts",
            "vat",
            "gender",
            "phone",
            "firstname",
            "lastname",
            "is_company",
            "company_name",
            "company_email",
            "mobile",
            "must_register_in_cs",
            "driving_license_expiration_date",
            "image_dni",
            "image_driving_license",
            "external_obj_id",
            "representative_vat",
            "automatic_validation",
            "payment_mode_id"
        ]

    def update_invoice(self, **params):
        _logger.info("Updating invoice status: " + str(params))

        sr_id = params.get('id')
        sr = self.env['subscription.request'].browse(int(sr_id))
        if not sr.exists():
            raise ValidationError(f"Subscription request with ID {sr_id} not found.")

        invoice = sr.capital_release_request
        invoice.action_invoice_open()

        payments_vals = {
                'amount': invoice.amount_total,
                'payment_date': fields.Date.today(),
                'payment_type': 'inbound',
                'partner_id': invoice.partner_id.id,
                'partner_type': 'customer',
                'journal_id': invoice.payment_mode_id.fixed_journal_id.id,
                'payment_method_id': invoice.payment_mode_id.payment_method_id.id,
            }
        payment = self.env['account.register.payments'].with_context(active_ids=[invoice.id], active_model='account.invoice').create(payments_vals)
        payment.create_payments()

        return Response(
            json.dumps({
                'message': _("Update invoice ok"),
                'id': sr_id,
                'new_status': invoice.state,
            }),
            status=200,
            content_type="application/json"
        )
    def _validator_update_invoice(self):
        return schemas.S_CS_INVOICE_SR_UPDATE
