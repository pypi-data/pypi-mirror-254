from .sdp_aio_api_core import SDP


class DeviceRegistration(SDP):

    async def register_device(self, input_data):
        '''
        Эта операция помогает зарегистрировать устройство для push-уведомлений.
        см. input_data в доках к api
        '''
        return await self.post_data(f'mobile_devices', input_data)
    
    async def unregister_device(self, registration_id):
        '''
        Эта операция помогает зарегистрировать устройство для push-уведомлений.
        см. input_data в доках к api
        '''
        return await self.post_data(f'mobile_devices/{registration_id}')