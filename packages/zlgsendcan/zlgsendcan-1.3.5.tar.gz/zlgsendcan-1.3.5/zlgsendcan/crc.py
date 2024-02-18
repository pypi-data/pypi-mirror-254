import copy
import json

from zlgsendcan.parseDBC import GlobleValue, DbcInit

"""
注意：所有项目的crc脚本都在该脚本文件，下方展示的是已知项目的crc校验规则的脚本，你可根据自己项目的校验规则按照下面方法去写脚本
例子：比如A88校验规则就是project_a88函数，然后将该函数名project_a88填入到pro_字典对应的项目下，对外提供的统一接口为crc_check；
如果不会写的可以将校验规则给到自动化测试组来编写
"""


# -----------------------------广汽--------------------------
# A88
def project_a88(*args):
    bit_pos = {'counter': 51, 'checksum': 63}

    k = args[0]
    v = args[1]
    ob = DbcInit(k, v, GlobleValue.dbc_init)
    # print(ob.get_signal_byname('BCS_VDCActiveSt'))
    init_data = ob.dbc_parser()
    # try:
    #     BCS_VDCActiveSt=v.get('BCS_VDCActiveSt')
    # except:
    #     pass
    # binary1 = bin(BCS_VDCActiveSt)[2:].zfill(4)

    check_bit = [7, 8]
    check_bit.sort()
    data = []

    b = int('0xff', 16) - init_data[0] - init_data[1] - init_data[2] - init_data[3] - init_data[4] - init_data[5] - \
        init_data[6] - init_data[7]
    for x7 in range(0, b):
        for x8 in range(0, b + 1):
            if x7 + x8 == b and 0 <= x7 < 16:
                c = copy.deepcopy(init_data)
                # c[check_bit[0] - 1] = hex(x7).split('x')[1]
                # c[check_bit[1] - 1] = hex(x8).split('x')[1]
                # if BCS_VDCActiveSt !=None:
                #     binary=bin(x7)[2:].zfill(8)
                #     binary=binary[:2] + str(BCS_VDCActiveSt) + binary[3:]
                #     c[check_bit[0] - 1] =int(binary,2)
                # else:
                c[check_bit[0] - 1] = init_data[6] + x7
                c[check_bit[1] - 1] = x8
                data.append(c)
    print(data)
    return data


# A58
def project_a58():
    pass


# A02
def project_a02(*args):
    return project_a88(*args)


# c03
def project_c03(*args):
    return project_a88(*args)


# --------------------------------------长城-------------------------------


def E2E_Counter(data, c_pos, c):
    Counter = data[c_pos] & 0x0F
    Counter += c
    if Counter > 14:
        Counter = Counter - 15
    a = data[c_pos] & 0xF0
    Counter = a + Counter
    return Counter


def E2E_CRC8(data):
    crc = 0x00  # 初始化校验值
    for byte in data:
        crc ^= byte  # 依次处理每个字节
        for _ in range(8):
            if (crc & 0x80):  # 判断最高位是否为1
                crc = ((crc << 1) ^ 0x1D)  # 如果是1，则左移一位并加上多项式0x1D
            else:
                crc <<= 1  # 如果是0，则左移一位
            crc &= 0xFF  # 对CRC校验值进行掩码操作，保证其在8位范围内
    return crc  # 返回计算出的CRC校验值


# 奇瑞t1j
def e2e_crc(data):
    crc = 0x00  # 初始化校验值
    data1 = [crc ^ bte for bte in data[0:7]]
    checksum = ((sum(data1) & 0xFF) ^ 0xFF) & 0xFF
    return checksum
# 奇瑞t28


#
# def comb_result(sigs_obj,data,  low_byte, high_byte,roll_count, crc_count):
#     a = []  # 定义一个空数组，用来存储15帧报文数据
#     for i in range(15):
#         crc_data_g1 = []  # 这个数组是用来将需要参与crc计算的数据添加进来
#         crc_data_g1.append(low_byte)  # dataid低字节
#         crc_data_g1.append(high_byte)  # dataid高字节
#         data1 = copy.deepcopy(data)
#         for s in sigs_obj:
#             s_d = s.__dict__
#             if s_d['start'] == int(roll_count*8):
#                 s_name = s_d['name']
#             data1[roll_count] = E2E_Counter(data1, roll_count, i)  # 动态改变rolling_counter值
#         for i in range(2, 9):
#             crc_data_g1.append(data1[i + (roll_count - 8)])
#         data1[crc_count] = E2E_CRC8(crc_data_g1)  # 调用crc8算法计算checksum值
#         a.append(data1)
#     return a
def comb_result(ob, low_byte, high_byte, roll_count, crc_count):
    a = []  # 定义一个空数组，用来存储15帧报文数据
    for i in range(15):
        crc_data_g1 = []  # 这个数组是用来将需要参与crc计算的数据添加进来
        if low_byte is not None:
            crc_data_g1.append(low_byte)  # dataid低字节
            crc_data_g1.append(high_byte)  # dataid高字节
        # data1 = copy.deepcopy(data)
        for s in ob.message_signas:
            s_d = s.__dict__
            if s_d['start'] == roll_count:
                s_name = s_d['name']
                ob.data[s_name] = i
                break
            # data1[roll_count] = E2E_Counter(data1, roll_count, i)  # 动态改变rolling_counter值
        re = ob.dbc_parser()

        # re[int(roll_count/8)]=E2E_Counter(re, int(roll_count/8), i)
        for i in range(2, 9):
            crc_data_g1.append(re[i + (int(roll_count / 8) - 8)])
        # re[int(crc_count / 8)] = E2E_CRC8(crc_data_g1)  # 调用crc8算法计算checksum值
        re[int(crc_count / 8)] = e2e_crc(crc_data_g1)  # 奇瑞t1j调用crc8算法计算checksum值
        re[int(crc_count / 8)] = e2e_crc(crc_data_g1)  # 奇瑞t28j调用crc8算法计算checksum值
        print([hex(i1) for i1 in re])
        a.append(re)
    return a


