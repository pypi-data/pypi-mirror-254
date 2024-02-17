#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.01.19 02:00:00                  #
# ================================================== #

from pygpt_net.core.dispatcher import Event


class Prompt:
    def __init__(self, window=None):
        """
        Prompt core

        :param window: Window instance
        """
        self.window = window

    def build_final_system_prompt(self, prompt: str) -> str:
        # tmp dispatch event: system prompt
        event = Event(Event.SYSTEM_PROMPT, {
            'mode': self.window.core.config.get('mode'),
            'value': prompt,
            'silent': True,
        })
        self.window.core.dispatcher.dispatch(event)
        prompt = event.data['value']

        if self.window.core.config.get('cmd'):
            # cmd prompt
            prompt += self.window.core.command.get_prompt()

            # cmd syntax tokens
            data = {
                'prompt': prompt,
                'silent': True,
                'syntax': [],
            }
            # tmp dispatch event: command syntax apply
            event = Event(Event.CMD_SYNTAX, data)
            self.window.core.dispatcher.dispatch(event)
            prompt = self.window.core.command.append_syntax(event.data)

        return prompt
