from libqtile.config import Key, Screen, Group
from libqtile.lazy import lazy
from libqtile import layout

from typing import List  # noqa: F401

# Startup Config
from libqtile import hook
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser('~/.config/bin/startup')
    subprocess.call([script])

# Keybindings
mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),

    # Layout switching, kill window, restart, shutdown
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Workspace Management
    Key(["mod1"], "Tab", lazy.layout.next()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod], "l", lazy.screen.next_group()),
    Key([mod], "h", lazy.screen.prev_group()),

    # Terminal
    Key([mod], "Return", lazy.spawn("termite")),

    # File Manager
    Key([mod], "e", lazy.spawn('termite -e vifm')),

    # Browser
    Key([mod], "f", lazy.spawn("firefox")),

    # fzf (search & open => custom bash scripts)
    Key([mod], "p", lazy.spawn('termite -e search')),
    Key([mod], "o", lazy.spawn('termite -e open')),

    # Rofi
    Key([mod], "r", lazy.spawn(
        'rofi -modi drun -display-drun "" ' +
        '-lines 12 -padding 18 ' +
        '-width 60 -location 0 ' +
        '-columns 2 ' +
        '-font "Ubuntu Mono 12" ' +
        '-hide-scrollbar ' +
        '-show'
    )),
]

# Workspaces
groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend([
        # mod + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        # mod + shift + letter of group = switch to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

# Layouts
layouts = [
    layout.MonadTall(name='stack', border_width=0, margin=15),
    layout.Max(margin=10)
]
screens =[Screen()]

# Needed for Java Applications
wmname = "LG3D"
