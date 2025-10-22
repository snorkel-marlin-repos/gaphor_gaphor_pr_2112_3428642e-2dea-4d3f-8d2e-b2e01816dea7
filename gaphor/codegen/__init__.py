import os

import gi

if os.getenv("GAPHOR_USE_GTK") != "NONE":
    # Allow to explicitly *not* initialize GTK (for docs, mainly)
    gtk_version = "3.0" if os.getenv("GAPHOR_USE_GTK") == "3" else "4.0"

    gi.require_version("Gtk", gtk_version)
    gi.require_version("Gdk", gtk_version)
