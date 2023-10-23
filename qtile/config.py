1# Copyright (c) 2010 Aldo Cortesi
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

from libqtile import bar, layout, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration, BorderDecoration
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupWidget
)
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)
mod = "mod4"
terminal = "alacritty"






keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows




    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "l", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "m", lazy.spawn("alacritty -e neomutt")),




    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod],"e", lazy.spawn("thunar"), desc='file manager'),
    Key([mod], "h", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod], "w", lazy.spawn("firefox"), desc='Firefox'),
    Key([mod, "shift"] ,"n", lazy.spawn("sh -c ~/.config/qtile/nordmod.sh"), desc="nord"),
    Key([mod], "n", lazy.spawn("nordvpn connect switzerland"), desc="swis"),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod], "s", lazy.spawn("spotify")),
    Key([mod, "shift"] ,"p", lazy.spawn("sh -c ~/.config/rofi/powermenu.sh")),
    Key([mod], "h", lazy.hide_show_bar("top")),
    Key([mod], "j", lazy.hide_show_bar("bottom")), 


]

#Defualt groups
#groups = [Group(i) for i in "123456789"]


#nerdfont icons   #replacments      󰊠 󰏃   "  
groups = [
    Group('1', label="",),
    Group('2', label="", matches = [Match(wm_class = "firefox")], layout='max'),
    Group('3', label=" ",matches = [Match(wm_class = "pcmanfm")]),
    Group('4', label="󰎈", matches = [Match(wm_class = "spotify")],),
    Group('5', label="󰈙 ", matches = [Match(wm_class = "Writer")]),
    Group('6', label="", matches = [Match(wm_class = "vysor")], layout='max'),
    Group('7', label="",),
    Group('8', label="",),
    Group('9', label='󰍹',),
    Group('0', label='',),
    ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
layout_theme = {
        "border_width": 2,
        "margin": 2,
        "border_focus": "1FFD2E",
        "border_normal": "bc35e6"
}


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2,**layout_theme),
    # layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

def search():
    qtile.cmd_spawn("rofi -show drun")



right = {
    "decorations": [
        RectDecoration(use_widget_background=True, padding_y=5, filled=True, radius=6),
        PowerLineDecoration(path="forward_slash",)
    ]
}

left = {
    "decorations": [
        RectDecoration(use_widget_background=True, padding_y=5, filled=True, radius=5),
        PowerLineDecoration(path="back_slash", padding_x=0, padding_y=0, padding=0)
    ]
}

widget_defaults = dict(
    font="JetBrains Mono Bold",
    fontsize=18,
    padding=3,
    background='#35344500',
    foreground='#7dcfff',
)

decorations: list = [
    RectDecoration(
        filled=True,
        group=True,
        line_width=0,
        padding_y=2,
        radius=18,
    ),
]


fill = {
    "decorations": [
        BorderDecoration(colour="#8EDfff",border_width=[2, 0, 2, 0],padding_x=0,),
        RectDecoration(colour="#00000080", radius=0, filled=True,padding_x=0, group=True),
    ],
    "padding": 20,
}
edge = {
    "decorations": [
       #  RectDecoration(colour="00000070", radius=11, filled=True,padding_x=0, group=True),
    ],
}

screens = [
    Screen(

        bottom=bar.Bar(
 

        [            widget.Image(filename='/home/craig/.config/qtile/Assets/endeavouros-icon.png',mouse_callbacks={"Button1":search},),
 widget.Image(filename='/home/craig/Assets/nvpn2.png',
                         background='#00000000',
                         mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('nordvpn connect switzerland'),'Button3': lambda: qtile.cmd_spawn('nordvpn disconnect')},
),

 widget.GenPollCommand(
   cmd = "nordvpn status|sed -n '4, 5p'" ,
   #  cmd = "nordvpn status",
    shell = True,
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('nordvpn connect switzerland'),'Button3': lambda: qtile.cmd_spawn('nordvpn disconnect')},
    update_intervall = 1,
    fontsize=10,
    ),

  widget.Spacer(length=bar.STRETCH),
      widget.Net(
                 format=' {up}   {down}   ',
                 prefix='k',
                 ),
          widget.CPU(fmt='{} ',update_interval=1),
          widget.Memory(
                    format = '{MemUsed: .1f}GB  ',

                    update_interval=1,
                    measure_mem = 'G',
            ),


       
],30, background='00000000',),

        top=bar.Bar(
          [ 




            widget.CurrentLayoutIcon(),

            widget.GroupBox(active='#00ff68',inactive='#78DCFF'),
            widget.Prompt(),

            widget.WindowName(),
           





widget.TextBox (
text = "",**edge,fontsize=40),

widget.TextBox (
text = " ",**fill,),

widget.TextBox(
text = '󰼨',
**fill,
mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('spotifycli --previous',)}
),


widget.TextBox(**fill,
text = '',
mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('spotifycli --playpause')}
),

widget.TextBox(**fill,

text = '󰼧 ',
mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('spotifycli --next')}
),

widget.GenPollCommand(**fill,
    cmd = "spotifycli --artist",
    shell = True,
   # update_interval = 2,
    scroll=True,
   # scroll_fixed_width = True,
     max_chars=9,
   # width = 150,
    ),

widget.TextBox (**fill,
text = "-",),

widget.GenPollCommand(
    cmd = "spotifycli --song",
    shell = True,
    scroll = True,
   # scroll_fixed_width = True,
  max_chars=9,
    width = 150,
**fill,
),
 # widget.Visualiser(cava_pipe='/dev/stdout', autostart=True,hight=40,bars=12,background="#000000",barcolor="#ffffff",framerate=30,cava_path='/usr/bin/cava',),
widget.TextBox (
text = "",**edge,fontsize=40),

            widget.Spacer(length=bar.STRETCH),

      
                widget.Volume(
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    background='#35344600',),

                widget.Volume(),


                widget.Clock(
                    format='  %H:%M %S ',),

            widget.TextBox (
            text = "",fontsize=40,foreground='#aa4242',padding=0,),
            widget.QuickExit(countdown_start = 2, default_text=" 󰐥 ",background='#aa4242'),
          ],
          30,
          background='00000000',
          # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
          # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,

          
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)


from libqtile import hook
# some other imports
import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart_once():
    subprocess.run('/home/craig/.config/qtile/autostart_once.sh')# path to my script, un>
    subprocess.call([home])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
