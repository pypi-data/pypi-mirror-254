# -*- coding: utf-8 -*-
# pydantic-1.10.12
import time
import pickle
from json import loads
from loguru import logger
from pydantic import BaseModel
from typing import Optional, List, Dict, Tuple
from k3cloud_webapi_sdk.main import K3CloudApiSdk


class RESPSchemaResponseStatus(BaseModel):
    """
    响应结构 第二层: ResponseStatus
    """
    IsSuccess: bool = None
    Errors: Optional[List] = None
    SuccessEntitys: Optional[List] = None
    SuccessMessages: Optional[List] = None
    MsgCode: int = None


class RESPSchemaResult(BaseModel):
    """
    响应结构 第一层
    """
    ResponseStatus: RESPSchemaResponseStatus = None
    NeedReturnData: Optional[List] = None


class RESPSchemaRES(BaseModel):
    """
    响应结构 Result
    """
    Result: RESPSchemaResult = None


class K3Formid:
    """
    业务对象
    """
    SAL_OUTSTOCK = "SAL_OUTSTOCK"                   # 销售出库
    SAL_RETURNSTOCK = "SAL_RETURNSTOCK"             # 销售退货
    STK_INSTOCK = "STK_INSTOCK"                     # 采购入库
    PUR_MRB = "PUR_MRB"                             # 采购退料
    STK_MISCELLANEOUS = "STK_MISCELLANEOUS"         # 其他入库
    STK_MISDELIVERY = "STK_MISDELIVERY"             # 其他出库
    STK_TRANSFERDIRECT = "STK_TRANSFERDIRECT"       # 直接调拨
    AR_RECEIVEBILL = "AR_RECEIVEBILL"               # 收款单
    AR_RECEIVABLE = "AR_RECEIVABLE"                 # 应收单
    AP_PAYABLE = "AP_PAYABLE"                       # 应付单
    BD_MATERIAL = "BD_MATERIAL"                     # 基础资料_物料
    BD_MATERIALCATEGORY = "BD_MATERIALCATEGORY"     # 存货类别
    BD_CURRENCY = "BD_CURRENCY"                     # 币别


class SchemaBatchSave(BaseModel):
    """批量保存输入参数"""
    # 是否用编码搜索基础资料，布尔类型，默认true（非必录）
    NumberSearch: bool = True

    # 是否验证数据合法性标志，布尔类型，默认true（非必录）注（设为false时不对数据合法性进行校验）
    ValidateFlag: bool = True

    # 是否删除已存在的分录，布尔类型，默认true（非必录）
    IsDeleteEntry = True

    # 是否批量填充分录，默认true（非必录）
    IsEntryBatchFill: str = None

    # 需要更新的字段，数组类型，格式：[key1, key2, ...] （非必录）
    # 注（更新字段时Model数据包中必须设置内码，若更新单据体字段还需设置分录内码）
    NeedUpDateFields: Optional[List] = None

    # 需返回结果的字段集合，数组类型，格式：[key, entitykey.key, ...]（非必录）
    # 注（返回单据体字段格式：entitykey.key）
    NeedReturnFields: Optional[List] = None

    # 表单所在的子系统内码，字符串类型（非必录）
    SubSystemId: str = None

    # 交互标志集合，字符串类型，分号分隔，格式："flag1;flag2;..."（非必录）
    # 例如（允许负库存标识：STK_InvCheckResult）
    InterationFlags: str = None

    # 服务端开启的线程数，整型（非必录） 注（数据包数应大于此值，否则无效）
    BatchCount: int = None

    # 是否验证所有的基础资料有效性，布尔类，默认false（非必录）
    IsVerifyBaseDataField: bool = True

    # 是否自动调整JSON字段顺序，布尔类型，默认false（非必录）
    IsAutoAdjustField: bool = True

    # 是否允许忽略交互，布尔类型，默认true（非必录）
    IgnoreInterationFlag: bool = True

    # 是否控制精度，为true时对金额、单价和数量字段进行精度验证，默认false（非必录）
    IsControlPrecision: bool = False

    # 校验Json数据包是否重复传入，一旦重复传入，接口调用失败，默认false（非必录）
    ValidateRepeatJson: bool = False

    # 表单数据包，JSON类型（必录）
    Model: Optional[List] = []


