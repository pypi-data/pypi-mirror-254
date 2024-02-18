
namespace eval ttk::theme::{themeTemplate} {{

    variable colors
    array set colors {{
        -fg             "#5c616c"
        -bg             "#f5f6f7"
        -disabledbg     "#fbfcfc"
        -disabledfg     "#a9acb2"
        -selectbg       "#5294e2"
        -selectfg       "#ffffff"
        -window         "#ffffff"
        -focuscolor     "#5c616c"
        -checklight     "#fbfcfc"
        -cboxbg     	"#bbbbbb"
    }}

    proc LoadImages {{imgdir}} {{
        variable I
        foreach file [glob -directory $imgdir *.png] {{
            set img [file tail [file rootname $file]]
            set I($img) [image create photo -file $file -format png]
        }}
    }}

    LoadImages [file join [file dirname [info script]] {themeTemplate}]

    ttk::style theme create {themeTemplate} -parent default -settings {{
        ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -selectbg $colors(-selectbg) \
            -selectfg $colors(-selectfg) \
            -fieldbg $colors(-window) \
            -font TkDefaultFont \
            -borderwidth 1 \
            -focuscolor $colors(-focuscolor)

        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        # Layouts
        ttk::style layout TButton {{
            Button.button -children {{
                Button.focus -children {{
                    Button.padding -children {{
                        Button.label -side left -expand true
                    }}
                }}
            }}
        }}

        ttk::style layout Toolbutton {{
            Toolbutton.button -children {{
                Toolbutton.focus -children {{
                    Toolbutton.padding -children {{
                        Toolbutton.label -side left -expand true
                    }}
                }}
            }}
        }}

        ttk::style layout Vertical.TScrollbar {{
            Vertical.Scrollbar.trough -sticky ns -children {{
                Vertical.Scrollbar.thumb -expand true
            }}
        }}

        ttk::style layout Horizontal.TScrollbar {{
            Horizontal.Scrollbar.trough -sticky ew -children {{
                Horizontal.Scrollbar.thumb -expand true
            }}
        }}

        ttk::style layout TMenubutton {{
            Menubutton.button -children {{
                Menubutton.focus -children {{
                    Menubutton.padding -children {{
                        Menubutton.indicator -side right
                        Menubutton.label -side right -expand true
                    }}
                }}
            }}
        }}

        ttk::style layout TCombobox {{
            Combobox.field -sticky nswe -children {{
                Combobox.downarrow -side right -sticky ns -children {{
                    Combobox.arrow -side right
                }}
                Combobox.padding -expand true -sticky nswe -children {{
                    Combobox.textarea -sticky nswe
                }}
            }}
        }}

        ttk::style layout TSpinbox {{
            Spinbox.field -side top -sticky we -children {{
                Spinbox.buttons -side right -children {{
                    null -side right -sticky {{}} -children {{
                        Spinbox.uparrow -side top -sticky nse -children {{
                            Spinbox.symuparrow -side right -sticky e
                        }}
                        Spinbox.downarrow -side bottom -sticky nse -children {{
                            Spinbox.symdownarrow -side right -sticky e
                        }}
                    }}
                }}
                Spinbox.padding -sticky nswe -children {{
                    Spinbox.textarea -sticky nswe
                }}
            }}
        }}

        # Elements
        ttk::style element create Button.button image [list $I(button-normal) \
                pressed     $I(button-pressed) \
                active      $I(button-hover) \
                disabled    $I(button-disabled) \
            ] -border 3 -padding {{3 2}} -sticky ewns

        ttk::style element create Toolbutton.button image [list $I(button-empty) \
                selected            $I(button-pressed) \
                pressed             $I(button-pressed) \
                {{active !disabled}}  $I(button-hover) \
            ] -border 3 -padding {{3 2}} -sticky news

        ttk::style element create Checkbutton.indicator image [list $I(checkbox-unchecked) \
                disabled            $I(checkbox-unchecked-disabled) \
                {{active selected}}   $I(checkbox-checked) \
                {{pressed selected}}  $I(checkbox-checked) \
                active              $I(checkbox-unchecked) \
                selected            $I(checkbox-checked) \
                {{disabled selected}} $I(checkbox-checked-disabled) \
            ] -width 22 -sticky w

        ttk::style element create Radiobutton.indicator image [list $I(radio-unchecked) \
                disabled            $I(radio-unchecked-disabled) \
                {{active selected}}   $I(radio-checked) \
                {{pressed selected}}  $I(radio-checked) \
                active              $I(radio-unchecked) \
                selected            $I(radio-checked) \
                {{disabled selected}} $I(radio-checked-disabled) \
            ] -width 22 -sticky w

        ttk::style element create Horizontal.Scrollbar.trough image $I(trough-scrollbar-horiz)
        ttk::style element create Horizontal.Scrollbar.thumb \
            image [list $I(slider-horiz-normal) \
                        {{pressed !disabled}} $I(slider-horiz-pressed) \
                        {{active !disabled}}  $I(slider-horiz-hover) \
                        disabled            $I(slider-horiz-disabled) \
            ] -border 6 -sticky ew

        ttk::style element create Vertical.Scrollbar.trough image $I(trough-scrollbar-vert)
        ttk::style element create Vertical.Scrollbar.thumb \
            image [list $I(slider-vert-normal) \
                        {{pressed !disabled}} $I(slider-vert-pressed) \
                        {{active !disabled}}  $I(slider-vert-hover) \
                        disabled            $I(slider-vert-disabled) \
            ] -border 6 -sticky ns

        ttk::style element create Horizontal.Scale.trough \
            image [list $I(trough-horiz-scale-active) disabled $I(trough-horiz-scale-disabled)] \
            -border {{8 5 8 5}} -padding 0
        ttk::style element create Horizontal.Scale.slider \
            image [list $I(scale-slider-normal) disabled $I(scale-slider-disabled) active $I(scale-slider-active)] \
            -sticky {{}}

        ttk::style element create Vertical.Scale.trough \
            image [list $I(trough-vert-scale-active) disabled $I(trough-vert-scale-disabled)] \
            -border {{5 8 5 8}} -padding 0
        ttk::style element create Vertical.Scale.slider \
            image [list $I(scale-slider-normal) disabled $I(scale-slider-disabled) active $I(scale-slider-active)] \
            -sticky {{}}

        ttk::style element create Entry.field \
            image [list $I(entry-normal) \
                        focus $I(entry-focus) \
                        disabled $I(entry-disabled)] \
            -border 3 -padding {{6 4}} -sticky news

        ttk::style element create Labelframe.border image $I(labelframe) \
            -border 4 -padding 4 -sticky news

        ttk::style element create Menubutton.button \
            image [list $I(Menubutton-normal) \
                        pressed  $I(Menubutton-pressed) \
                        active   $I(Menubutton-hover) \
                        disabled $I(Menubutton-disabled) \
            ] -sticky news -border 3 -padding {{3 2}}
        ttk::style element create Menubutton.indicator \
            image [list $I(arrow-down-normal) \
                        active   $I(arrow-down-active) \
                        pressed  $I(arrow-down-active) \
                        disabled $I(arrow-down-disabled) \
            ] -sticky e -width 20

        ttk::style element create Combobox.field \
            image [list $I(combo-normal-entry) \
                {{readonly disabled}}  $I(readonly-combo-disabled) \
                {{readonly pressed}}   $I(readonly-combo-pressed) \
                {{readonly focus}}     $I(readonly-combo-focus) \
                {{readonly hover}}     $I(readonly-combo-hover) \
                readonly             $I(readonly-combo-normal) \
                {{disabled}} $I(combo-disabled-entry) \
                {{focus}}    $I(combo-focus-entry) \
                {{hover}}    $I(combo-normal-entry) \
            ] -border 4 -padding {{6 0 0 0}}

        ttk::style element create Combobox.downarrow \
            image [list $I(combo-normal-button) \
                        pressed   $I(combo-pressed-button) \
                        active    $I(combo-hover-button) \
                        disabled  $I(combo-disabled-button) \
          ] -border 4 -padding {{0 10 6 10}}

        ttk::style element create Combobox.arrow \
            image [list $I(arrow-down-normal) \
                        active    $I(arrow-down-active) \
                        pressed   $I(arrow-down-active) \
                        disabled  $I(arrow-down-disabled) \
          ]  -sticky e -width 15

        ttk::style element create Spinbox.field \
            image [list $I(spinbox-normal-entry) focus $I(spinbox-focus-entry)] \
            -border 4 -padding {{6 0 0 0}} -sticky news

        ttk::style element create Spinbox.uparrow \
            image [list $I(spinbox-uparrow-btn-normal) \
                        pressed   $I(spinbox-uparrow-btn-pressed) \
                        active    $I(spinbox-uparrow-btn-hover) \
                        disabled  $I(spinbox-uparrow-btn-disable) \
            ] -width 20 -border {{0 2 3 0}} -padding {{0 5 6 2}}

        ttk::style element create Spinbox.symuparrow \
            image [list $I(spinbox-small-uparrow) \
                        active    $I(spinbox-small-uparrow-active) \
                        pressed   $I(spinbox-small-uparrow-active) \
                        disabled  $I(spinbox-small-uparrow-disabled) \
            ]
        ttk::style element create Spinbox.downarrow \
            image [list $I(spinbox-down-btn-normal) \
                        pressed   $I(spinbox-down-btn-pressed) \
                        active    $I(spinbox-down-btn-hover) \
                        disabled  $I(spinbox-down-btn-disable) \
            ] -width 20 -border {{0 0 3 2}} -padding {{0 2 6 5}}

        ttk::style element create Spinbox.symdownarrow \
            image [list $I(spinbox-small-down) \
                        active    $I(spinbox-small-down-pressed) \
                        pressed   $I(spinbox-small-down-pressed) \
                        disabled  $I(spinbox-small-down-disabled) \
          ]

        ttk::style element create Notebook.client \
            image $I(notebook-client) -border 1
        ttk::style element create Notebook.tab \
            image [list $I(notebook-tab-top) \
                        selected    $I(notebook-tab-selected) \
                        active      $I(notebook-tab-hover) \
            ] -padding {{0 2 0 0}} -border 2

        ttk::style element create Horizontal.Progressbar.trough \
            image $I(progressbar-trough-hori) -border {{5 1 5 1}} -padding 1
        ttk::style element create Horizontal.Progressbar.pbar \
            image $I(progressbar-pbar-hori) -border {{4 0 4 0}}

        ttk::style element create Vertical.Progressbar.trough \
            image $I(progressbar-trough-vert) -border {{1 5 1 5}} -padding 1
        ttk::style element create Vertical.Progressbar.pbar \
            image $I(progressbar-pbar-vert) -border {{0 4 0 4}}

        ttk::style element create Treeview.field \
            image $I(treeview-not-selected) -border 1
        ttk::style element create Treeheading.cell \
            image [list $I(treeview-selected) pressed $I(treeview-selected)] \
            -border 1 -padding 4 -sticky ewns

        ttk::style element create Treeitem.indicator \
            image [list $I(treeitem-plus) user2 $I(treeitem-empty) user1 $I(treeitem-minus)] \
            -width 15 -sticky w

        #ttk::style element create Separator.separator image $I()

        #
        # Settings:
        #

        ttk::style configure TButton -padding {{8 4 8 4}} -width -10 -anchor center
        ttk::style configure TMenubutton -padding {{8 4 4 4}}
        ttk::style configure Toolbutton -anchor center
        ttk::style map TCheckbutton -background [list active $colors(-checklight)]
        ttk::style configure TCheckbutton -padding 3
        ttk::style map TRadiobutton -background [list active $colors(-checklight)]
        ttk::style configure TRadiobutton -padding 3
        ttk::style configure TNotebook -tabmargins {{0 2 0 0}}
        ttk::style configure TNotebook.Tab -padding {{6 2 6 2}} -expand {{0 0 2}}
        ttk::style map TNotebook.Tab -expand [list selected {{1 2 4 2}}]
        ttk::style configure TSeparator -background $colors(-bg)
        ttk::style configure TCombobox -selectbackground $colors(-cboxbg)
        #ttk::style configure TCombobox -selectbackground [list active $colors(-cboxbg_active)]
        ttk::style configure TCombobox -selectforeground $colors(-fg)



        # Treeview
        ttk::style configure Treeview -background $colors(-window)
        ttk::style configure Treeview.Item -padding {{2 0 0 0}}
        ttk::style map Treeview \
            -background [list selected $colors(-selectbg)] \
            -foreground [list selected $colors(-selectfg)]
    }}
}}

variable version 0.1
package provide ttk::theme::{themeTemplate} $version


