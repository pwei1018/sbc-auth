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
"""Service to get in-app notifications."""
from enum import Enum

from flask import current_app

from status_api.services.cache import cache
from status_api.services.google_service import GoogleService
from status_api.utils.util import convert_datetime, get_today


class InAppNotifications:
    """Service to get in-app notifications."""

    class ApplicationName(str, Enum):
        """Application Name."""

        ALL = 'ALL'
        NAME_REQUEST = 'Name Request'
        DIRECTOR_SEARCH = 'Director Search'
        BUSINESS_HOME = 'BC Registry Home'
        BUSINESS_FILINGS = 'business-filings-ui'
        BUSINESS_EDIT = 'business-edit-ui'
        BUSINESS_CREATE = 'business-create-ui'
        BC_REGISTRY_HOME = 'BCROS Home'
        PPR = 'PPR'

    def __init__(self):
        """Return a Service object."""

    @classmethod
    @cache.cached(key_prefix='inapp_notificaitons')
    def get_inapp_notificaitons(cls, application_name: str):
        """Get notifications from Google Sheet by service name. The value will be cached for 5 minutes."""
        notifications = GoogleService(current_app.config.get('SYSTEM_BANNER_SHEET_NAME')).fetch_details()

        # remove empty rows
        notifications = list(filter(lambda x:
                                    (x.get('Id') != '' and x.get('Applicaiton') != '' and x.get('Message') != ''),
                                    notifications))

        # filter by date
        notifications = list(filter(lambda x:
                                    (x.get('Start Date') == '' or convert_datetime(x.get('Start Date')) <= get_today()),
                                    notifications))

        notifications = list(filter(lambda x:
                                    (x.get('End Date') == '' or convert_datetime(x.get('End Date')) >= get_today()),
                                    notifications))

        # filter by application name
        app_name = InAppNotifications.ApplicationName[application_name].value
        if app_name != 'ALL':
            notifications = list(filter(lambda x:
                                        (x.get('Applicaiton') == 'ALL' or x.get('Applicaiton') == app_name),
                                        notifications))
        else:
            notifications = list(filter(lambda x:
                                        x.get('Applicaiton') == 'ALL',
                                        notifications))

        # filter by environment
        notifications = list(filter(lambda x: x.get(current_app.config.get('ENVIRONMENT')) == 'TRUE', notifications))

        notifications_out = []
        for notification in notifications:
            notifications_out.append({'id': notification['Id'],
                                      'type': notification['Type'].lower(),
                                      'message': notification['Message']})

        return {'messages': notifications_out}

    @classmethod
    @cache.cached(key_prefix='whatnews')
    def get_whatsnew(cls, application_name: str):
        """Get news from Google Sheet by service name. The value will be cached for 5 minutes."""
        news = GoogleService(current_app.config.get('WHATS_NEW_SHEET_NAME')).fetch_details()

        # remove empty rows
        news = list(filter(lambda x:
                           (x.get('Id') != '' and x.get('Applicaiton') != ''
                               and x.get('Title') != '' and x.get('News') != ''),
                           news))

        # filter by date
        news = list(filter(lambda x:
                           (x.get('Start Date') == '' or convert_datetime(x.get('Start Date')) <= get_today()),
                           news))

        news = list(filter(lambda x:
                           (x.get('End Date') == '' or convert_datetime(x.get('End Date')) >= get_today()),
                           news))

        # filter by application name
        app_name = InAppNotifications.ApplicationName[application_name].value
        if app_name != 'ALL':
            news = list(filter(lambda x:
                               (x.get('Applicaiton') == 'ALL' or x.get('Applicaiton') == app_name),
                               news))
        else:
            news = list(filter(lambda x:
                               x.get('Applicaiton') == 'ALL',
                               news))

        # filter by environment
        news = list(filter(lambda x: x.get(current_app.config.get('ENVIRONMENT')) == 'TRUE', news))

        news_out = []
        for notification in news:
            news_out.append({'id': notification['Id'],
                             'priority': notification['Priority'],
                             'label': notification['Label'],
                             'date': notification['Date'],
                             'title': notification['Title'],
                             'message': notification['News'],
                             'more': notification['More']})

        return {'messages': news_out}