class SchemaSubmit(BaseModel):
    """单据提交输入参数"""
    # 创建者组织内码（非必录）
    CreateOrgId: int = 0
    # 单据编码集合，数组类型，格式：[No1,No2,...]（使用编码时必录）
    Numbers: Optional[List] = None
    # 单据内码集合，字符串类型，格式："Id1,Id2,..."（使用内码时必录）
    Ids: str = None
    # 是否启用网控，布尔类型，默认false（非必录）
    NetworkCtrl: bool = False
    # 是否允许忽略交互，布尔类型，默认true（非必录）
    IgnoreInterationFlag: bool = True


class SchemaAudit(BaseModel):
    """单据审核输入参数"""
    # 创建者组织内码（非必录）
    CreateOrgId: int = 0
    # 单据编码集合，数组类型，格式：[No1,No2,...]（使用编码时必录）
    Numbers: Optional[List] = None
    # 单据内码集合，字符串类型，格式："Id1,Id2,..."（使用内码时必录）
    Ids: str = None
    # 交互标志集合，字符串类型，分号分隔，格式："flag1;flag2;..."（非必录） 例如（允许负库存标识：STK_InvCheckResult）
    InterationFlags: str = None
    # 是否启用网控，布尔类型，默认false（非必录）
    NetworkCtrl: bool = False
    # 是否检验单据关联运行中的工作流实例，布尔类型，默认false（非必录）
    IsVerifyProcInst: bool = False
    # 是否允许忽略交互，布尔类型，默认true（非必录）
    IgnoreInterationFlag: bool = True
    # 是否应用单据参数设置分批处理，默认false
    UseBatControlTimes: bool = False


class SchemaUnAudit(BaseModel):
    """单据审核输入参数"""
    # 创建者组织内码（非必录）
    CreateOrgId: int = 0
    # 单据编码集合，数组类型，格式：[No1,No2,...]（使用编码时必录）
    Numbers: Optional[List] = None
    # 单据内码集合，字符串类型，格式："Id1,Id2,..."（使用内码时必录）
    Ids: str = None
    # 交互标志集合，字符串类型，分号分隔，格式："flag1;flag2;..."（非必录） 例如（允许负库存标识：STK_InvCheckResult）
    InterationFlags: str = None
    # 是否启用网控，布尔类型，默认false（非必录）
    NetworkCtrl: bool = False
    # 是否检验单据关联运行中的工作流实例，布尔类型，默认false（非必录）
    IsVerifyProcInst: bool = False
    # 是否允许忽略交互，布尔类型，默认true（非必录）
    IgnoreInterationFlag: bool = True


class SchemaDelete(BaseModel):
    """单据删除输入参数"""
    # 创建者组织内码（非必录）
    CreateOrgId: int = 0
    # 单据编码集合，数组类型，格式：[No1,No2,...]（使用编码时必录）
    Numbers: Optional[List] = None
    # 单据内码集合，字符串类型，格式："Id1,Id2,..."（使用内码时必录）
    Ids: str = None
    # 是否启用网控，布尔类型，默认false（非必录）
    NetworkCtrl: bool = False


class SchemaAllocate(BaseModel):
    """单据分配输入参数"""
    # 被分配的基础资料内码集合，字符串类型，格式："PkId1,PkId2,..."（必录）
    PkIds: str = None
    # 目标组织内码集合，字符串类型，格式："TOrgId1,TOrgId2,..."（必录）
    TOrgIds: str = None


