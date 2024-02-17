import param
from panel.reactive import ReactiveHTML

# =============================================================================================== #
#                                                                                                 #
#   Written by Marc Skov Madsen                                                                   #
#   Code: https://github.com/holoviz/panel/issues/2802                                            #
#   https://discourse.holoviz.org/t/toast-a-pop-up-notification/2903                              #
#                                                                                                 #
# =============================================================================================== #


class Notyf(ReactiveHTML):

    """
    A notification pane made using Panel and ReacticeHTML components. Produces warning,
    success, and error messages with configurable durations, positions, etc. 

    """

    _template = """<div id="toast"></div>"""

    duration = param.Integer(2000, bounds=(0,15000))
    ripple = param.Boolean(True)
    position_x = param.Selector(default="right", objects=["left", "right"])
    position_y = param.Selector(default="bottom", objects=["bottom", "top"])
    dismissible = param.Boolean(False)
    types = param.List([])

    _dismiss_all = param.Integer()

    _error = param.String("")
    _success = param.String("")

    def error(self, message):
        self._error = message

    def success(self, message):
        self._success = message

    def dismiss_all(self):
        self._dismiss_all += 1

    def __init__(self, **params):
        if not params:
            params={}
        params["height"]=params["width"]=params["margin"]=0
        params["sizing_mode"]="fixed"
        super().__init__(**params)

    __css__ = ["https://cdn.jsdelivr.net/npm/notyf@3/notyf.min.css"]
    __javascript__ = ["https://cdn.jsdelivr.net/npm/notyf@3/notyf.min.js"]

    _scripts = {
      "render": """
function newNotyf(data) {
  var config = {
    duration: data.duration,
    ripple: data.ripple,
    position: {x: data.position_x, y: data.position_y},
    dismissible: data.dismissible,
    types: data.types
  }
  window.panelNotyf = new Notyf( config )
}
state.newNotyf=newNotyf
state.newNotyf(data)
""",
      "_error": """if ( data._error !==""){window.panelNotyf.error( data._error );data._error="";}""",
      "_success": """if ( data._success !==""){window.panelNotyf.success( data._success );data._success="";}""",
      "_dismiss_all": """window.panelNotyf.dismissAll();""",
      "duration": """state.newNotyf(data)""",
      "ripple": """state.newNotyf(data)""",
      "position_x": """state.newNotyf(data)""",
      "position_y": """state.newNotyf(data)""",
      "dismissible": """state.newNotyf(data)""",
      "types": """state.newNotyf(data)""",
    }