# 功能安全灯配置,若一个message下面有多个信号需要crc请按下面格式配置
dataId = {
    '0x137': {
        'ABSFailSts': {
            'low': 0x28,
            'hight': 0x00,
            'roll_c': 379,
            'crc_c': 327
        },

        'ESPFailSts': {
            'low': 0x2B,
            'hight': 0x00,
            'roll_c': 187,
            'crc_c': 135
        },
        'ESPFuncOffSts': {
            'low': 0x2B,
            'hight': 0x00,
            'roll_c': 187,
            'crc_c': 135
        },
        'EBDFailSts': {
            'low': 0x28,
            'hight': 0x00,
            'roll_c': 379,
            'crc_c': 327
        },
        'VehOdoInfo': {
            'low': 0x28,
            'hight': 0x00,
            'roll_c': 379,
            'crc_c': 327
        },
        "VehOdoInfoSts":
            {
                'low': 0x28,
                'hight': 0x00,
                'roll_c': 379,
                'crc_c': 327
            }
    }

}


# ES11/M81/M83/V71
# def project_m81(*args):
#     data = args[0]
#     sigs_obj = args[3]
#     data = [int(i, 16) for i in data]
#     up = hex(args[1]).split('0x')[1].upper()
#     aId = '0x' + up
#     if aId == '0x295':
#         data1 = comb_result(sigs_obj,data, 0x33, 0x00, 7, 0)
#         return data1
#     elif aId == '0x137':
#         if dataId.get(aId) is not None:
#             data2 = []
#             for k, v in dataId[aId].items():
#                 # if k in sig:
#                 l = dataId[aId][k]['low']
#                 h = dataId[aId][k]['hight']
#                 roll_c = dataId[aId][k]['roll_c']
#                 crc_c = dataId[aId][k]['crc_c']
#                 data1 = comb_result(data, l, h, roll_c, crc_c)
#                 data2.append(copy.deepcopy(data1))
#             if len(data2) > 1:
#                 for idx, v in enumerate(data2[1:]):
#                     for idx1, v1 in enumerate(v):
#                         for idx2, v2 in enumerate(v1):
#                             if v[idx1][idx2] != 0:
#                                 data2[0][idx1][idx2] = v[idx1][idx2]
#             return data2[0]
#
#     elif aId == '0x351':
#         data1 = comb_result(data, 0x3A, 0x00, 7, 0)
#         return data1
#     elif aId == '0x16B':
#         data1 = comb_result(data, 0x2A, 0x00, 7, 0)
#         return data1
#     elif aId == '0xF1':
#         data1 = comb_result(data, 0x0B, 0x00, 7, 0)
#         return data1
#     elif aId == '0x248':
#         data1 = comb_result(data, 0x8C, 0x00, 7, 0)
#         return data1
#     elif aId == '0x147':
#         data1 = comb_result(data, 0x35, 0x00, 7, 0)
#         return data1
#     elif aId == '0x201':
#         data1 = comb_result(data, 0x8D, 0x00, 7, 0)
#         return data1
#     elif aId == '0x219':
#         data1 = comb_result(data, 0xC1, 0x00, 15, 8)
#         return data1
#     elif aId == '0x236':
#         data1 = comb_result(data, 0xC2, 0x00, 15, 8)
#         return data1
#     elif aId == '0x12A':
#         data1 = comb_result(data, 0xB1, 0x00, 7, 0)
#         return data1
#     elif aId == '0x2D6':
#         data1 = comb_result(data, 0xC2, 0x00, 15, 8)
#         return data1
#     elif aId == '0x2F6':
#         data1 = comb_result(data, 0xAD, 0x00, 39, 32)
#         return data1


