package require Tk 8.6

set base_theme_dir [file join [pwd] [file dirname [info script]]]

array set base_themes {
  aaa 0.1
  arc 0.1
  xttk 0.1
}

foreach {theme version} [array get base_themes] {
  package ifneeded ttk::theme::$theme $version \
    [list source [file join $base_theme_dir $theme $theme.tcl]]
}
