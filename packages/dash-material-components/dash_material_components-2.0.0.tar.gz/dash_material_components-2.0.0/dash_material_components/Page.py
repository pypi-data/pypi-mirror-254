# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Page(Component):
    """A Page component.
Page component, used to wrap section and card components
Dashboard > Page

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Component children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- errorMessage (string; optional):
    Error message.

- errorStatus (number; optional):
    Error status code.

- orientation (a value equal to: 'columns', 'rows'; optional):
    Page general orientation (rows or columns)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_material_components'
    _type = 'Page'
    @_explicitize_args
    def __init__(self, children=None, orientation=Component.UNDEFINED, errorStatus=Component.UNDEFINED, errorMessage=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'errorMessage', 'errorStatus', 'orientation']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'errorMessage', 'errorStatus', 'orientation']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Page, self).__init__(children=children, **args)