# 项目配置:项目对应的校验规则函数名称填入下面字典
def project_m81(*args):
    k = args[0]
    v = args[1]
    dbcinit = args[2]
    # data = [int(i, 16) for i in data]
    # up = hex(args[1]).split('0x')[1].upper()
    # aId = '0x' + up

    ob = DbcInit(k, v, dbcinit)
    up = hex(ob.message_frame_id).split('0x')[1].upper()
    aId = '0x' + up
    if aId == '0x295':
        data1 = comb_result(ob, 0x33, 0x00, 59, 7)
        return data1
    elif aId == '0x137':
        if dataId.get(aId) is not None:
            s = list(v.keys())[0]
            l = dataId[aId][s]['low']
            h = dataId[aId][s]['hight']
            roll_c = dataId[aId][s]['roll_c']
            crc_c = dataId[aId][s]['crc_c']
            data1 = comb_result(ob, l, h, roll_c, crc_c)
            return data1
    elif aId == '0x351':
        data1 = comb_result(ob, 0x3A, 0x00, 59, 7)
        return data1
    elif aId == '0x16B':
        data1 = comb_result(ob, 0x2A, 0x00, 59, 7)
        return data1
    elif aId == '0xF1':
        data1 = comb_result(ob, 0x0B, 0x00, 59, 7)
        return data1
    elif aId == '0x248':
        data1 = comb_result(ob, 0x8C, 0x00, 59, 7)
        return data1
    elif aId == '0x147':
        data1 = comb_result(ob, 0x35, 0x00, 59, 7)
        return data1
    elif aId == '0x201':
        data1 = comb_result(ob, 0x8D, 0x00, 59, 7)
        return data1
    elif aId == '0x219':
        data1 = comb_result(ob, 0xC1, 0x00, 123, 71)
        return data1
    elif aId == '0x236':
        data1 = comb_result(ob, 0x25, 0x00, 123, 71)
        return data1
    elif aId == '0x12A':
        data1 = comb_result(ob, 0xB1, 0x00, 59, 7)
        return data1
    elif aId == '0x2D6':
        data1 = comb_result(ob, 0xC3, 0x00, 123, 71)
        return data1
    elif aId == '0x2F6':
        data1 = comb_result(ob, 0xAD, 0x00, 315, 263)
        return data1
    elif aId == '0x168':
        data1 = comb_result(ob, 0x35, 0x00, 59, 7)
        return data1
    elif aId == '0x24F':
        data1 = comb_result(ob, 0xB2, 0x00, 59, 7)
        return data1
    elif aId == '0x2C0':
        data1 = comb_result(ob, None, None, 35, 55)
        return data1
    elif aId == '0x501':
        data1 = comb_result(ob, None, None, 35, 55)
        return data1


pro_ = {'A58': project_m81,
        'A88': project_a88,
        'A02': project_a02,
        'A19': None,
        'A13Y': None,
        'A8E': None,
        '唐海外版': None,
        'V71': project_m81,
        'V51': None,
        'V71EU': project_m81,
        'ES11': project_m81,
        'B01': None,
        'B01HEV/PHEV': None,
        'B03PHEV': None,
        'P05': None,
        'C01': project_m81,
        'C03': project_m81,
        'M81': project_m81,
        'FX11': None,
        'G426': None,
        'G636': None,
        'G733': None,
        'FS11-A2': None,
        'FX11-A2': None,
        'FX11-J1': None,
        'KX11-A2': None,
        'G3': None,
        'T18': None,
        'T1j': project_m81,
        'T28': project_m81
        }


# def crc_check(ischeck, pro=None, data=None, msgid=None, sig=None,sigs_obj=None):
#     if ischeck:
#         if pro_[pro] is not None:
#             return_da = pro_[pro](data, msgid, sig,sigs_obj)
#             return return_da
#         else:
#             re = f'当前{pro}项目未添加过crc脚本'
#             return re
#     else:
#         return None
def crc_check(pro=None, k=None, v=None,dbcinit=None):
    if pro is None:
        print('项目名称位None')
        return
    if pro_[pro] is not None:
        return_da = pro_[pro](k, v,dbcinit)
        return return_da
    else:
        re = f'当前{pro}项目未添加过crc脚本'
        return re


def calc_crc8(buf):
    crc = 0x00
    for b in buf:
        crc ^= b
        for i in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ 0x1D
            else:
                crc <<= 1
            crc &= 0xFF
    crc ^= 0xFF
    return crc


if __name__ == '__main__':
    # dbc = json.loads(GetBaseInfo().get_dbc_path())['dbc文件路径']
    # GlobleValue.dbc_init = get_signal_data1(dbc).db
    # # v=  {'EPBErrSts': '0', 'DrvModDispSts': '1', 'DrvGearDispSts': '0', 'DrvAutoGearDisp': '1'}
    # v = {'BCS_VDCActiveSt': '1'}
    # k = 'GW_BCS_2_B'
    # print(project_m81(k, v))
    # num1=1
    pass
