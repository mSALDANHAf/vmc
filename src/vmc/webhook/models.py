"""
 * Licensed to DSecure.me under one or more contributor
 * license agreements. See the NOTICE file distributed with
 * this work for additional information regarding copyright
 * ownership. DSecure.me licenses this file to you under
 * the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
"""
from django.db import models

from vmc.common.models import BaseModel


class TheHive4LogConverter(BaseModel):
    log_message = models.TextField()
    tag = models.CharField(max_length=128)


class TheHive4(BaseModel):
    SCHEMA = (
        ('http', 'http'),
        ('https', 'https')
    )
    name = models.CharField(max_length=128)
    schema = models.CharField(choices=SCHEMA, default='http', max_length=5)
    host = models.CharField(max_length=128)
    port = models.PositiveSmallIntegerField()
    token = models.CharField(max_length=256)
    insecure = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    vulnerability_status_converter = models.ManyToManyField(TheHive4LogConverter)

    def get_url(self) -> str:
        return F'{self.schema}://{self.host}:{self.port}'