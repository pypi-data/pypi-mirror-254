# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Table(Component):
    """A Table component.
Table component

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Component children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- columns (list of dicts; required):
    Array of table columns to render.

    `columns` is a list of dicts with keys:

    - field (string; required):
        Column field.

    - width (number; required):
        Column width.

- rows (list of dicts; required):
    Array of table rows to render.

    `rows` is a list of dicts with keys:


- rowsPerPageOptions (list of numbers; optional):
    Table pagination setting."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_material_components'
    _type = 'Table'
    @_explicitize_args
    def __init__(self, children=None, columns=Component.REQUIRED, rows=Component.REQUIRED, rowsPerPageOptions=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'columns', 'rows', 'rowsPerPageOptions']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'columns', 'rows', 'rowsPerPageOptions']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['columns', 'rows']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Table, self).__init__(children=children, **args)
