import dracula.draw

# Load existing settings made via :set
config.load_autoconfig()

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})


config.set('content.javascript.enabled', True)
c.fonts.default_family = 'Lato Black'
c.colors.hints.fg = 'cyan'
c.colors.hints.bg = 'black'
c.fonts.web.family.standard = 'Lato Black'

"""
import catppuccin

# load your autoconfig, use this, if the rest of your config is empty!
config.load_autoconfig()

# set the flavor you'd like to use
# valid options are 'mocha', 'macchiato', 'frappe', and 'latte'
# last argument (optional, default is False): enable the plain look for the menu rows
catppuccin.setup(c, 'mocha', True)


import os
from urllib.request import urlopen

# load your autoconfig, use this, if the rest of your config is empty!
config.load_autoconfig()

if not os.path.exists(config.configdir / "theme.py"):
    theme = "https://raw.githubusercontent.com/catppuccin/qutebrowser/main/setup.py"
    with urlopen(theme) as themehtml:
        with open(config.configdir / "theme.py", "a") as file:
            file.writelines(themehtml.read().decode("utf-8"))

if os.path.exists(config.configdir / "theme.py"):
    import theme
    theme.setup(c, 'mocha', True)

c.fonts.default_family = 'Lato Black'
c.colors.hints.fg = 'cyan'
c.colors.hints.bg = 'black'
c.fonts.web.family.standard = 'Lato Black'
config.set('content.javascript.enabled', True)
# c.fonts.default_family = 'source code pro'
"""
