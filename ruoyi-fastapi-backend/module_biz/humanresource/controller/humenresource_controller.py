from datetime import datetime
from typing import Annotated

from fastapi import Form, Path, Query, Request, Response
from fastapi.responses import StreamingResponse
from pydantic_validation_decorator import ValidateFields
from sqlalchemy.ext.asyncio import AsyncSession

from common.annotation.log_annotation import Log
from common.aspect.db_seesion import DBSessionDependency
from common.aspect.interface_auth import UserInterfaceAuthDependency
from common.aspect.pre_auth import CurrentUserDependency, PreAuthDependency
from common.enums import BusinessType
from common.router import APIRouterPro
from common.vo import DataResponseModel, PageResponseModel, ResponseBaseModel
from module_admin.entity.vo.user_vo import CurrentUserModel
from module_biz.humanresource.service.humenresource_service import HumenresourceService
from module_biz.humanresource.entity.vo.humenresource_vo import HumenresourcePageQueryModel, HumenresourceRowModel
from utils.common_util import bytes2file_response
from utils.log_util import logger
from utils.response_util import ResponseUtil


humenresource_controller = APIRouterPro(
    prefix='/human/human_resource', order_num=50, tags=['业务人员信息'], dependencies=[PreAuthDependency()]
)


@humenresource_controller.get(
    '/list',
    summary='获取业务人员信息分页列表接口',
    description='用于获取业务人员信息分页列表',
    response_model=PageResponseModel[HumenresourceRowModel],
    dependencies=[UserInterfaceAuthDependency('human:human_resource:list')],
)
async def get_humanresource_humenresource_list(
        request: Request,
        human_resource_page_query: Annotated[HumenresourcePageQueryModel, Query()],
        query_db: Annotated[AsyncSession, DBSessionDependency()],
) -> Response:
    # 获取分页数据
    human_resource_page_query_result = \
        await HumenresourceService.get_humenresource_list_services(query_db, human_resource_page_query, is_page=True)
    logger.info('获取成功')

    return ResponseUtil.success(model_content=human_resource_page_query_result)

#
# @humenresource_controller.post(
#     '',
#     summary='新增业务人员信息接口',
#     description='用于新增业务人员信息',
#     response_model=ResponseBaseModel,
#     dependencies=[UserInterfaceAuthDependency('human:human_resource:add')],
# )
# @ValidateFields(validate_model='add_humenresource')
# @Log(title='业务人员信息', business_type=BusinessType.INSERT)
# async def add_humanresource_humenresource(
#     request: Request,
#     add_humenresource: HumenresourceModel,
#     query_db: Annotated[AsyncSession, DBSessionDependency()],
#     current_user: Annotated[CurrentUserModel, CurrentUserDependency()],
# ) -> Response:
#     add_humenresource.create_by = current_user.user.user_name
#     add_humenresource.create_time = datetime.now()
#     add_humenresource.update_by = current_user.user.user_name
#     add_humenresource.update_time = datetime.now()
#     add_humenresource_result = await HumenresourceService.add_humenresource_services(query_db, add_humenresource)
#     logger.info(add_humenresource_result.message)
#
#     return ResponseUtil.success(msg=add_humenresource_result.message)
#
#
# @humenresource_controller.put(
#     '',
#     summary='编辑业务人员信息接口',
#     description='用于编辑业务人员信息',
#     response_model=ResponseBaseModel,
#     dependencies=[UserInterfaceAuthDependency('human:human_resource:edit')],
# )
# @ValidateFields(validate_model='edit_humenresource')
# @Log(title='业务人员信息', business_type=BusinessType.UPDATE)
# async def edit_humanresource_humenresource(
#     request: Request,
#     edit_humenresource: HumenresourceModel,
#     query_db: Annotated[AsyncSession, DBSessionDependency()],
#     current_user: Annotated[CurrentUserModel, CurrentUserDependency()],
# ) -> Response:
#     edit_humenresource.update_by = current_user.user.user_name
#     edit_humenresource.update_time = datetime.now()
#     edit_humenresource_result = await HumenresourceService.edit_humenresource_services(query_db, edit_humenresource)
#     logger.info(edit_humenresource_result.message)
#
#     return ResponseUtil.success(msg=edit_humenresource_result.message)
#
#
# @humenresource_controller.delete(
#     '/{staff_ids}',
#     summary='删除业务人员信息接口',
#     description='用于删除业务人员信息',
#     response_model=ResponseBaseModel,
#     dependencies=[UserInterfaceAuthDependency('human:human_resource:remove')],
# )
# @Log(title='业务人员信息', business_type=BusinessType.DELETE)
# async def delete_humanresource_humenresource(
#     request: Request,
#     staff_ids: Annotated[str, Path(description='需要删除的人员ID')],
#     Annotated[AsyncSession, DBSessionDependency()],
# ) -> Response:
#     delete_humenresource = DeleteHumenresourceModel(staffIds=staff_ids)
#     delete_humenresource_result = await HumenresourceService.delete_humenresource_services(query_db, delete_humenresource)
#     logger.info(delete_humenresource_result.message)
#
#     return ResponseUtil.success(msg=delete_humenresource_result.message)
#
#
# @humenresource_controller.get(
#     '/{staff_id}',
#     summary='获取业务人员信息详情接口',
#     description='用于获取指定业务人员信息的详细信息',
#     response_model=DataResponseModel[HumenresourceModel],
#     dependencies=[UserInterfaceAuthDependency('humanresource:humenresource:query')]
# )
# async def query_detail_humanresource_humenresource(
#     request: Request,
#     staff_id: Annotated[int, Path(description='人员ID')],
#     query_db: Annotated[AsyncSession, DBSessionDependency()],
# ) -> Response:
#     humenresource_detail_result = await HumenresourceService.humenresource_detail_services(query_db, staff_id)
#     logger.info(f'获取staff_id为{staff_id}的信息成功')
#
#     return ResponseUtil.success(data=humenresource_detail_result)
#
#
# @humenresource_controller.post(
#     '/export',
#     summary='导出业务人员信息列表接口',
#     description='用于导出当前符合查询条件的业务人员信息列表数据',
#     response_class=StreamingResponse,
#     responses={
#         200: {
#             'description': '流式返回业务人员信息列表excel文件',
#             'content': {
#                 'application/octet-stream': {},
#             },
#         }
#     },
#     dependencies=[UserInterfaceAuthDependency('humanresource:humenresource:export')],
# )
# @Log(title='业务人员信息', business_type=BusinessType.EXPORT)
# async def export_humanresource_humenresource_list(
#     request: Request,
#     humenresource_page_query: Annotated[HumenresourcePageQueryModel, Form()],
#     query_db: Annotated[AsyncSession, DBSessionDependency()],
# ) -> Response:
#     # 获取全量数据
#     humenresource_query_result = await HumenresourceService.get_humenresource_list_services(query_db, humenresource_page_query, is_page=False)
#     humenresource_export_result = await HumenresourceService.export_humenresource_list_services(humenresource_query_result)
#     logger.info('导出成功')
#
#     return ResponseUtil.streaming(data=bytes2file_response(humenresource_export_result))
