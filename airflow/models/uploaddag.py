# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import json
from builtins import bytes
from urllib.parse import urlparse, unquote, parse_qsl

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import synonym

from airflow import LoggingMixin
from airflow.exceptions import AirflowException
from airflow.models.base import Base, ID_LEN
from airflow.models.crypto import get_fernet


class Uploaddag(Base, LoggingMixin):
    
    def parse_from_uri(self, uri):
        pass

    def get_password(self):
        pass

    def set_password(self, value):
        pass

    @declared_attr
    def password(cls):
        pass

    def get_extra(self):
        pass

    def set_extra(self, value):
        pass

    @declared_attr
    def extra(cls):
        pass

    def rotate_fernet_key(self):
        pass

    def get_hook(self):
        pass

    def __repr__(self):
        pass

    def debug_info(self):
        pass

    @property
    def extra_dejson(self):
        pass
