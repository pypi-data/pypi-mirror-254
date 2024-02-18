# -*- coding: utf-8 -*-
import sys
import asyncio
import numpy as np
from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
# from pyZlBusSdk import pyZlBus as zlb
import pyZlBusSdk.pyZlBus as zlb

# Serivce Characteristic UUID
config_notificaition_characteristic= "AEC91001-6E7A-4BC2-9A4C-4CDA7A728F58"
data_notificaition_characteristic= "AEC91002-6E7A-4BC2-9A4C-4CDA7A728F58"
status_notificaition_characteristic= "AEC91003-6E7A-4BC2-9A4C-4CDA7A728F58"

'''
# step 1
实例化解包单元,并设置内部解包FIFO大小
'''
pkt = zlb.ZlBusUnPack(fifoMaxSize = 20)

'''
# step 2
手动设置上传数据流水号编码, 默认FLOW_ID_FORMAT_8
'''
pkt.setFlowIdFormat(zlb.e_FLOW_FORMAT.FLOW_ID_FORMAT_8.value)

'''
# step 3
手动设置上传数据的数据格式，用于解包格式识别，错误的数据格式，无法解包成功，包数据直接丢弃
or
通过蓝牙获取, 见main函数中的如下调用
await client.write_gatt_char(config_notificaition_characteristic, zlb.ul_getDataFormat(), response=True)
'''
# pkt.setDataFormat((zlb.e_UpLoadDataForMat.UPLOAD_DATA_TIME.value | zlb.e_UpLoadDataForMat.UPLOAD_DATA_QUATERNION.value|
#                    zlb.e_UpLoadDataForMat.UPLOAD_DATA_GYRO.value | zlb.e_UpLoadDataForMat.UPLOAD_DATA_LIN_ACC.value))

DEBUG = 0

def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    if (DEBUG):
        print("low level rev data:",data) 

    '''
    # step 4
    将流数据加入进，解包接口
    '''
    pkt.decodeDataStreamInput(bytes(data))

    '''
    # step 5
    查询解包后,FIFO Block个数
    '''
    while pkt.count() > 0:
        '''
        # step 6
        获取FIFO Block, 无效Block 或FIFO 中无数据时,返回None
        '''
        block =  pkt.getHeadBlockNote() # or pkt.getHeadBlock(blockId)

        if block != None:
            # block.testPrint()
            if isinstance(block, zlb.ImuDataBlock):
                print('IMU 数据 类型')
                state, timeMs = block.getTimeStamp()
                if state:
                    print("时间戳 ms:", timeMs)
                state, quat = block.getAhrsQuaternion()
                if state:
                    print("四元数:", quat.w, quat.x, quat.y, quat.z)
                state, gyro = block.getGyro()
                if state:
                    print("陀螺仪:", gyro.x, gyro.y, gyro.z)
                state, linAcc = block.getLinAcc()
                if state:
                    print("线性加速度:", linAcc.x, linAcc.y, linAcc.z)
            elif isinstance(block, zlb.BatteryBlock):
                print('电池 数据 类型')
                state, mv = block.getAdcMv()
                if state:
                    print("电池电压:", mv)
                state, level = block.getLevel()
                if state:
                    print("电池电量:", level)
            elif isinstance(block, zlb.UploadDataFormatBlock):
                format = block.getUploadDataFormat()
                print("上报数据格式:", hex(format))
            else:
                print("其他数据类型", type(block))


async def main(device_name:str):
    print("start scan ...")
    
    device = await BleakScanner.find_device_by_name(device_name)
    if device is None:
        print("could not find device with name %s", device_name)


    disconnected_event = asyncio.Event()

    def disconnected_callback(client):
        print("Disconnected callback called")
        disconnected_event.set()


    print("connect to device ...")
    async with BleakClient(device, disconnected_callback=disconnected_callback) as client:
        print("Connected")
        # 启动Notify （上传数据相关）
        await client.start_notify(data_notificaition_characteristic, notification_handler)

        # 启动Notify （指令相关）
        await client.start_notify(config_notificaition_characteristic, notification_handler)

        # 启动Notify （电池相关）
        await client.start_notify(status_notificaition_characteristic, notification_handler)

        # 获取上传数据格式 (指令发送)
        await client.write_gatt_char(config_notificaition_characteristic, zlb.ul_getDataFormat(), response=True)

        await disconnected_event.wait()

def bleDemo(device_name:str = "ZL24-00000001-0000"):
    try:
        asyncio.run(main(device_name))
    except KeyboardInterrupt:
        sys.exit()

__all__ = [bleDemo]
