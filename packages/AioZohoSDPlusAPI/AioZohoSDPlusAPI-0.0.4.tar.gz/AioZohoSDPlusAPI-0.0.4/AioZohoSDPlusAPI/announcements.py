from .sdp_aio_api_core import SDP

class Announcements(SDP):

    async def get_all_announcements_data(self, input_data=None):
        '''
        Просмотреть все объявления
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return await self.get_data(f'announcements', input_data)
    
    async def get_announcement_data(self, announcement_id):
        '''
        Просмотреть данные об объявлении
        '''
        return await self.get_data(f'announcements/{announcement_id}')
    
    async def add_announcement(self, input_data):
        '''
        Добавить объявление
        см. input_data в доках к api
        '''
        return await self.post_data(f'announcements', input_data)
    
    async def update_announcement(self, announcement_id, input_data):
        '''
        Изменить объявление
        см. input_data в доках к api
        '''
        return await self.post_data(f'announcements/{announcement_id}', input_data)
    
    async def delete_announcement(self, announcement_id):
        '''
        Удалить объявление
        '''
        return await self.post_data(f'announcements/{announcement_id}')
    
    # Тут закончились методы указанные в документациях