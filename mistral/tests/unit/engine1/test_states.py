# -*- coding: utf-8 -*-
#
# Copyright 2013 - Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from mistral.openstack.common import log as logging
from mistral.tests import base
from mistral.workflow import states as s

LOG = logging.getLogger(__name__)


class StatesModuleTest(base.BaseTest):
    def test_is_valid_transition(self):
        # From IDLE
        self.assertTrue(s.is_valid_transition(s.IDLE, s.IDLE))
        self.assertTrue(s.is_valid_transition(s.IDLE, s.RUNNING))
        self.assertTrue(s.is_valid_transition(s.IDLE, s.ERROR))
        self.assertFalse(s.is_valid_transition(s.IDLE, s.STOPPED))
        self.assertFalse(s.is_valid_transition(s.IDLE, s.DELAYED))
        self.assertFalse(s.is_valid_transition(s.IDLE, s.SUCCESS))

        # From RUNNING
        self.assertTrue(s.is_valid_transition(s.RUNNING, s.RUNNING))
        self.assertTrue(s.is_valid_transition(s.RUNNING, s.ERROR))
        self.assertTrue(s.is_valid_transition(s.RUNNING, s.STOPPED))
        self.assertTrue(s.is_valid_transition(s.RUNNING, s.DELAYED))
        self.assertTrue(s.is_valid_transition(s.RUNNING, s.SUCCESS))
        self.assertFalse(s.is_valid_transition(s.RUNNING, s.IDLE))

        # From STOPPED
        self.assertTrue(s.is_valid_transition(s.STOPPED, s.STOPPED))
        self.assertTrue(s.is_valid_transition(s.STOPPED, s.RUNNING))
        self.assertTrue(s.is_valid_transition(s.STOPPED, s.ERROR))
        self.assertFalse(s.is_valid_transition(s.STOPPED, s.DELAYED))
        self.assertFalse(s.is_valid_transition(s.STOPPED, s.SUCCESS))
        self.assertFalse(s.is_valid_transition(s.STOPPED, s.IDLE))

        # From DELAYED
        self.assertTrue(s.is_valid_transition(s.DELAYED, s.DELAYED))
        self.assertTrue(s.is_valid_transition(s.DELAYED, s.RUNNING))
        self.assertTrue(s.is_valid_transition(s.DELAYED, s.ERROR))
        self.assertFalse(s.is_valid_transition(s.DELAYED, s.STOPPED))
        self.assertFalse(s.is_valid_transition(s.DELAYED, s.SUCCESS))
        self.assertFalse(s.is_valid_transition(s.DELAYED, s.IDLE))

        # From SUCCESS
        self.assertTrue(s.is_valid_transition(s.SUCCESS, s.SUCCESS))
        self.assertFalse(s.is_valid_transition(s.SUCCESS, s.RUNNING))
        self.assertFalse(s.is_valid_transition(s.SUCCESS, s.ERROR))
        self.assertFalse(s.is_valid_transition(s.SUCCESS, s.STOPPED))
        self.assertFalse(s.is_valid_transition(s.SUCCESS, s.DELAYED))
        self.assertFalse(s.is_valid_transition(s.SUCCESS, s.IDLE))

        # From ERROR
        self.assertTrue(s.is_valid_transition(s.ERROR, s.ERROR))
        self.assertFalse(s.is_valid_transition(s.ERROR, s.RUNNING))
        self.assertFalse(s.is_valid_transition(s.ERROR, s.STOPPED))
        self.assertFalse(s.is_valid_transition(s.ERROR, s.DELAYED))
        self.assertFalse(s.is_valid_transition(s.ERROR, s.SUCCESS))
        self.assertFalse(s.is_valid_transition(s.ERROR, s.IDLE))
