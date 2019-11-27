# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class ModifyTagWithUuidRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ModifyTagWithUuid','sas')

	def get_TagId(self):
		return self.get_query_params().get('TagId')

	def set_TagId(self,TagId):
		self.add_query_param('TagId',TagId)

	def get_MachineTypes(self):
		return self.get_query_params().get('MachineTypes')

	def set_MachineTypes(self,MachineTypes):
		self.add_query_param('MachineTypes',MachineTypes)

	def get_TagList(self):
		return self.get_query_params().get('TagList')

	def set_TagList(self,TagList):
		self.add_query_param('TagList',TagList)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_UuidList(self):
		return self.get_query_params().get('UuidList')

	def set_UuidList(self,UuidList):
		self.add_query_param('UuidList',UuidList)