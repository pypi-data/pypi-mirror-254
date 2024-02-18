#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.01.29 18:00:00                  #
# ================================================== #

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QLineEdit, QStyle

from pygpt_net.utils import trans
import pygpt_net.icons_rc


class CtxSearchInput(QLineEdit):
    def __init__(self, window=None):
        """
        Search input

        :param window: Window instance
        """
        super(CtxSearchInput, self).__init__(window)
        self.window = window
        self.setPlaceholderText(trans('ctx.list.search.placeholder'))

        self.clear_action = QAction(self)
        self.clear_action.setIcon(QIcon(":/icons/close.svg"))
        self.clear_action.triggered.connect(self.clear_search_string)
        self.addAction(self.clear_action, QLineEdit.TrailingPosition)

    def clear_search_string(self):
        """Clear input"""
        self.window.controller.ctx.search_string_clear()

    def keyPressEvent(self, event):
        """
        Key press event

        :param event: key event
        """
        super(CtxSearchInput, self).keyPressEvent(event)
        self.window.controller.ctx.search_string_change(self.text())