class SchemaExecuteBillQuery(BaseModel):
    """单据查询输入参数"""
    # 业务对象表单Id（必录）
    FormId: str = None
    # 需查询的字段key集合，字符串类型，格式："key1,key2,..."（必录） 注（查询单据体内码,需加单据体Key和下划线,如：FEntryKey_FEntryId）
    FieldKeys: str = None
    # 过滤条件，数组类型，如：[{"Left":"(","FieldName":"Field1","Compare":"=","Value":"111","Right":")","Logic":"AND"},{"Left":"(","FieldName":"Field2","Compare":"=","Value":"222","Right":")","Logic":""}]
    FilterString: Optional[list] = []
    # 排序字段，字符串类型（非必录）
    OrderString: str = ''
    # 返回总行数，整型（非必录）
    TopRowCount: int = 0
    # 开始行索引，整型（非必录）
    StartRow: int = 0
    # 最大行数，整型，不能超过10000（非必录）
    Limit: int = 20
    # 表单所在的子系统内码，字符串类型（非必录）
    SubSystemId: str = ''


def split_list(li: list, size: int = None):
    """
    将给定列表按照指定大小分割成若干子列表

    :param li: 给定的列表
    :param size: 指定的子列表大小，如果 size 为 None，则默认将列表切分为长度相等的两个子列表
    :return: 分割后的子列表组成的列表
    """
    # 如果 size 为 None，则默认将列表切分为长度相等的两个子列表
    if size is None:
        size = len(li) // 2
    # 判断 size 是否合法
    if not isinstance(size, int) or size <= 0:
        return [li]
    # 使用列表切片分割列表，并使用列表推导式实现代码
    return [li[i:i+size] for i in range(0, len(li), size)]


