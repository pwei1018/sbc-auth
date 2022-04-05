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
"""Resource for in-app notifications endpoints."""
from http import HTTPStatus

from flask import jsonify
from flask_restx import Namespace, Resource, cors

from status_api.services.inapp_notificaitons import InAppNotifications as InAppNotificationsService
from status_api.utils.util import cors_preflight


API = Namespace('inapp', description='InApp Notifications Service System')

INAPP_NOTIFICATIONS_SERVICE = InAppNotificationsService()


@cors_preflight('GET')
@API.route('', methods=['GET', 'OPTIONS'], strict_slashes=False)
@API.route('/<string:application_name>', methods=['GET', 'OPTIONS'])
class InAppNotifications(Resource):
    """Endpoint resource to get in-app notifications."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @API.response(200, 'OK')
    def get(application_name: str = 'ALL'):
        """Get the in-app notifications."""
        response, status = INAPP_NOTIFICATIONS_SERVICE.get_inapp_notificaitons(application_name), HTTPStatus.OK
        return jsonify(response), status
