# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GifPlayer(Component):
    """A GifPlayer component.
GifPlayer is a component the creates a playable
gif in a dash application. This provides a more 
pleasant experience since gifs will not be constantly
looping. This component requires a file path to a
gif as well as a still image to use when the gif is
paused.

Keyword arguments:

- id (string; required):
    Id for identification in callbacks.

- alt (string; optional):
    Optional alt text attribute passed to img element.

- autoplay (boolean; default False):
    A boolean which can be set True if you want to immediately bomard
    your user with a moving GIF.

- gif (string; required):
    A string address to an animated GIF image.

- height (number; optional):
    Optional number for defining the height of the component.

- still (string; required):
    A string address to a still preview of the GIF (e.g. JPG, PNG,
    etc.).

- width (number; optional):
    Optional number for defining the width of the component."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'gif_player'
    _type = 'GifPlayer'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, gif=Component.REQUIRED, still=Component.REQUIRED, autoplay=Component.UNDEFINED, alt=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alt', 'autoplay', 'gif', 'height', 'still', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alt', 'autoplay', 'gif', 'height', 'still', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'gif', 'still']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(GifPlayer, self).__init__(**args)
