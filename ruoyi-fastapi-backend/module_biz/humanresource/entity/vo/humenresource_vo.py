from datetime import datetime, date
from typing import Optional, Union

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from pydantic_validation_decorator import NotBlank

from module_admin.entity.vo.dept_vo import DeptModel


class HumenresourceModel(BaseModel):
    """
    业务人员信息表对应pydantic模型
    """
    model_config = ConfigDict(alias_generator=to_camel, from_attributes=True)
    staff_id: Optional[int] = Field(default=None, description='人员ID')
    dept_id: Optional[int] = Field(default=None, description='部门ID')
    staff_name: Optional[str] = Field(default=None, description='人员姓名')
    oa_account: Optional[str] = Field(default=None, description='人员OA账号')
    employee_code: Optional[str] = Field(default=None, description='人员员工编码')
    mobile_phone: Optional[str] = Field(default=None, description='移动电话')
    company_email: Optional[str] = Field(default=None, description='公司邮箱')
    political_status: Optional[str] = Field(default=None, description='政治面貌')
    birth_date: Optional[date] = Field(default=None, description='出生日期')
    native_place: Optional[str] = Field(default=None, description='籍贯')
    marital_status: Optional[str] = Field(default=None, description='婚姻状况（0未婚 1已婚 2离异 3丧偶 9其他）')
    place_of_birth: Optional[str] = Field(default=None, description='出生地')
    household_type: Optional[str] = Field(default=None, description='户口类型（如：农业户口、非农业户口等）')
    household_address: Optional[str] = Field(default=None, description='户口所在地')
    ethnicity: Optional[str] = Field(default=None, description='民族')
    create_by: Optional[str] = Field(default=None, description='创建者')
    create_time: Optional[datetime] = Field(default=None, description='创建时间')
    update_by: Optional[str] = Field(default=None, description='更新者')
    update_time: Optional[datetime] = Field(default=None, description='更新时间')
    remark: Optional[str] = Field(default=None, description='备注')
    del_flag: Optional[str] = Field(default=None, description='删除标志（0代表存在 2代表删除）')

    @NotBlank(field_name='staff_name', message='人员姓名不能为空')
    def get_staff_name(self) -> Union[str, None]:
        return self.staff_name

    @NotBlank(field_name='oa_account', message='人员OA账号不能为空')
    def get_oa_account(self) -> Union[str, None]:
        return self.oa_account

    @NotBlank(field_name='employee_code', message='人员员工编码不能为空')
    def get_employee_code(self) -> Union[str, None]:
        return self.employee_code


    def validate_fields(self) -> None:
        self.get_staff_name()
        self.get_oa_account()
        self.get_employee_code()



class HumenresourceRowModel(HumenresourceModel):
    """
    业务人员信息列表行数据模型
    """
    dept: Optional[DeptModel] = Field(default=None, description='部门信息')

    pass

class HumenresourceXXXXXXXModel(HumenresourceRowModel):
    """
    业务人员职位职级信息
    """

    pass
class humendetailModel(BaseModel):
    """
    业务人员详细信息
    """

    data: Optional[Union[HumenresourceModel, None]] = Field(default=None, description='用户信息')
    # 等待补充，部门信息，职位信息，角色信息，等等等，单一数据返回模型




    # post_ids: Optional[list] = Field(default=None, description='岗位ID信息')
    # posts: list[Union[PostModel, None]] = Field(description='岗位信息')
    # role_ids: Optional[list] = Field(default=None, description='角色ID信息')
    # roles: list[Union[RoleModel, None]] = Field(description='角色信息')




class HumenresourceQueryModel(HumenresourceRowModel):
    """
    业务人员信息不分页查询模型
    """
    pass


class HumenresourcePageQueryModel(HumenresourceQueryModel):
    """
    业务人员信息分页查询模型
    """

    page_num: int = Field(default=1, description='当前页码')
    page_size: int = Field(default=10, description='每页记录数')


class DeleteHumenresourceModel(BaseModel):
    """
    删除业务人员信息模型
    """

    model_config = ConfigDict(alias_generator=to_camel)

    staff_ids: str = Field(description='需要删除的人员ID')
