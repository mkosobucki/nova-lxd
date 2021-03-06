# Copyright 2015 Canonical Ltd
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import collections
import os

from nova import conf


_InstanceAttributes = collections.namedtuple('InstanceAttributes', [
    'instance_dir', 'console_path', 'storage_path', 'container_path'])


def InstanceAttributes(instance):
    """An instance adapter for nova-lxd specific attributes."""
    instance_dir = os.path.join(conf.CONF.instances_path, instance.name)
    console_path = os.path.join('/var/log/lxd/', instance.name, 'console.log')
    storage_path = os.path.join(instance_dir, 'storage')
    container_path = os.path.join(
        conf.CONF.lxd.root_dir, 'containers', instance.name)
    return _InstanceAttributes(
        instance_dir, console_path, storage_path, container_path)
