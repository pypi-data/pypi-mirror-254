from .sdp_aio_api_core import SDP


class Personalization(SDP):

    async def add_personalization(self, input_data):
        '''
        Добавить персонализацию
        см. input_data в доках к api
        '''
        return await self.post_data(f'personalizations', input_data)
    
    async def get_personalization(self, registration_id):
        '''
        Посмотреть персонализацию
        '''
        return await self.get_data(f'personalizations')