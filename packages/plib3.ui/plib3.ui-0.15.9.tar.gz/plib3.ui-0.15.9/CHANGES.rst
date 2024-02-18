plib3.ui Change Log
===================

Version 0.15.9
==============

- Add ``HtmlDisplay`` widget to enable display of HTML.

- Add pre-built input dialogs for ``str``, and ``int`` values;
  add methods to return ``bool`` from Ok/Cancel and Yes/No
  query dialogs, and ``bool`` or ``None`` from Yes/No/Cancel
  dialog. Update example programs to use new dialog functions.

- Add ``font`` parameter to all specs for widgets that display
  text.

- Add convenience methods for font specs in the ``plib.ui.common``
  module.

- Add ``prompt`` parameter to ``StringSelectDialog`` to allow
  displaying a prompt above the selection list box. Also add a
  ``font`` parameter to this dialog.

Version 0.15.8.3
----------------

- Rework signal handling bug fix to preserve correct MRO for
  edit widget classes.

Version 0.15.8.2
----------------

- Fix bug in signal handling for ``PNumEditBox`` in wx toolkit.

Version 0.15.8.1
----------------

- Added note in ``README`` explaining why example programs are
  installed as console scripts instead of GUI scripts.

- Updated TODO to remove items implemented in version 0.15.8.

Version 0.15.8
--------------

- Add ``PScroller`` and ``PScrollingWrapper`` widgets to
  enable adding scrolling capability to any widget. ``PScroller``
  is intended for custom widgets or widgets created dynamically
  by the application; ``PScrollingWrapper`` is intended for
  use in widget specs (the ``scrolling`` spec is added to the
  ``plib.ui.widgets`` module for this purpose). The ``ui-signals3``
  example program now includes a tab with a scrolling list box
  to illustrate usage.

- Add grid layout option to ``PPanel``. Either the number of
  columns or the number of rows can be specified. The
  ``ui-signals3`` example program now includes button and
  radio groups using the grid layout options.

Version 0.15.7.4
----------------

- Bug fix in handling of file filter translation for
  file open/save dialogs.

Version 0.15.7.3
----------------

- Enable PEP 562 version of ``plib.ui.app`` import
  mechanism in Python 3.7 since that PEP is implemented
  in that version.

Version 0.15.7.2
----------------

- Bug fix in ``plib.ui.app`` import mechanism so that
  it works in Python 3.7 and earlier, when PEP 562
  functionality is not available.

Version 0.15.7.1
----------------

- Make default layout of panels (vertical) consistent
  across all toolkits.

- Change ``PANEL_NONE`` style constant to ``PANEL_PLAIN``
  to better describe what it does.

- Bug fix in ``PImageView`` widget for wx toolkit.

Version 0.15.7
--------------

- Add mixin classes to support expanded signals
  for widgets. This also eliminates the need for
  toolkit-specific code in the ``ui-signals3`` example
  program that uses the custom signal API. Currently
  the expanded signals supported are focus in/out
  (the edit control widgets have this enabled by
  default, but the ``PFocusMixin`` class allows this
  to be used with any widget) and mouse down, up,
  and double click for the left, right, and middle
  mouse buttons. (Note that this allows "mouse click"
  functionality, similar to what is already built in
  to buttons, to be enabled for any widget; the
  custom widgets in the ``ui-signals3`` example
  program do this.) Support for other expanded signals
  may be added in future releases.

- Add the ability to import any of the standard
  objects from the ``plib.ui.app`` module instead of
  having to use the ``get_toolkit_object`` function.

Version 0.15.6.1
----------------

- Add an index to the handler parameters for one of the
  custom signals in the ``ui-signals3`` example program.

- Fix custom widgets in ``ui-signals3`` example program
  to only respond to left mouse clicks in pyside2 and
  qt5 (this was already correct for wx).

Version 0.15.6
--------------

- Add API for adding custom signals, actions, and
  widgets. The ``ui-signals3`` example program has been
  updated to demonstrate the API. Note that some aspects
  still require toolkit-specific code, as shown in the
  example program.

- Add support for custom widgets in module ``__main__``
  as well as modules with a dot in the name.

- Fix handling of dialog results in wx.

Version 0.15.5.4
----------------

- Bug fix in the ``PImageView`` widget on PySide 2.

Version 0.15.5.3
----------------

- Bug fix in the wx toolkit to ensure that button
  selected signal is fired when a button group button
  is checked in code.

Version 0.15.5.2
----------------

- Bug fixes in the wx toolkit for button group layout,
  list box layout, and event handling.

Version 0.15.5.1
----------------

- Bug fix for application initialization.

Version 0.15.5
--------------

