from sqlalchemy import CHAR, Date, String, DateTime, BigInteger, Column

from config.database import Base


class BizStaffInfo(Base):
    """
    业务人员信息表
    """

    __tablename__ = 'biz_staff_info'
    __table_args__ = {'comment': '业务人员信息表'}

    staff_id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False, comment='人员ID')
    dept_id = Column(BigInteger, nullable=True, comment='部门ID')
    staff_name = Column(String(100), nullable=False, comment='人员姓名')
    oa_account = Column(String(50), nullable=False, comment='人员OA账号')
    employee_code = Column(String(50), nullable=False, comment='人员员工编码')
    mobile_phone = Column(String(11), nullable=True, comment='移动电话')
    company_email = Column(String(50), nullable=True, comment='公司邮箱')
    political_status = Column(String(50), nullable=True, comment='政治面貌')
    birth_date = Column(Date, nullable=True, comment='出生日期')
    native_place = Column(String(100), nullable=True, comment='籍贯')
    marital_status = Column(CHAR(1), nullable=True, comment='婚姻状况（0未婚 1已婚 2离异 3丧偶 9其他）')
    place_of_birth = Column(String(100), nullable=True, comment='出生地')
    household_type = Column(String(50), nullable=True, comment='户口类型（如：农业户口、非农业户口等）')
    household_address = Column(String(255), nullable=True, comment='户口所在地')
    ethnicity = Column(String(50), nullable=True, comment='民族')
    create_by = Column(String(64), nullable=True, comment='创建者')
    create_time = Column(DateTime, nullable=True, comment='创建时间')
    update_by = Column(String(64), nullable=True, comment='更新者')
    update_time = Column(DateTime, nullable=True, comment='更新时间')
    remark = Column(String(500), nullable=True, comment='备注')
    del_flag = Column(CHAR(1), nullable=True, comment='删除标志（0代表存在 2代表删除）')



