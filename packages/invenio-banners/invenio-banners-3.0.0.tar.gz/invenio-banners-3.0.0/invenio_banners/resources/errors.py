# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 CERN.
#
# Invenio-Banners is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Errors."""

from flask_resources import HTTPJSONException, create_error_handler

from ..services.errors import BannerNotExistsError


class ErrorHandlersMixin:
    """Mixin to define error handlers."""

    error_handlers = {
        BannerNotExistsError: create_error_handler(
            lambda e: HTTPJSONException(
                code=404,
                description=e.description,
            )
        ),
    }
