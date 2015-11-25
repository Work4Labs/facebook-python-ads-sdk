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

from facebookads import test_config

ad_account_id = test_config.account_id

# _DOC oncall [duliomatos]
# _DOC open [ADACCOUNT_GET_REACHESTIMATE]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount, AdSet

account = AdAccount(ad_account_id)
targeting_spec = {
    'geo_locations': {
        'countries': ['US'],
    },
    'age_min': 20,
    'age_max': 40,
}
params = {
    'currency': 'USD',
    'optimize_for': AdSet.OptimizationGoal.offsite_conversions,
    'targeting_spec': targeting_spec,
}
reach_estimate = account.get_reach_estimate(params=params)
print(reach_estimate)
# _DOC close [ADACCOUNT_GET_REACHESTIMATE]