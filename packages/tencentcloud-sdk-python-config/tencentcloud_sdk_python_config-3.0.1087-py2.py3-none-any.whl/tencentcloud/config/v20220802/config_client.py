# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.config.v20220802 import models


class ConfigClient(AbstractClient):
    _apiVersion = '2022-08-02'
    _endpoint = 'config.tencentcloudapi.com'
    _service = 'config'


    def ListAggregateConfigRules(self, request):
        """账号组获取规则列表

        :param request: Request instance for ListAggregateConfigRules.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRulesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateConfigRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateConfigRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConfigRules(self, request):
        """获取规则列表

        :param request: Request instance for ListConfigRules.
        :type request: :class:`tencentcloud.config.v20220802.models.ListConfigRulesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListConfigRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConfigRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListConfigRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutEvaluations(self, request):
        """上报自定义规则评估结果

        :param request: Request instance for PutEvaluations.
        :type request: :class:`tencentcloud.config.v20220802.models.PutEvaluationsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.PutEvaluationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutEvaluations", params, headers=headers)
            response = json.loads(body)
            model = models.PutEvaluationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))