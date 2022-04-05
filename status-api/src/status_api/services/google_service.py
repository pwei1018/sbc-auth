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
"""Google Service."""
import json

import gspread
import pandas as pd
from flask import current_app
from oauth2client.service_account import ServiceAccountCredentials


class Google(type):
    """Singleton meta."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call for meta."""
        if cls not in cls._instances:
            cls._instances[cls] = super(Google, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GoogleService(metaclass=Google):  # pylint: disable=too-few-public-methods
    """Singleton wrapper for Google Service."""

    __google_client = None
    __google_sheet_name = None

    def get_google_client(self):
        """Retrieve singleton Google client."""
        return self.__google_client

    def fetch_details(self):
        """Fetch content from Google sheet."""
        client = self.get_google_client()
        spreadsheet_key = current_app.config.get('GOOGLE_SPREADSHEET_KEY')
        workbook = client.open_by_key(spreadsheet_key)
        worksheet = workbook.worksheet(self.__google_sheet_name)
        values = worksheet.get_all_values()
        news_dataframe = pd.DataFrame(values[1:], columns=values[0])

        news = json.loads(news_dataframe.to_json(orient='records'))

        print(news)

        return news

    def __init__(self, sheet_name: str):
        """Private constructor."""
        scope = ['https://www.googleapis.com/auth/drive.readonly']
        sa_creds = current_app.config.get('GOOGLE_CREDS')
        sa_creds = json.loads(sa_creds)
        # In the private key, 1-char newline got replaced with 2-char '\n'
        sa_creds['private_key'] = sa_creds['private_key'].replace('\\n', '\n')
        credential = ServiceAccountCredentials.from_json_keyfile_dict(sa_creds, scope)
        self.__google_client = gspread.authorize(credential)
        self.__google_sheet_name = sheet_name
