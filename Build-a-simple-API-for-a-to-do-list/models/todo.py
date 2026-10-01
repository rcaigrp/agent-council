#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Todo:
    def __init__(self, id, title, description="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    def __repr__(self):
        return f'<Todo {self.title}>'