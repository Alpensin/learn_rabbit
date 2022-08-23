from marshmallow import Schema, fields


class NewSalepointSchema(Schema):
    id = fields.Int(required=True)


class SalepointChangesSchema(Schema):
    id = fields.Int(required=True)
    has_diff_point_main_information = fields.Bool(required=True)
    has_diff_partners = fields.Bool(required=True)
    has_diff_directions = fields.Bool(required=True)
    time = fields.Nested("TimeShiftChangesSchema", required=True)


class TimeShiftChangesSchema(Schema):
    work = fields.Nested("BusinessTypedShiftSchema", required=True)
    daily = fields.Nested("BusinessTypedShiftSchema", required=True)


class BusinessTypedShiftSchema(Schema):
    b2b = fields.Bool(required=True)
    b2c = fields.Bool(required=True)
