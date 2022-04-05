# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests to assure the inapp notifications end-point."""


def test_inapp(client):
    """Assert that the endpoint returns 200 with actual result."""
    rv = client.get('/api/v1/inapp')
    assert rv.status_code == 200


def test_inapp_with_slash(client):
    """Assert that the endpoint returns 200 with actual result."""
    rv = client.get('/api/v1/inapp/')
    assert rv.status_code == 200


def test_inapp_with_application_name(client):
    """Assert that the endpoint returns 200 with actual result."""
    application_name = 'PPR'

    rv = client.get(f'/api/v1/inapp/{application_name}')
    assert rv.status_code == 200
