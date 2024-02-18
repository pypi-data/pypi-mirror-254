# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class InputText(Component):
    """An InputText component.
InputText component

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Component children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- adornmentLeft (string; optional):
    An adornment to be displayed at the start of the input.

- adornmentRight (string; optional):
    An adornment to be displayed at the end of the input.

- autoFocus (boolean; optional):
    If True, the input will be focused automatically.

- disabled (boolean; optional):
    If True, the input field will be disabled.

- error (boolean; optional):
    If True, the input field will indicate an error.

- inputType (a value equal to: 'text', 'integer', 'float'; optional):
    The type of input ('text', 'integer', or 'float').

- labelText (string; optional):
    The label text displayed for the input field.

- margin (string | number; optional):
    Margin around the input field (CSS value as string or number).

- maxLength (number; optional):
    The maximum length of the input string.

- maxValue (number; optional):
    The maximum numeric value allowed (for numeric input types).

- minValue (number; optional):
    The minimum numeric value allowed (for numeric input types).

- multiline (boolean; optional):
    Whether the text field should allow multiline input.

- precision (number; optional):
    The number of decimal places to allow (for 'float' input type).

- size (a value equal to: 'small', 'medium'; optional):
    The size of the input field.

- value (string | number; optional):
    The initial value of the input.

- variant (a value equal to: 'filled', 'outlined', 'standard'; optional):
    The variant of the text field.

- width (string; optional):
    The width of the input field (CSS value as string)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_material_components'
    _type = 'InputText'
    @_explicitize_args
    def __init__(self, children=None, labelText=Component.UNDEFINED, value=Component.UNDEFINED, maxValue=Component.UNDEFINED, minValue=Component.UNDEFINED, precision=Component.UNDEFINED, inputType=Component.UNDEFINED, multiline=Component.UNDEFINED, variant=Component.UNDEFINED, maxLength=Component.UNDEFINED, autoFocus=Component.UNDEFINED, size=Component.UNDEFINED, width=Component.UNDEFINED, margin=Component.UNDEFINED, adornmentLeft=Component.UNDEFINED, adornmentRight=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'adornmentLeft', 'adornmentRight', 'autoFocus', 'disabled', 'error', 'inputType', 'labelText', 'margin', 'maxLength', 'maxValue', 'minValue', 'multiline', 'precision', 'size', 'value', 'variant', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'adornmentLeft', 'adornmentRight', 'autoFocus', 'disabled', 'error', 'inputType', 'labelText', 'margin', 'maxLength', 'maxValue', 'minValue', 'multiline', 'precision', 'size', 'value', 'variant', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(InputText, self).__init__(children=children, **args)
