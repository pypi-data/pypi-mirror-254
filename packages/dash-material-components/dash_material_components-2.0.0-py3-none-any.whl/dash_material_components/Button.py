# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Button(Component):
    """A Button component.
Button component

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Component children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- color (a value equal to: 'primary', 'secondary', 'error', 'inherit', 'success', 'info', 'warning'; optional):
    MUI button color.

- disableElevation (boolean; optional):
    Disable elevation.

- disableFocusRipple (boolean; optional):
    Disable keyboard focus ripple.

- disableRipple (boolean; optional):
    Button has no ripple effect.

- disabled (boolean; optional):
    Button is disabled.

- endIcon (string; optional):
    Material Icon name to display at end of button.

- href (string; optional):
    Button link.

- iconColor (a value equal to: 'disabled', 'primary', 'secondary', 'action', 'error'; optional):
    Icon color.

- margin (string | number; optional):
    Component margin.

- nClicks (number; optional):
    Number of times the button has been clicked.

- size (a value equal to: 'small', 'medium', 'large'; optional):
    MUI button size, small | medium | large.

- startIcon (string; optional):
    Material Icon name to display at start of button.

- text (string; optional):
    Button text.

- variant (a value equal to: 'outlined', 'text', 'contained'; optional):
    MUI button variant.

- width (string; optional):
    Component width."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_material_components'
    _type = 'Button'
    @_explicitize_args
    def __init__(self, children=None, text=Component.UNDEFINED, variant=Component.UNDEFINED, color=Component.UNDEFINED, iconColor=Component.UNDEFINED, size=Component.UNDEFINED, margin=Component.UNDEFINED, disabled=Component.UNDEFINED, disableRipple=Component.UNDEFINED, disableFocusRipple=Component.UNDEFINED, disableElevation=Component.UNDEFINED, startIcon=Component.UNDEFINED, endIcon=Component.UNDEFINED, href=Component.UNDEFINED, width=Component.UNDEFINED, nClicks=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'color', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'disabled', 'endIcon', 'href', 'iconColor', 'margin', 'nClicks', 'size', 'startIcon', 'text', 'variant', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'color', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'disabled', 'endIcon', 'href', 'iconColor', 'margin', 'nClicks', 'size', 'startIcon', 'text', 'variant', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Button, self).__init__(children=children, **args)
