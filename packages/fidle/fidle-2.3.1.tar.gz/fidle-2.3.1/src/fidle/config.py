

# ==================================================================
#          __ _     _ _                         __ _       
#         / _(_)   | | |                       / _(_)      
#        | |_ _  __| | | ___    ___ ___  _ __ | |_ _  __ _ 
#        |  _| |/ _` | |/ _ \  / __/ _ \| '_ \|  _| |/ _` |
#        | | | | (_| | |  __/ | (_| (_) | | | | | | | (_| |
#        |_| |_|\__,_|_|\___|  \___\___/|_| |_|_| |_|\__, |
#                                                     __/ |
#                                                    |___/ 
#                                                       fidle.config
# ==================================================================
# Few configuration stuffs for the Fidle practical work notebooks
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022


# ---- Version -----------------------------------------------------
# Format: x.y
#
VERSION                 = '2.3.1'

# ---- Default notebook name ---------------------------------------
#
DEFAULT_NOTEBOOK_NAME   = "Unknown"

# ---- Styles ------------------------------------------------------
#
FIDLE_MPLSTYLE          = 'mplstyles/custom.mplstyle'
FIDLE_CSSFILE           = 'css/custom.css'

# ---- Save figs or not (yes|no)
#      Overided by env : FIDLE_SAVE_FIGS
#      
SAVE_FIGS               = False

# ---- Used modules -------------------------------------------------
#
DEFAULT_KERAS_BACKEND  = 'torch'

USED_MODULES   = ['keras','numpy', 'sklearn','yaml',
                  'skimage', 'matplotlib','plotly','pandas','jupyterlab',
                  'torch', 'torchvision', 'lightning']

# ---- Install list -------------------------------------------------
#
CATALOG_URL    = 'https://fidle.cnrs.fr/fidle-admin/catalog.json'


# -------------------------------------------------------------------


__version__   = VERSION