- Add support for "widget managers" other than the
  application object. Widget managers are objects that,
  like the application object, will have a ``main_widget``
  attribute that gives a spec for a main widget, and will
  provide event handlers for all desired events for that
  main widget and all of its sub-widgets. A widget
  manager class (i.e., a subclass of ``PWidgetManager``)
  can itself appear as a widget spec; the widget
  auto-construction machinery will instantiate the class
  and will assign that instance as the manager of the
  main widget it constructs from the ``main_widget``
  attribute of the class, and all of its sub-widgets.
  Widget managers can be nested to any desired level;
  the objective is to make it easy to package a set of
  widgets and the code that handles them and their events
  in whatever way works best for the specific use case,
  instead of having to have them all on the application.
  The ``ui-signals3`` example program uses a widget
  manager for one of its pages, to show how the basic
  machinery works, and gives console output that shows
  how widgets and managers are set up.

- The application object and all widget managers have
  defined ``after_create`` and ``populate_data`` methods
  that can be used to construct objects as needed and to
  populate widgets with data (the latter is most commonly
  used with dialogs but can be used anywhere). These
  methods automatically get called during initialization
  of the application; the application and any widget managers
  first call the methods on all of their sub-managers before
  doing their own setup. The ``ui-signals3`` example program
  gives console output that shows the initialization order.

- Add ``PButtonGroup`` and ``PRadioGroup`` widgets to
  support groups of exclusive toggle or radio buttons.

- Add ``PPageWidget`` to display one of a series of pages,
  with an option to link selection of the pages to another
  widget. Update the ``ui-signals3`` example program to
  add options for using a page widget with various selector
  widgets instead of a tab widget.

- Add ``plib.ui.coll`` module for common base classes for
  widgets that look like standard Python collections (for
  example, the ``BaseStringListWidget`` class is a common
  base class for widgets that look like lists of strings
  (currently these are ``PComboBox``, ``PListBox``,
  ``PButtonGroup``, and ``PRadioGroup``).

- Add ``caption`` property to ``PButton`` and ``PCheckBox``.

- Add ``remove_widget`` method to ``PPanel``.

- Change ``SIGNAL_LISTBOXSELECTED`` to provide index instead
  of item string, to be similar to combo box signal.

- Add ``setup_signals`` method for widgets, to allow automatic
  linking of widgets (for example, a page widget can automatically
  link to the selected signal of another widget to change pages,
  based on the ``link_to`` parameter in the constructor).

- Wrapper box/panel and label widgets now get assigned known
  names in the ``labeled`` and ``labelbox`` widget specs.

- The ``ui-signals3`` example program now includes a demonstration
  of how to construct a user interface dynamically based on
  information at run time.

- ``PDialog`` now requires a client spec in its constructor.

Version 0.15.4
--------------

- Add support for widgets from user-defined modules: in
  widget specs, any module with a dot "." in its name is
  treated as user-defined and looked up by its name directly
  instead of the module name being taken from the toolkit
  sub-package in use.

Version 0.15.3
--------------

- Change signature of ``truncate`` method of ``PTextOutput``
  to have ``size`` default to ``0``. Update ``pyidserver-ui``
  example program to use new default signature.

- Move sentinel object for signaling untitled file to
  ``PTextFile`` base class so it is commonly available.

Version 0.15.2
--------------

- Size dialogs to their controls immediately before display
  to ensure correct sizing (since control sizes may change
  when the dialog is populated with data).

Version 0.15.1
--------------

- Add ``dialogs`` module with base ``DialogRunner`` class
  and some standard dialogs. Update the preferences manager
  in the ``prefs`` module to inherit from ``DialogRunner``.

- Add support for naming container widgets (group box, panel,
  label box) and padding instead of using automatic names
  computed by number.

Version 0.15
------------

- Switch to ``setuputils_build`` PEP 517 build backend.

Version 0.14.2
--------------

- Add ``example`` module that uses the auto-construction facility
  for entry points from ``plib3.stdlib.postinstall`` for the
  example programs shipped with ``plib3.ui``. Remove the
  ``scripts`` source directory since the wrapper scripts for the
  example programs are now auto-constructed as entry points.

Version 0.14.1
--------------

- Fix importing of wrapped example modules from ``plib.stdlib``
  in ``pyidserver-ui3`` and ``scrips-edit3`` example programs.

Version 0.14
------------

- Add ``PImageView`` image view widget.

- Moved basic file open/save functionality into separate
  ``PFileAware`` class.

- Add support for multiple file filters in file open/save dialogs.

- Set parent widget correctly in application file dialogs.

- Add support for passing file names to open on command line
  of notepad and XML viewer example programs.

Version 0.13
------------

- Make ``plib`` an implicit namespace package per PEP 420.

- Update to PEP 517 build compatibility using ``setuputils``
  version 2.0 to build setup.cfg.

Version 0.12.1
--------------

- Update bug fix to correctly handle older PySide2 versions.

Version 0.12
------------

- Fix bug created by Qt5/PySide2 changing ``QSocketNotifier`` to pass
  a ``QSocketDescriptor`` object to notification handlers (instead of
  an ``int`` representing the socket's ``fileno``).

Version 0.11
------------

- Initial release, version numbering continued from ``plib3.gui``.
