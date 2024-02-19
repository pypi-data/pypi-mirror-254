from .sdp_aio_api_core import SDP

class Asset(SDP):

    async def get_all_assets_data(self, input_data=None):
        '''
        Просмотреть все активы
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return await self.get_data(f'assets', input_data)
    
    async def get_asset_data(self, asset_id):
        '''
        Просмотреть данные об активе
        '''
        return await self.get_data(f'assets/{asset_id}')
    
    async def add_asset(self, input_data):
        '''
        Добавить актив
        см. input_data в доках к api
        '''
        return await self.post_data(f'assets', input_data)
    
    async def update_asset(self, asset_id, input_data):
        '''
        Изменить информации в активе
        см. input_data в доках к api
        '''
        return await self.put_data(f'assets/{asset_id}', input_data)
    
    async def delete_asset(self, asset_id):
        '''
        Удалить актив
        '''
        return await self.delete_data(f'assets/{asset_id}')
    
    async def get_asset_metainfo(self):
        '''
        Получить метаинформацию об активах
        '''
        return await self.get_data(f'assets/metainfo')
    
    async def copy_asset(self, asset_id, number_copies=1):
        '''
        Копировать актив
        '''
        input_data = {"copy": {"number_copies": str(number_copies)}}
        return await self.post_data(f'assets/{asset_id}/copy', input_data)
    
    async def configure_depreciation_asset(self, asset_id, input_data):
        '''
        Настройка амортизации актива.
        см. input_data в доках к api
        '''
        return await self.post_data(f'assets/{asset_id}/configure_depreciation', input_data)
    
    # workstation
    async def get_all_workstations_data(self, input_data=None):
        '''
        Просмотреть все рабочие станции
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return await self.get_data(f'workstations', input_data)
    
    async def get_workstation_data(self, workstation_id):
        '''
        Просмотреть данные об рабочей станции
        '''
        return await self.get_data(f'workstations/{workstation_id}')
    
    async def add_workstation(self, input_data):
        '''
        Добавить рабочюю станцию
        см. input_data в доках к api
        '''
        return await self.post_data(f'workstations', input_data)
    
    async def update_workstation(self, workstation_id, input_data):
        '''
        Эта операция позволяет обновить рабочую станцию.
        см. input_data в доках к api
        '''
        return await self.put_data(f'workstations/{workstation_id}', input_data)
    
    async def delete_workstation(self, workstation_id):
        '''
        Удалить актив
        '''
        return await self.delete_data(f'workstations/{workstation_id}')
    
    async def get_workstation_metainfo(self):
        '''
        API Metainfo предоставляет метаданные дополнительных полей рабочей станции, 
        идентификатора дополнительных полей актива и атрибутов CI. 
        Атрибуты CI рабочей станции можно добавить и обновить, 
        передав идентификатор типа продукта в качестве аргумента этому API
        '''
        return await self.get_data(f'workstations/metainfo')
    
    async def copy_workstation(self, workstation_id, number_copies=1):
        '''
        Копировать актив
        '''
        input_data = {"copy": {"number_copies": str(number_copies)}}
        return await self.post_data(f'workstations/{workstation_id}/copy', input_data)
    
     # Тут закончились методы указанные в документациях