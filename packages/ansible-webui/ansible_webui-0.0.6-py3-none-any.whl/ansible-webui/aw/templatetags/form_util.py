from django import template

from django.forms import BoundField
from django.forms.widgets import Select
from django.core.validators import RegexValidator

from aw.model.job import BaseJobCredentials
from aw.utils.util import is_set

register = template.Library()


@register.filter
def get_form_field_attributes(bf: BoundField) -> str:
    attr_str = ''
    for key, value in bf.field.widget_attrs(bf.field.widget).items():
        attr_str += f' {key}="{value}"'

    return attr_str


@register.filter
def get_form_field_validators(bf: BoundField) -> str:
    attr_str = ''

    for validator in bf.field.validators:
        if isinstance(validator, RegexValidator):
            # pylint: disable=W0212
            # was not able to get the raw regex from regex attribute ('_lazy_re_compile')
            regex = validator._constructor_args[1]['regex']
            attr_str += f' pattern="{regex}"'
            if validator.message is not None:
                attr_str += f' title="{validator.message}"'

    return attr_str


@register.filter
def form_field_is_dropdown(bf: BoundField) -> bool:
    return isinstance(bf.field.widget, Select)


def get_form_required(bf: BoundField) -> str:
    return ' required' if bf.field.required else ''


def get_form_field_value(bf: BoundField, existing: dict) -> str:
    # PWD_ATTRS are not exposed here
    if bf.name not in existing and bf.name not in BaseJobCredentials.PWD_ATTRS:
        return ''

    if bf.name in BaseJobCredentials.PWD_ATTRS:
        enc_field = '_enc_' + bf.name
        if enc_field in existing and not is_set(existing[enc_field]):
            return ''

        if enc_field not in existing:
            value = ''

        else:
            value = BaseJobCredentials.PWD_HIDDEN

    else:
        value = str(existing[bf.name])

    return 'value="' + value + '"'


@register.filter
def get_form_field_select(bf: BoundField, existing: dict) -> str:
    selected = None
    if bf.field.initial is not None:
        selected = bf.field.initial
    elif bf.name in existing:
        selected = str(existing[bf.name])

    get_form_field_value(bf, existing)
    options_str = f'<select class="form-control" id="{bf.id_for_label}" name="{bf.name}">'

    # pylint: disable=W0212
    for option in bf.field._choices:
        is_selected = 'selected' if str(option[0]) == str(selected) else ''
        options_str += f'<option value="{option[0]}" {is_selected}>{option[1]}</option>'

    options_str += '</select>'
    return options_str


@register.filter
def get_form_field_input(bf: BoundField, existing: dict) -> str:
    field_type = ''
    if bf.name.find('pass') != -1:
        field_type = 'type="password" '

    return (f'<input class="form-control" id="{bf.id_for_label}" name="{bf.name}" {field_type}'
            f'{get_form_field_value(bf, existing)} {get_form_required(bf)}'
            f'{get_form_field_attributes(bf)} {get_form_field_validators(bf)}>')
