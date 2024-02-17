#!/bin/python

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .mbio import MBIO

from .items import Items
# from .config import MBIOConfig
from .xmlconfig import XMLConfig
from .device import MBIODevices, MBIODeviceGeneric
from .value import MBIOValues, MBIOValueDigital

from .metzconnect import MBIODeviceMetzConnectMRAI8
from .metzconnect import MBIODeviceMetzConnectMRAOP4
from .metzconnect import MBIODeviceMetzConnectMRDI10
from .metzconnect import MBIODeviceMetzConnectMRDI4
from .metzconnect import MBIODeviceMetzConnectMRDO4
from .belimo import MBIODeviceBelimoP22RTH
from .digimatplc import MBIODeviceDigimatPLC
from .ebm import MBIODeviceEBM

import time
import threading

from prettytable import PrettyTable

from pymodbus.client import ModbusTcpClient
import logging
# from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder

# Modbus Clients Examples
# https://pymodbus.readthedocs.io/en/dev/source/examples.html


class MBIOGateway(object):
    """MBIOGateway object, containing MBIOValues containing every MBIOValue"""
    def __init__(self, parent: MBIO, name, host, port=502, interface=None, timeout=3, retries=3, xml: XMLConfig = None):
        self._parent: MBIO = parent
        self._name=str(name).lower()
        if not name:
            name='gw%d' % parent.gateways.count()
        self._host=host
        self._interface=interface
        self._port=port
        self._timeout=timeout
        self._retries=retries
        self._error=False

        self._key='%s' % self._name

        self._client: ModbusTcpClient=None
        self._timeoutClient=0
        self._timeoutIdleAfterSend=0

        self._devices=MBIODevices(parent.logger)
        self._sysvalues=MBIOValues(self, self.key, self.logger)
        self._sysComErr=MBIOValueDigital(self._sysvalues, 'comerr')

        self.logger.info('Declaring GW:%s', self.host)

        self._eventStop=threading.Event()

        self.load(xml)

        # FIXME: daemon=True ?
        self._thread=threading.Thread(target=self.manager)
        self.logger.info("Starting background GW:%s task" % self.host)
        self._thread.start()

    @property
    def parent(self) -> MBIO:
        return self._parent

    def getMBIO(self) -> MBIO:
        return self._parent

    @property
    def logger(self):
        return self._parent.logger

    def onLoad(self, xml: XMLConfig):
        pass

    def load(self, xml: XMLConfig):
        if xml:
            try:
                if xml.isConfig('gateway'):
                    # TODO: clone other gw feature
                    self.onLoad(xml)
            except:
                self.logger.exception('%s:%s:load()' % (self.__class__.__name__, self.key))

    @property
    def key(self):
        return self._key

    def timeout(self, delay):
        return time.time()+delay

    def isTimeout(self, t):
        if time.time()>=t:
            return True
        return False

    def isOpen(self):
        if self._client and self._client.is_socket_open():
            return True
        return False

    def open(self):
        if not self._client:
            try:
                self.logger.info('Connecting to GW %s:%d (interface %s)' % (self._host, self._port, self._interface))
                source=(self._interface, 0)
                if not self._interface:
                    source=None
                self._client=ModbusTcpClient(host=self._host, port=self._port,
                            source_address=source,
                            timeout=self._timeout,
                            retries=self._retries,
                            # broadcast_enable=True,
                            # strict=True,
                            close_comm_on_error=False)
                # FIXME: how to disable correctly pymodbus logging (connect errors) ?
                logger=logging.getLogger()
                if logger:
                    logger.setLevel(logging.CRITICAL)
                self._timeoutIdleAfterSend=0
            except:
                pass

        if self._client:
            if self._client.connected:
                return self._client
            try:
                if self.isTimeout(self._timeoutClient):
                    self._timeoutClient=self.timeout(15)
                    self.logger.info('Opening socket')
                    if self._client.connect():
                        return self._client
            except:
                pass

    def close(self):
        try:
            if self._client:
                self.logger.info('Closing socket')
                self._client.close()
        except:
            pass
        self._client=None

    @property
    def client(self):
        return self.open()

    @property
    def name(self):
        return self._name

    @property
    def host(self):
        return self._host

    def probe(self, address):
        try:
            self.logger.debug('Probing device address %d' % address)
            self.checkIdleAfterSend()
            r=self.client.read_device_information(slave=address)
            self.signalMessageTransmission()
            if r and not r.isError():
                data={'address': address,
                      'vendor': r.information[0].decode(),
                      'model': r.information[1].decode(),
                      'version': r.information[2].decode()}
                self.logger.info('Found device [%s] [%s] %s at address %d' %
                                 (data['vendor'], data['model'], data['version'], address))
                return data
        except:
            pass

    # FIXME: implement a better MBIODevice class registration
    def declareDeviceFromName(self, vendor, model, address, xml: XMLConfig = None):
        try:
            address=int(address)
            model=model or 'unknown'

            if vendor and address>0:
                vendor=vendor.lower()
                model=model.lower()
                device=None

                if 'metz' in vendor:
                    if 'di10' in model:
                        device=MBIODeviceMetzConnectMRDI10(self, address, xml=xml)
                    if 'di4' in model:
                        device=MBIODeviceMetzConnectMRDI4(self, address, xml=xml)
                    elif 'do4' in model:
                        device=MBIODeviceMetzConnectMRDO4(self, address, xml=xml)
                    elif 'aop4' in model or 'ao4' in model:
                        device=MBIODeviceMetzConnectMRAOP4(self, address, xml=xml)
                    elif 'ai8' in model:
                        device=MBIODeviceMetzConnectMRAI8(self, address, xml=xml)

                elif 'belimo' in vendor:
                    if 'p22rth' in model:
                        device=MBIODeviceBelimoP22RTH(self, address, xml=xml)

                elif 'digimat' in vendor:
                    if 'plc' in model:
                        device=MBIODeviceDigimatPLC(self, address, xml=xml)

                elif 'ebm' in vendor:
                    if 'base' in model:
                        device=MBIODeviceEBM(self, address, xml=xml)

                elif 'generic' in vendor:
                    device=MBIODeviceGeneric(self, address, xml=xml)

                return device
        except:
            pass

    def discover(self, start=1, end=32, maxerrors=3):
        devices=[]
        errors=0
        for address in range(start, end+1):
            data=self.probe(address)
            if data:
                if not self.device(address):
                    device=self.declareDeviceFromName(data['vendor'], data['model'], address)
                    if device:
                        devices.append(device)
                continue
            errors+=1
            maxerrors-=1
            if maxerrors>0 and errors>maxerrors:
                break
        return devices

    def ping(self, address):
        try:
            self.checkIdleAfterSend()
            r=self.client.diag_read_bus_message_count(slave=address)
            self.signalMessageTransmission()
            if r:
                if not r.isError():
                    return True
            self.logger.error('Unable to ping device %d' % address)
        except:
            # self.logger.exception('ping')
            pass
        return False

    def stop(self):
        self.halt()
        self._eventStop.set()

    def waitForThreadTermination(self):
        self.stop()
        self._thread.join()
        self.close()

    def sleep(self, delay=1):
        try:
            if self._eventStop.is_set():
                return True
            return self._eventStop.wait(delay)
        except:
            pass

    def checkIdleAfterSend(self):
        while not self.isTimeout(self._timeoutIdleAfterSend):
            self.sleep(0.001)

    def signalMessageTransmission(self):
        # https://minimalmodbus.readthedocs.io/en/stable/serialcommunication.html
        # 19200bps->2ms
        self._timeoutIdleAfterSend=self.timeout(0.002)

    def manager(self):
        while True:
            self.sleep(0.1)
            try:
                halted=True
                error=False
                for device in self._devices:
                    device.manager()
                    device.microsleep()
                    if device.isError():
                        error=True
                    if not device.isHalted():
                        halted=False

                self._error=error
                self._sysComErr.updateValue(self._error)

                if self._eventStop.is_set():
                    if halted:
                        self.logger.info("Exiting background GW:%s task" % self.host)
                        self.close()
                        return
            except:
                self.logger.exception("Background GW:%s task" % self.host)

    def isError(self):
        return self._error

    @property
    def devices(self):
        return self._devices

    def device(self, did):
        return self._devices.item(did)

    def reset(self, address=None):
        if address is not None:
            try:
                self.device(address).reset()
            except:
                pass
        else:
            self._devices.reset()

    def resetHalted(self):
        self._devices.resetHalted()

    def halt(self, address=None):
        if address is not None:
            try:
                self.device(address).halt()
            except:
                pass
        else:
            self._devices.halt()

    def dump(self):
        if self._devices:
            t=PrettyTable()
            t.field_names=['ADR', 'Key', 'Vendor', 'Model', 'Version', 'Class', 'State', 'Error', 'Values']
            t.align='l'
            for device in self._devices:
                t.add_row([device.address, device.key, device.vendor, device.model, device.version,
                           device.__class__.__name__, device.statestr(), str(device.isError()), device.values.count()])

        print(t.get_string(sortby="ADR"))

    def count(self):
        return len(self._devices)

    def __getitem__(self, key):
        return self.device(key)

    # FIXME: for METZ only
    def rs485(self, speed, parity='E'):
        data=0x5300

        parity=parity.upper()
        if parity[0]=='E':
            data|=0x10
        elif parity[0]=='O':
            data|=0x20
        else:
            data|=0x30

        try:
            n=[1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200].index(int(speed))
            data|=(0x1+n)
        except:
            return

        self.checkIdleAfterSend()
        self.client.write_registers(0x41, data, slave=0)
        self.signalMessageTransmission()
        # self.client.diag_restart_communication(False, slave=0)
        # for device in self._devices:
        for device in range(1, 32):
            print("Set speed 0x%02X for device %d" % (data, device))
            self.checkIdleAfterSend()
            self.client.write_registers(0x41, data)
            self.signalMessageTransmission()

    def __repr__(self):
        state='CLOSED'
        if self.isOpen():
            state='OPEN'
        return '%s(%s=%s, %d devices, %s)' % (self.__class__.__name__, self.name, self.host, self.count(), state)

    # FIXME: debug
    def toggle(self):
        for device in self.devices:
            try:
                device.toggle()
            except:
                pass

    def on(self):
        for device in self.devices:
            try:
                device.on()
            except:
                pass

    def off(self):
        for device in self.devices:
            try:
                device.off()
            except:
                pass

    def auto(self):
        for device in self.devices:
            device.auto()

    def manual(self):
        for device in self.devices:
            device.manual()


