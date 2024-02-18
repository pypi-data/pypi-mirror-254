# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Dropdown(Component):
    """A Dropdown component.
Dropdown component

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Component children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- disabled (boolean; optional):
    Disabled the component.

- helperText (string; optional):
    Text to display under the dropdown form.

- labelText (string; optional):
    Text to display in the dropdown form, when no items are selected.

- margin (string | number; optional):
    Margin of the component.

- multiple (boolean; optional):
    Allow multiple selections.

- options (list of string | numbers; required):
    Array of options to select in the dropdown form.

- selected (list of string | numbers; optional):
    Active option selection.

- width (string | number; optional):
    Width of dropdown form."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_material_components'
    _type = 'Dropdown'
    @_explicitize_args
    def __init__(self, children=None, labelText=Component.UNDEFINED, helperText=Component.UNDEFINED, width=Component.UNDEFINED, margin=Component.UNDEFINED, options=Component.REQUIRED, multiple=Component.UNDEFINED, selected=Component.UNDEFINED, disabled=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'disabled', 'helperText', 'labelText', 'margin', 'multiple', 'options', 'selected', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'disabled', 'helperText', 'labelText', 'margin', 'multiple', 'options', 'selected', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['options']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Dropdown, self).__init__(children=children, **args)
