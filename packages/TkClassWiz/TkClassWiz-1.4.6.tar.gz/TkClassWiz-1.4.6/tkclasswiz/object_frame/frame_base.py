from typing import get_args, get_origin, Iterable, Union, Literal, Any, TYPE_CHECKING, TypeVar
from abc import ABC, abstractmethod
from contextlib import suppress
from functools import cache

from ..convert import *
from ..aliasing import *
from ..dpi import *
from ..utilities import *
from ..storage import *
from ..messagebox import Messagebox
from ..extensions import extendable
from ..doc import doc_category

import tkinter.ttk as ttk
import tkinter as tk
import json


if TYPE_CHECKING:
    from .window import ObjectEditWindow


T = TypeVar('T')


__all__ = (
    "NewObjectFrameBase",
)


@extendable
@doc_category("Object frames")
class NewObjectFrameBase(ttk.Frame, ABC):
    """
    Base Frame for inside the :class:`ObjectEditWindow` that allows object definition.

    Parameters
    -------------
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
    origin_window: "ObjectEditWindow" = None

    def __init__(
        self,
        class_: Any,
        return_widget: Union[ComboBoxObjects, ListBoxObjects, None],
        parent = None,
        old_data: Any = None,
        check_parameters: bool = True,
        allow_save = True,
    ):
        self.class_ = class_
        "The type (class) of object being creating"

        self.return_widget = return_widget
        "The widget where the abstract object (ObjectInfo) will be stored"

        self._original_gui_data = None
        self.parent = parent
        self.check_parameters = check_parameters  # At save time
        "Check for parameters on save"

        self.allow_save = allow_save  # Allow save or not allow (eg. viewing SQL data)
        "Saving is allowed"

        self.old_gui_data = old_data  # Set in .load
        "If editing, the value being edited"

        # If return_widget is None, it's a floating display with no return value
        editing_index = return_widget.current() if return_widget is not None else -1
        if editing_index == -1:
            editing_index = None

        self.editing_index = editing_index
        "The index of object being edited"

        super().__init__(master=parent)
        self.init_toolbar_frame(class_)
        self.init_main_frame()

    @staticmethod
    @cache
    def get_cls_name(cls: Any, args: bool = False) -> str:
        """
        Returns the name of the class ``cls`` or
        the original class when the name cannot be obtained.
        If alias exists, alias is returned instead.
        """
        normal_cls = get_origin(cls) or cls
        if (alias := get_aliased_name(normal_cls)) is not None:
            return alias + f" ({name})"
        elif hasattr(normal_cls, "__name__"):
            name = normal_cls.__name__
        elif hasattr(normal_cls, "_name") and normal_cls._name:
            name = normal_cls._name
        else:
            name = str(normal_cls)

        if args and (type_args := get_args(cls)):
            name = (
                name + 
                f"[{ ', '.join([NewObjectFrameBase.get_cls_name(x, True) for x in type_args]) }]"
            )
        
        return name

    @classmethod
    def set_origin_window(cls, window: "ObjectEditWindow"):
        cls.origin_window = window

    @classmethod
    def filter_literals(cls, types_: Iterable):
        "Returns only the literal types from ``types_``"
        return [x for x in types_ if get_origin(x) is Literal]

    @classmethod
    def check_literals(cls, value: str, literal_types: Iterable):
        """
        Checks if the ``value`` is a correct iterable.
        
        Parameters
        -------------
        value: str
            The string value to be checked.
        types: Iterable[Literal]
            An iterable of accepted literals.
        """
        allowed_values = []
        for literal_type in literal_types:
            args = get_args(literal_type)
            if value in args:
                return value

            allowed_values.extend(args)

        raise ValueError(
            f"'{value}' (a string) is not one of accepted types and does not match any literal values.\n"
            f"'Allowed literals: {allowed_values}."
        )

    @classmethod
    def cast_type(cls, value: Any, types: Iterable):
        """
        Tries to convert *value* into one of the types inside *types* (first successful).

        Raises
        ----------
        TypeError
            Could not convert into any type.
        """

        CAST_FUNTIONS = {
            dict: lambda v: convert_to_object_info(json.loads(v))
        }

        for type_ in filter(lambda t: t.__module__ == "builtins", types):
            with suppress(Exception):
                cast_funct = CAST_FUNTIONS.get(type_)
                if cast_funct is None:
                    value = type_(value)
                else:
                    value = cast_funct(value)
                break
        else:
            raise TypeError(f"Could not convert '{value}' to any of accepted types.\nAccepted types: '{types}'")

        return value

    def init_main_frame(self):
        frame_main = ttk.Frame(self)
        frame_main.pack(expand=True, fill=tk.BOTH)
        self.frame_main = frame_main

    def init_toolbar_frame(self, class_):
        frame_toolbar = ttk.Frame(self)
        frame_toolbar.pack(fill=tk.X)
        self.frame_toolbar = frame_toolbar

    @property
    def modified(self) -> bool:
        """
        Returns True if the GUI values have been modified.
        """
        current_values = self.get_gui_data()
        return current_values != self._original_gui_data

    def update_window_title(self):
        "Set's the window title according to edit context."
        self.origin_window.title(f"{'New' if self.old_gui_data is None else 'Edit'} {self.get_cls_name(self.class_, True)} object")

    def close_frame(self):
        if self.allow_save and self.modified:
            resp = Messagebox.yesnocancel("Save?", "Do you wish to save?", master=self.origin_window)
            if resp is not None:
                if resp:
                    self.save()
                else:
                    self._cleanup()
        else:
            self._cleanup()

    def new_object_frame(
        self,
        class_,
        widget,
        *args,
        **kwargs
    ):
        """
        Opens up a new object frame on top of the current one.
        Parameters are the same as in :class:`NewObjectFrame` (current class).
        """
        allow_save = kwargs.pop("allow_save", self.allow_save)
        return self.origin_window.open_object_edit_frame(
            class_, widget, allow_save=allow_save, *args, **kwargs
        )

    @abstractmethod
    def to_object(self):
        """
        Creates an object from the GUI data.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self, old_data: Any):
        """
        Loads the old object info data into the GUI.

        Parameters
        -------------
        old_data: Any
            The old gui data to load.
        """
        raise NotImplementedError

    def save(self):
        """
        Save the current object into the return widget and then close this frame.
        """
        try:
            if not self.allow_save or self.return_widget is None:
                raise TypeError("Saving is not allowed in this context!")

            object_ = self.to_object()
            self._update_ret_widget(object_)
            self._cleanup()
        except Exception as exc:
            Messagebox.show_error(
                "Saving error",
                f"Could not save the object.\n{exc}",
                parent=self.origin_window
            )

    def remember_gui_data(self):
        """
        Remembers GUI data for change checking.
        """
        self._original_gui_data = self.get_gui_data()

    @abstractmethod
    def get_gui_data(self) -> Any:
        """
        Returns all GUI values.
        """
        raise NotImplementedError

    def _cleanup(self):
        self.origin_window.clean_object_edit_frame()

    def _update_ret_widget(self, new: Any):
        ind = self.return_widget.count()
        if self.old_gui_data is not None:
            ret_widget = self.return_widget
            if self.editing_index is not None:  # The index of edited item inside return widget
                ind = self.editing_index
                ret_widget.delete(ind)

        self.return_widget.insert(ind, new)
        if isinstance(self.return_widget, ComboBoxObjects):
            self.return_widget.current(ind)
        else:
            self.return_widget.selection_set(ind)