class K3Api:
    def __init__(self, timeout: int = 300):
        self.api = K3CloudApiSdk(timeout=timeout)
        self.fomid = K3Formid
        self.bs_model: SchemaBatchSave = SchemaBatchSave()

    def init_api(self, config_path="kingdee.ini", config_node="config"):
        self.api.Init(config_path, config_node)

    @staticmethod
    def __status__(data_total, success_total, error_total, **kwargs):
        """
        打印结果状态
        :param data_total: 数据总条数
        :param success_total: 成功条数
        :param error_total: 失败条数
        :param kwargs:
        :return:
        """
        if error_total > 0 and success_total > 0:
            logger.warning(
                f"日期: {kwargs.get('date')} {kwargs.get('role')}({kwargs.get('formid')}) - 执行完成 "
                f"单据合计 {data_total} 条; 成功合计 {success_total} 条; 失败合计 {error_total} 条"
            )
        elif error_total > 0 and success_total == 0:
            logger.error(
                f"日期: {kwargs.get('date')} {kwargs.get('role')}({kwargs.get('formid')}) - 执行完成 "
                f"单据合计 {data_total} 条; 失败合计 {error_total} 条"
            )
        else:
            logger.debug(
                f"日期: {kwargs.get('date')} {kwargs.get('role')}({kwargs.get('formid')}) - 执行完成 "
                f"单据合计 {data_total} 条; 成功合计 {success_total} 条"
            )

    @staticmethod
    def __result__(flag, result):
        """
        打印结果明细
        :param flag:
        :param result:
        :return:
        """
        if not flag:
            return
        uniq_total = 0
        for res in result:
            if res.Result.ResponseStatus.Errors:
                for item in res.Result.ResponseStatus.Errors:
                    if item["Message"].startswith("违反字段唯一性要求：") and item["Message"].endswith("已经被使用。"):
                        uniq_total += 1
                        continue
                    logger.error(f"错误信息: \n\t{item}")
        if uniq_total:
            logger.warning(f"重复数据 {uniq_total} 条")

    @staticmethod
    def multi_entry_builder(model_pkg: Optional[List[Dict]], fno_key: str, entry_key: str, ) -> Optional[Tuple]:
        """
        单据构造多行分录
        :param model_pkg: 等待构造多行分录的数据模型
        :param fno_key: 单据编码字段名称
        :param entry_key: 需要构造多行分录的分录字段名称
        :return:
        """
        model_fz = {}
        # 遍历每一个只有一行分录的数据模型
        for one_model in model_pkg:
            # 单据编码
            f_number = one_model[fno_key]
            # 分录
            f_entry = one_model[entry_key]
            # 如果该单据已存在, 就把后面相同单据编号的分录一起累加到该单据的分录
            if f_number in model_fz:
                model_fz[f_number][entry_key] += f_entry
            # 如果不存在, 就新建这条单据模型记录
            else:
                model_fz[f_number] = one_model
        return list(model_fz.keys()), list(model_fz.values())

    def assemble_data(self, model_builder, records: Optional[List], fno_key: str, entry_key: str) -> Optional[tuple]:
        """
        将单条数据组合成数据包
        按照费用项目组合
        :param model_builder: 模型构造函数
        :param records: 原始数据
        :param fno_key: 单据编码字段名称
        :param entry_key: 需要构造多行分录的分录字段名称
        :return:
        """
        my_pkg = []
        for record in records:
            one_pkg = model_builder(record)
            if one_pkg:
                my_pkg.append(one_pkg)
        # 构造多行分录
        return self.multi_entry_builder(my_pkg, fno_key, entry_key)

    def batch_save(self, formid: str, data: list, split: int = 400, **kwargs) -> Optional[List]:
        """
        本接口用于实现单据批量保存(BatchSave)功能
        :param formid: 业务对象
        :param data: 单据模型
        :param split: 拆分保存 默认400
        :param kwargs: 其他参数 (可选)
        :return:
        """
        # 批量保存-单据模型结构
        schema = SchemaBatchSave(**kwargs)
        # 执行结果
        result = []
        # 拆分保存
        data_len = len(data)    # 数据包长度
        success_total = 0       # 初始化成功总数
        error_total = 0         # 初始化失败总数
        for batch_model in split_list(data, split):
            # 数据包模型
            schema.Model = batch_model        # 单批次执行的数据量
            data = schema.__dict__
            # 批量保存数据
            res = RESPSchemaRES(**loads(self.api.BatchSave(formid=formid, data=data)))
            success_batch = len(res.Result.ResponseStatus.SuccessEntitys)   # 单次执行成功数量
            error_batch = len(batch_model) - success_batch                  # 单次执行失败数量
            success_total += success_batch                                  # 累加 单次执行成功数量
            error_total += error_batch                                      # 累加 单次执行失败数量
            result.append(res)
            time.sleep(0.1)
        # 显示状态结果
        self.__status__(
            data_len,
            success_total,
            error_total,
            role="批量保存",
            formid=formid.upper(),
            date=kwargs.get("date")
        )
        # 显示明细结果
        self.__result__(kwargs.get("show_result"), result)
        return result

    def submit(self, formid: str, numbers: list, split: int = 5000, **kwargs) -> Optional[List]:
        """
        本接口用于实现提交(Submit)功能
        :param formid: 业务对象
        :param numbers: 单据编码
        :param split: 拆分
        :param kwargs: 其他参数
        :return:
        """
        # 提交-单据模型结构
        schema = SchemaSubmit(**kwargs)
        # 执行结果
        result = []
        data_total = len(numbers)  # 数据包总数
        success_total = 0  # 成功总数
        error_total = 0  # 失败总数
        for batch_numbers in split_list(numbers, split):
            # 数据包模型
            schema.Numbers = batch_numbers
            data = schema.dict()
            # 提交数据
            res = RESPSchemaRES(**loads(self.api.Submit(formid=formid, data=data)))

            success_batch = len(res.Result.ResponseStatus.SuccessEntitys)   # 单次执行成功数量
            error_batch = len(batch_numbers) - success_batch                # 单次执行失败数量
            success_total += success_batch                                  # 累加 单次执行成功数量
            error_total += error_batch                                      # 累加 单次执行失败数量
            result.append(res)
            time.sleep(0.1)
        # 显示状态结果
        self.__status__(
            data_total,
            success_total,
            error_total,
            role="批量提交",
            formid=formid.upper(),
            date=kwargs.get("date")
        )
        # 显示明细结果
        self.__result__(kwargs.get("show_result"), result)
        return result

    def audit(self, formid: str, numbers: list, split: int = 5000, **kwargs) -> Optional[List]:
        """
        本接口用于实现审核(Audit)功能
        :param formid: 业务对象
        :param numbers: 单据编码
        :param split: 拆分
        :param kwargs: 其他参数
        :return:
        """
        # 审核-单据模型结构
        schema = SchemaAudit(**kwargs)
        # 执行结果
        result = []
        data_total = len(numbers)  # 数据包总数
        success_total = 0  # 成功总数
        error_total = 0  # 失败总数
        for batch_numbers in split_list(numbers, split):
            # 数据包模型
            schema.Numbers = batch_numbers
            data = schema.dict()
            # 提交数据
            res = RESPSchemaRES(**loads(self.api.Audit(formid=formid, data=data)))
            success_batch = len(res.Result.ResponseStatus.SuccessEntitys)  # 单次执行成功数量
            error_batch = len(batch_numbers) - success_batch  # 单次执行失败数量
            success_total += success_batch  # 累加 单次执行成功数量
            error_total += error_batch  # 累加 单次执行失败数量
            result.append(res)
            time.sleep(0.1)
        # 显示状态结果
        self.__status__(data_total, success_total, error_total, role="批量审核", formid=formid.upper(), date=kwargs.get("date"))
        # 显示明细结果
        self.__result__(kwargs.get("show_result"), result)
        return result

    def un_audit(self, formid: str, numbers: list, split: int = 5000, **kwargs) -> Optional[List]:
        """
        本接口用于实现审核(Audit)功能
        :param formid: 业务对象
        :param numbers: 单据编码
        :param split: 拆分
        :param kwargs: 其他参数
        :return:
        """
        # 审核-反单据模型结构
        schema = SchemaUnAudit(**kwargs)
        # 执行结果
        result = []
        data_total = len(numbers)  # 数据包总数
        success_total = 0  # 成功总数
        error_total = 0  # 失败总数
        for batch_numbers in split_list(numbers, split):
            # 数据包模型
            schema.Numbers = batch_numbers
            data = schema.dict()
            # 提交数据
            res = RESPSchemaRES(**loads(self.api.UnAudit(formid=formid, data=data)))
            success_batch = len(res.Result.ResponseStatus.SuccessEntitys)  # 单次执行成功数量
            error_batch = len(batch_numbers) - success_batch  # 单次执行失败数量
            success_total += success_batch  # 累加 单次执行成功数量
            error_total += error_batch  # 累加 单次执行失败数量
            result.append(res)
            time.sleep(0.1)
        # 显示状态结果
        self.__status__(data_total, success_total, error_total, role="批量反审核", formid=formid.upper(),
                    date=kwargs.get("date"))
        # 显示明细结果
        self.__result__(kwargs.get("show_result"), result)
        return result

    def delete(self, formid: str, numbers: list, split: int = 5000, **kwargs) -> Optional[List]:
        """
        本接口用于实现删除(Delete)功能
        :param formid: 业务对象
        :param numbers: 单据编码
        :param split: 拆分
        :param kwargs: 其他参数
        :return:
        """
        # 删除-单据模型结构
        schema = SchemaDelete(**kwargs)
        # 执行结果
        result = []
        data_total = len(numbers)  # 数据包总数
        success_total = 0  # 成功总数
        error_total = 0  # 失败总数
        for batch_numbers in split_list(numbers, split):
            # 数据包模型
            schema.Numbers = batch_numbers
            data = schema.dict()
            # 删除
            res = RESPSchemaRES(**loads(self.api.Delete(formid=formid, data=data)))
            success_batch = len(res.Result.ResponseStatus.SuccessEntitys)  # 单次执行成功数量
            error_batch = len(batch_numbers) - success_batch  # 单次执行失败数量
            success_total += success_batch  # 累加 单次执行成功数量
            error_total += error_batch  # 累加 单次执行失败数量
            result.append(res)
            time.sleep(0.1)
        # 显示状态结果
        self.__status__(
            data_total,
            success_total,
            error_total,
            role="批量删除",
            formid=formid.upper(),
            date=kwargs.get("date")
        )
        # 显示明细结果
        self.__result__(kwargs.get("show_result"), result)
        return result

    def allocate(self, formid: str, **kwargs):
        """
        本接口用于实现分配(Allocate)功能
        - PkIds 被分配的基础资料内码集合，字符串类型，格式："PkId1,PkId2,..."（必录）
        - TOrgIds 目标组织内码集合，字符串类型，格式："TOrgId1,TOrgId2,..."（必录）
        :param formid: 业务对象
        :param kwargs: 其他参数
        :return:
        """
        schema = SchemaAllocate(**kwargs)
        logger.info(f'单据分配 - 开始')
        resp = RESPSchemaRES(**loads(self.api.Allocate(formid=formid, data=schema.dict())))
        # 打印结果
        if resp.Result.ResponseStatus.IsSuccess:
            logger.success(f'单据分配 - 成功 {len(resp.Result.ResponseStatus.SuccessEntitys)} 条')
        else:
            logger.error(f'单据分配 - 成功 {len(resp.Result.ResponseStatus.SuccessEntitys)} 条; '
                         f'失败 {len(resp.Result.ResponseStatus.Errors)}条')
        return resp

    def execute_bill_query(self, formid: str, field_keys: str, start_row: int = 0, limit: int = 20, max_row: int = 5, **kwargs):
        """
        本接口用于实现单据查询(ExecuteBillQuery)功能
        默认返回5条数据
        :param formid: 业务对象
        :param field_keys: 需查询的字段key集合，字符串类型，格式："key1,key2,..."（必录） 注（查询单据体内码,需加单据体Key和下划线,如：FEntryKey_FEntryId）
        :param start_row: 开始行索引，整型（非必录）
        :param limit: 最大行数，整型，不能超过10000（非必录）
        :param max_row: 返回最大行数  None或0 表示获取全部数据，大于 0 表示返回实际行数
        :param kwargs: 可选参数:OrderString - 排序字段，字符串类型（非必录）, SubSystemId - 表单所在的子系统内码，字符串类型（非必录）
        """
        # 如果 max_row 为 None 或 0，则获取全部数据
        if max_row == 0 or max_row is None:
            max_row = 999999999
        # 参数结构
        query = SchemaExecuteBillQuery(**kwargs)
        # 业务对象
        query.FormId = formid
        # 查询字段
        query.FieldKeys = field_keys
        # 偏移位置
        query.StartRow = start_row
        # 偏移量
        query.Limit = limit if 0 < limit <= 10000 else 20
        # 循环获取所有数据
        sum_total = 0
        # 剩余返回的总行数
        _max_row = pickle.loads(pickle.dumps(max_row))
        # print(query.dict())
        while True:
            # 获取本次查询的结果
            result = loads(self.api.ExecuteBillQuery(query.dict()))
            # 计算本次查询的结果总行数
            total = len(result)
            # 使用生成器返回本次查询的结果，从头开始取出不超过 _max_row 行数据
            yield from result[:_max_row]
            # 计算取出结果后还剩余的最大数据行数
            _max_row -= total
            # 计算已经取出的数据行数总和
            sum_total += total
            # 将游标移动到下一行，以便取下一批数据
            query.StartRow += query.Limit
            # total < query.Limit 如果获取到的查询结果不足一页或已经查询到最大行数时，则执行 return 退出循环
            # max_row <= sum_total 表示已经取出的数据行数总和 sum_total 是否超过或等于设定的最大行数
            if any((total < query.Limit, max_row <= sum_total)):
                return
