from typing import get_args, get_origin, Any, List, Literal
from inspect import isclass, isfunction
from functools import partial
from enum import Enum

from ..doc import doc_category
from ..deprecation import *
from ..utilities import *
from ..convert import *
from ..dpi import *

from ..messagebox import Messagebox
from ..extensions import extendable
from .tooltip import ListboxTooltip
from .frame_base import *
from ..storage import *

import tkinter as tk
import tkinter.ttk as ttk


__all__ = (
    "NewObjectFrameIterable",
    "NewObjectFrameIterableView",
)


@extendable
@doc_category("Object frames")
class NewObjectFrameIterable(NewObjectFrameBase):
    """
    Frame for use inside the ObjectEditWindow that allows definition of lists / iterables.
    The list annotations should be annotated similarly to the following example: ``list[Union[int, float]]`` 
    or ``Iterable[Union[int, float]]`` or ``Iterable[SomeClass]``


    Parameters
    ------------
    class_: Any
        The class we are defining for.
    return_widget: Any
        The widget to insert the ObjectInfo into after saving.
    parent: TopLevel
        The parent window.
    old_data: Any
        The old_data gui data.
    check_parameters: bool
        Check parameters (by creating the real object) upon saving.
        This is ignored if editing a function instead of a class.
    allow_save: bool
        If False, will open in read-only mode.
    """
    def __new__(cls, *args, **kwargs):
        if kwargs.get("allow_save", True):
            obj = super().__new__(NewObjectFrameIterable)
        else:
            obj = super().__new__(NewObjectFrameIterableView)

        return obj

    def __init__(
        self,
        class_: Any,
        return_widget: Any,
        parent=None,
        old_data: list = None,
        check_parameters: bool = True,
        allow_save = True
    ):
        dpi_5 = dpi_scaled(5)
        super().__init__(class_, return_widget, parent, old_data, check_parameters, allow_save)
        self.storage_widget = w = ListBoxScrolled(self.frame_main, height=20)
        ListboxTooltip(self.storage_widget, 0)

        frame_edit_remove = ttk.Frame(self.frame_main, padding=(dpi_5, 0))
        frame_edit_remove.pack(side="right")
        frame_cp = ttk.Frame(frame_edit_remove)
        frame_cp.pack(fill=tk.X, expand=True, pady=dpi_5)

        ttk.Button(frame_cp, text="Copy", command=w.save_to_clipboard).pack(side="left", fill=tk.X, expand=True)
        ttk.Button(frame_cp, text="Paste", command=w.paste_from_clipboard).pack(side="left", fill=tk.X, expand=True)
        menubtn = ttk.Menubutton(frame_edit_remove, text="Insert item")
        menu = tk.Menu(menubtn)
        menubtn.configure(menu=menu)
        menubtn.pack(fill=tk.X)
        ttk.Button(frame_edit_remove, text="Remove", command=w.delete_selected).pack(fill=tk.X)
        ttk.Button(frame_edit_remove, text="Edit", command=lambda: self._edit_selected()).pack(fill=tk.X)

        frame_up_down = ttk.Frame(frame_edit_remove)
        frame_up_down.pack(fill=tk.X, expand=True, pady=dpi_5)
        ttk.Button(frame_up_down, text="Up", command=lambda: w.move_selection(-1)).pack(side="left", fill=tk.X, expand=True)
        ttk.Button(frame_up_down, text="Down", command=lambda: w.move_selection(1)).pack(side="left", fill=tk.X, expand=True)

        self._list_args = get_args(self.class_)
        args_normal = []
        args_depr = []
        for arg in self._list_args:
            if is_deprecated(arg):
                args_depr.append(arg)
            else:
                args_normal.append(arg)

        self._create_add_menu(args_normal, menu)
        if args_depr:
            menu_depr = tk.Menu()
            self._create_add_menu(args_depr, menu_depr)
            menu.add_cascade(label=">Deprecated", menu=menu_depr)

        w.pack(side="left", fill=tk.BOTH, expand=True)

        if old_data is not None:
            self.load(old_data)

        self.remember_gui_data()

    def _create_add_menu(self, args: list, menu: tk.Menu):
        insert_items = []
        widget = self.storage_widget
        for arg in args:
            if arg is None:
                insert_items.append(...)
                insert_items.append(None)
            elif issubclass_noexcept(arg, Enum):
                insert_items.append(...)
                insert_items.extend(list(arg))
            elif get_origin(arg) is Literal:
                insert_items.append(...)
                insert_items.extend(get_args(arg))
            else:
                menu.add_command(
                    label=f"New {self.get_cls_name(arg, True)}",
                    command=partial(self.new_object_frame, arg, widget)
                )

        if insert_items:
            menu_insert = tk.Menu(menu)
            for item in insert_items:
                if item is Ellipsis:
                    menu_insert.add_separator()
                else:
                    label = f"'{item}'" if isinstance(item, str) else str(item)
                    menu_insert.add_command(label=label, command=partial(widget.insert, tk.END, item))

            menu.add_cascade(label=">Insert", menu=menu_insert)

    def load(self, old_data: List[Any]):
        self.storage_widget.insert(tk.END, *old_data)
        self.old_gui_data = old_data

    def get_gui_data(self) -> Any:
        return self.storage_widget.get()

    def to_object(self):
        data = self.get_gui_data()  # List items are not to be converted
        for d in data:
            if isinstance(d, str) and str not in self._list_args:
                self.check_literals(d, self.filter_literals(self._list_args))

        return get_origin(self.class_)(data)

    def _edit_selected(self):
        selection = self.storage_widget.curselection()
        if len(selection) == 1:
            object_ = self.storage_widget.get()[selection[0]]
            if isinstance(object_, ObjectInfo):
                self.new_object_frame(object_.class_, self.storage_widget, old_data=object_)
            else:
                self.new_object_frame(type(object_), self.storage_widget, old_data=object_)
        else:
            Messagebox.show_error("Selection error", "Select ONE item!", parent=self)


class NewObjectFrameIterableView(NewObjectFrameIterable):
    """
    Same as :class:`NewObjectFrameIterable`, but only allows viewing iterable objects.
    Also does not require annotations as supposed to the base class.
    """
    def __init__(self, class_: Any, return_widget: Any, parent=None, old_data: list = None, check_parameters: bool = True, allow_save=True):
        dpi_5 = dpi_scaled(5)
        super(NewObjectFrameBase, self).__init__(class_, return_widget, parent, old_data, check_parameters, allow_save)
        self.storage_widget = w = ListBoxScrolled(self.frame_main, height=20)
        ListboxTooltip(self.storage_widget, 0)

        frame_edit_remove = ttk.Frame(self.frame_main, padding=(dpi_5, 0))
        frame_edit_remove.pack(side="right")
        frame_cp = ttk.Frame(frame_edit_remove)
        frame_cp.pack(fill=tk.X, expand=True, pady=dpi_5)

        ttk.Button(frame_edit_remove, text="View", command=lambda: self._edit_selected()).pack(fill=tk.X)
        w.pack(side="left", fill=tk.BOTH, expand=True)

        if old_data is not None:
            self.load(old_data)

        self.remember_gui_data()
