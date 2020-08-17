from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget

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

    Key([mod, "control"], "Right", lazy.screen.next_group()),
    Key([mod, "control"], "Left", lazy.screen.prev_group()),

    # Layout Management
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),

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

# Bar
colors = [["#282c35", "#282c35"], # panel background
          ["#393f4c", "#393f4c"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#61afef", "#61afef"], # border line color for current tab
          ["#61afef", "#61afef"], # border line color for other tab and odd widgets
          ["#c678dd", "#c678dd"], # color for the even widgets
          ["#99c379", "#99c379"]] # window name

widgets = [
    widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[2],
            background = colors[0]
            ),
   widget.GroupBox(font="Ubuntu Bold",
            fontsize = 9,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 3,
            active = colors[2],
            inactive = colors[2],
            rounded = False,
            highlight_color = colors[1],
            highlight_method = "line",
            this_current_screen_border = colors[3],
            this_screen_border = colors [4],
            foreground = colors[2],
            background = colors[0]
            ),
   widget.Prompt(
            font="Ubuntu Mono",
            padding=10,
            foreground = colors[3],
            background = colors[0]
            ),
   widget.Sep(
            linewidth = 0,
            padding = 40,
            foreground = colors[2],
            background = colors[0]
            ),
   widget.WindowName(
            foreground = colors[0],
            background = colors[0],
            padding = 0
            ),
   widget.TextBox(
            text='◀',
            background = colors[0],
            foreground = colors[3],
            padding=-3.5,
            fontsize=55
            ),
   widget.Clock(
            foreground = colors[2],
            background = colors[3],
            format="%A, %B %d  [ %H:%M ]"
            ),
   widget.Sep(
            linewidth = 0,
            padding = 10,
            foreground = colors[0],
            background = colors[3]
            ),
]

screens = [
    Screen(
        top=bar.Bar(
            widgets,
            24
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(["mod1"], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag(["mod1"], "Button2", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Needed for Java Applications
wmname = "LG3D"