class MBIOGateways(Items):
    def __init__(self, logger):
        super().__init__(logger)
        self._items: list[MBIOGateway]=[]
        self._itemByHost={}
        self._itemByKey={}
        self._itemByName={}

    def item(self, key):
        item=super().item(key)
        if item:
            return item

        item=self.getByKey(key)
        if item:
            return item

        item=self.getByHost(key)
        if item:
            return item

        item=self.getByName(key)
        if item:
            return item

        try:
            return self[key]
        except:
            pass

    def add(self, item: MBIOGateway) -> MBIOGateway:
        if isinstance(item, MBIOGateway):
            super().add(item)
            self._itemByName[item.name]=item
            self._itemByKey[item.key]=item
            self._itemByHost[item.host]=item

    def getByHost(self, host):
        try:
            return self._itemByHost[host]
        except:
            pass

    def getByName(self, name):
        try:
            return self._itemByName[name]
        except:
            pass

    def getByKey(self, key):
        try:
            return self._itemByKey[key]
        except:
            pass

    def stop(self):
        for item in self._items:
            item.stop()

    def reset(self):
        for item in self._items:
            item.reset()

    def halt(self):
        for item in self._items:
            item.halt()

    def resetHalted(self):
        for item in self._items:
            item.resetHalted()

    def waitForThreadTermination(self):
        for item in self._items:
            item.waitForThreadTermination()

    def discover(self):
        for item in self._items:
            item.discover()

    # def dump(self):
        # if not self.isEmpty():
            # t=PrettyTable()
            # t.field_names=['#', 'Key', 'Name', 'Host', 'Open']
            # t.align='l'
            # for item in self._items:
                # t.add_row([self.index(item), item.key, item.name, item.host, item.isOpen()])

        # print(t.get_string(sortby="Key"))


if __name__ == "__main__":
    pass
