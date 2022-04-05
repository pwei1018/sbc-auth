# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests to assure the Status check service layer.

Test-Suite to ensure that the Status Service layer is working as expected.
"""
import pytest
from status_api.services.inapp_notificaitons import InAppNotifications as InAppNotificationsService

TEST_INAPP_DATA = [
    {'Id': '1',
     'Start Date': '2022-03-21 00:00',
     'End Date': '2022-04-27 00:00',
     'Type': 'Warning',
     'Applicaiton': 'ALL',
     'Message': 'PayBC outage',
     'development': 'TRUE',
     'test': 'FALSE',
     'sanbox': 'FALSE',
     'production': 'FALSE'},
    {'Id': '2',
     'Start Date':
     '2022-03-24 00:00',
     'End Date': '',
     'Type': 'Warning',
     'Applicaiton': 'Name Request',
     'Message': 'Name Request issue',
     'development': 'TRUE',
     'test': 'TRUE',
     'sanbox': 'FALSE',
     'production': 'FALSE'},
    {'Id': '3',
     'Start Date':
     '2022-03-20 15:00',
     'End Date': '2022-04-27 00:00',
     'Type': 'Error',
     'Applicaiton': 'ALL',
     'Message': 'System Error',
     'development': 'TRUE',
     'test': 'TRUE',
     'sanbox': 'FALSE',
     'production': 'TRUE'},
    {'Id': '4',
     'Start Date': '2022-03-20 15:00',
     'End Date': '2022-04-27 00:00',
     'Type': 'Info',
     'Applicaiton': 'ALL',
     'Message': 'Application Upgrade between 6:00pm to 7:00pm',
     'development': 'TRUE',
     'test': 'FALSE',
     'sanbox': 'FALSE',
     'production': 'FALSE'}
]


@pytest.mark.parametrize('id,startDate,endDate,type,application,message,development,test,sanbox,production',
                         TEST_INAPP_DATA)
def test_get_inapp_notificaitons(app, id, startDate, endDate, type, application, message, development, test, sanbox, production):
    """Assert that the function returns schedules."""
    with app.app_context():
        application_name = 'PPR'

        response = InAppNotificationsService.get_inapp_notificaitons(application_name=application_name)
        assert response is not None
