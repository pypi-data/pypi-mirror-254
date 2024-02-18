# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Button(Component):
    """A Button component.
A Material UI Button component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the button.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- classes (dict; optional):
    Override or extend the styles applied to the component. See [CSS
    API](https://mui.com/material-ui/api/button/#css) for more
    details.

- color (a value equal to: 'inherit', 'primary', 'secondary', 'success', 'error', 'info', 'warning' | string; optional):
    The color of the component. It supports both default and custom
    theme colours.

- disableElevation (boolean; optional):
    If `True`, no elevation is used.

- disableFocusRipple (boolean; optional):
    If `True`, the  keyboard focus ripple will be disabled.

- disableRipple (boolean; optional):
    If `True`, the ripple effect will be disabled.

- disabled (boolean; optional):
    If `True`, the button will be disabled.

- endIcon (a list of or a singular dash component, string or number; optional):
    Element placed after the children.

- fullWidth (boolean; optional):
    If `True`, the button will take up the full width of its
    container.

- href (string; optional):
    The URL to link to when the button is clicked. If defined, an `a`
    element will be used as the root node.

- n_clicks (number; default 0):
    The number of times the button has been clicked.

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Properties whose user interactions will persist after refreshing
    the component or the page.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, any
    `persisted_props` that the user has changed while using the app
    will keep those changes, as long as the new prop value also
    matches what was given originally. Used in conjunction with
    `persistence_type` and `persisted_props`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- size (a value equal to: 'small', 'medium', 'large'; optional):
    The size of the button. `small` is equivalent to the dense button
    styling.

- startIcon (a list of or a singular dash component, string or number; optional):
    Element placed before the children.

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- variant (a value equal to: 'text', 'outlined', 'contained'; optional):
    The variant to use."""
    _children_props = ['endIcon', 'startIcon']
    _base_nodes = ['endIcon', 'startIcon', 'children']
    _namespace = 'dash_mui'
    _type = 'Button'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, disableElevation=Component.UNDEFINED, disableFocusRipple=Component.UNDEFINED, disableRipple=Component.UNDEFINED, endIcon=Component.UNDEFINED, fullWidth=Component.UNDEFINED, href=Component.UNDEFINED, size=Component.UNDEFINED, startIcon=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'classes', 'color', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'disabled', 'endIcon', 'fullWidth', 'href', 'n_clicks', 'persisted_props', 'persistence', 'persistence_type', 'size', 'startIcon', 'sx', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'classes', 'color', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'disabled', 'endIcon', 'fullWidth', 'href', 'n_clicks', 'persisted_props', 'persistence', 'persistence_type', 'size', 'startIcon', 'sx', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Button, self).__init__(children=children, **args)
