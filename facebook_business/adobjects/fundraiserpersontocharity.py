# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class FundraiserPersonToCharity(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isFundraiserPersonToCharity = True
        super(FundraiserPersonToCharity, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        amount_raised = 'amount_raised'
        charity_id = 'charity_id'
        currency = 'currency'
        description = 'description'
        donations_count = 'donations_count'
        donors_count = 'donors_count'
        end_time = 'end_time'
        external_amount_raised = 'external_amount_raised'
        external_donations_count = 'external_donations_count'
        external_donors_count = 'external_donors_count'
        external_event_name = 'external_event_name'
        external_event_start_time = 'external_event_start_time'
        external_event_uri = 'external_event_uri'
        external_fundraiser_uri = 'external_fundraiser_uri'
        external_id = 'external_id'
        goal_amount = 'goal_amount'
        id = 'id'
        internal_amount_raised = 'internal_amount_raised'
        internal_donations_count = 'internal_donations_count'
        internal_donors_count = 'internal_donors_count'
        name = 'name'
        uri = 'uri'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=FundraiserPersonToCharity,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'amount_raised': 'int',
        'charity_id': 'string',
        'currency': 'string',
        'description': 'string',
        'donations_count': 'int',
        'donors_count': 'int',
        'end_time': 'datetime',
        'external_amount_raised': 'int',
        'external_donations_count': 'int',
        'external_donors_count': 'int',
        'external_event_name': 'string',
        'external_event_start_time': 'datetime',
        'external_event_uri': 'string',
        'external_fundraiser_uri': 'string',
        'external_id': 'string',
        'goal_amount': 'int',
        'id': 'string',
        'internal_amount_raised': 'int',
        'internal_donations_count': 'int',
        'internal_donors_count': 'int',
        'name': 'string',
        'uri': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


