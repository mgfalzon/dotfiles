# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget

from typing import List  # noqa: F401

# Matt's Imports
from libqtile.config import ScratchPad, DropDown

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    # Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("termite")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    # Key([mod], "r", lazy.spawncmd()),

    ### Matt's Custom Keybindings ###

    # File Manager
    Key([mod], "e", lazy.spawn('termite -e vifm')),

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

    # Browser
    Key([mod], "f", lazy.spawn("firefox")),

    # Windows Workspace Management
    Key(["mod1"], "Tab", lazy.layout.next()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod], "l", lazy.screen.next_group()),
    Key([mod], "h", lazy.screen.prev_group()),

    # Testing
    Key([mod], "o", lazy.screen.increase_ratio()),
    Key([mod], "p", lazy.screen.decrease_ratio()),
]

groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        # Key([mod, "control"], "Right", lazy.group[nextGroup(i.name)].toscreen()),
        # mod1 + shift + letter of group = switch to & move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to swtch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

# ocean -> border_focus=("#676f7a")
# onedark 1 ->border_focus #353b45
# onedark 2 ->border_focus #4d515b
# layout.MonadTall(name='stack', border_normal=('#2c303b'), border_focus=("#4d515b"), margin=10),
layouts = [
    layout.MonadTall(name='stack', border_width=0, margin=15),
    layout.Max(margin=10),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(name='wide', border_normal=('#2c303b'), border_focus=("#4d515b"), margin=10),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
##### CUSTOM WIDGET SETTINGS #####

##### COLORS #####
''' ocean
colors = [["#2c303b", "#2c303b"], # panel background
          ["#3d4252", "#3d4252"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#bd626b", "#bd626b"], # border line color for current tab
          ["#bd626b", "#bd626b"], # border line color for other tab and odd widgets
          ["#a3bd8d", "#a3bd8d"], # color for the even widgets
          ["#a3bd8d", "#a3bd8d"]] # window name
'''

colors = [["#282c35", "#282c35"], # panel background
          ["#393f4c", "#393f4c"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#61afef", "#61afef"], # border line color for current tab
          ["#61afef", "#61afef"], # border line color for other tab and odd widgets
          ["#c678dd", "#c678dd"], # color for the even widgets
          ["#99c379", "#99c379"]] # window name

##### WIDGETS #####
defaultWidgets = [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("default config", name="default"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
]


customWidgets = [
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
            foreground = colors[6],
            background = colors[0],
            padding = 0
            ),
   widget.TextBox(
            text='◀',
            background = colors[0],
            foreground = colors[5],
            padding=-3.5,
            fontsize=55
            ),
   widget.Battery(
            foreground = colors[2],
            background = colors[5],
            padding=5,
            format='{char} {percent:2.0%}'
            ),
   widget.TextBox(
            text='◀',
            background = colors[5],
            foreground = colors[4],
            padding=-3.5,
            fontsize=55
            ),
   widget.CurrentLayout(
            foreground = colors[2],
            background = colors[4],
            padding = 5
            ),
   widget.TextBox(
            text='◀',
            background = colors[4],
            foreground = colors[5],
            padding=-3.5,
            fontsize=55
            ),
   widget.Clock(
            foreground = colors[2],
            background = colors[5],
            format="%A, %B %d  [ %H:%M ]"
            ),
   widget.Sep(
            linewidth = 0,
            padding = 10,
            foreground = colors[0],
            background = colors[5]
            ),
   widget.Systray(
            background=colors[0],
            padding = 5
            ),
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=3,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

'''
screens = [
    Screen(
        top=bar.Bar(
            customWidgets,
            24
        ),
    ),
]
'''
screens =[Screen()]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Matt's Config
from libqtile import hook
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
