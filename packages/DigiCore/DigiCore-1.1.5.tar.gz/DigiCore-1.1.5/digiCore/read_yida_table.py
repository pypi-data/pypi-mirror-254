# -*- coding: utf-8 -*-

from alibaba.alibabacloud_dingtalk.yida_1_0.client import Client as dingtalkyida_1_0Client
from alibaba.alibabacloud_tea_openapi import models as open_api_models
from alibaba.alibabacloud_dingtalk.yida_1_0 import models as dingtalkyida__1__0_models
from alibaba.alibabacloud_tea_util import models as util_models


class YidaTableTools:
    def __init__(self, app_type, system_token, form_uuid, user_id, access_token):
        self.access_token = access_token
        self.user_id = user_id
        self.app_type = app_type
        self.system_token = system_token
        self.form_uuid = form_uuid
        self.client = self.init_client()

    def init_client(self):
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_1_0Client(config)

    def get_form_table_data(
            self, page_number, page_size=100
    ) -> []:
        """
        读取表格数据
        :return:
        """
        search_form_data_second_generation_headers = dingtalkyida__1__0_models.SearchFormDataSecondGenerationHeaders()
        search_form_data_second_generation_headers.x_acs_dingtalk_access_token = self.access_token
        search_form_data_second_generation_request = dingtalkyida__1__0_models.SearchFormDataSecondGenerationRequest(
            page_number=page_number,
            form_uuid=self.form_uuid,
            system_token=self.system_token,
            page_size=page_size,
            user_id=self.user_id,
            app_type=self.app_type
        )
        try:
            response = self.client.search_form_data_second_generation_with_options(
                search_form_data_second_generation_request,
                search_form_data_second_generation_headers,
                util_models.RuntimeOptions())
            return response.body.to_map().get('data')
        except Exception as err:
            return []

    def table_item_define(
            self,
    ) -> []:
        """
        获取表格组件定义列表
        :return:
        """
        get_form_component_definition_list_headers = dingtalkyida__1__0_models.GetFormComponentDefinitionListHeaders()
        get_form_component_definition_list_headers.x_acs_dingtalk_access_token = self.access_token
        get_form_component_definition_list_request = dingtalkyida__1__0_models.GetFormComponentDefinitionListRequest(
            system_token=self.system_token,
            user_id=self.user_id,
            language='zh_CN'
        )
        try:
            response = self.client.get_form_component_definition_list_with_options(self.app_type, self.form_uuid,
                                                                                   get_form_component_definition_list_request,
                                                                                   get_form_component_definition_list_headers,
                                                                                   util_models.RuntimeOptions())
            return response.body.to_map().get('result')
        except Exception as err:
            return []

    def get_sub_from_table_data(
            self,
            form_instance_id,
            table_field_id='tableField_lm5lyvkc',
            page_number=1
    ):
        """
        获取应用中子表单的数据
        """
        list_table_data_by_form_instance_id_table_id_headers = dingtalkyida__1__0_models.ListTableDataByFormInstanceIdTableIdHeaders()
        list_table_data_by_form_instance_id_table_id_headers.x_acs_dingtalk_access_token = self.access_token
        list_table_data_by_form_instance_id_table_id_request = dingtalkyida__1__0_models.ListTableDataByFormInstanceIdTableIdRequest(
            app_type=self.app_type,
            form_uuid=self.form_uuid,
            table_field_id=table_field_id,
            page_number=page_number,
            page_size=50,
            system_token=self.system_token,
            user_id=self.user_id
        )
        try:
            result = self.client.list_table_data_by_form_instance_id_table_id_with_options(
                form_instance_id,
                list_table_data_by_form_instance_id_table_id_request,
                list_table_data_by_form_instance_id_table_id_headers, util_models.RuntimeOptions())
            return result
        except Exception as err:
            return {}
