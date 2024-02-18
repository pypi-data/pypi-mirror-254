import aiohttp
import json
import mimetypes
import os


class SDP():

    def __init__(self, api_key, api_url_base):
        '''
        api_url_base должен в себе содержать url до /api/v3
        Например https://sd-exemple.ru/api/v3
        '''
        self.api_key = api_key
        self.api_url_base = api_url_base
        self.headers = {f"authtoken": self.api_key, "Content-Type": "application/json"}

    async def get_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP GET запросов и получения json ответа
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.api_url_base+'/'+api_method, params=params) as resp:
                return await resp.json()
            
    async def get_content_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP GET запросов с получением контента
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.api_url_base+'/'+api_method, params=params) as resp:
                return await resp.content.read()
            
    async def post_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP POST запросов и получения json ответа
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(self.api_url_base+'/'+api_method, params=params) as resp:
                return await resp.json()
            
    async def put_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP PUT запросов и получения json ответа
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.put(self.api_url_base+'/'+api_method, params=params) as resp:
                return await resp.json()
            
    async def delete_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP DELETE запросов и получения json ответа
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.delete(self.api_url_base+'/'+api_method, params=params) as resp:
                return await resp.json()
    
    async def send_file(self, file_path, method, http_method='post'):
        '''
        Для выполнения скачивания файла. Файл скачается на указанный file_path.
        В method нужно указать href url после /api/v3. Например: requests/{request_id}/attachments/{attachment_id}/download
        В http_method можно указать 2 варианта put или post
        '''
        file_name = file_path.split(os.path.sep)[-1]
        mimetype = mimetypes.guess_type(file_path)[0]
        headers = self.headers
        data = aiohttp.FormData(quote_fields=False)
        data.add_field('input_file',
                       open(file_path, 'rb'),
                       filename=file_name,
                       content_type=mimetype,
                       content_transfer_encoding="binary")
        headers['Content-Type'] = 'multipart/form-data; boundary='+data._writer.boundary
        async with aiohttp.ClientSession(headers=headers) as session:
            if http_method == 'post':
                async with session.post(self.api_url_base+'/'+method, data=data) as resp:
                    return await resp.json()
            elif http_method == 'put':
                async with session.put(self.api_url_base+'/'+method, data=data) as resp:
                    return await resp.json()
            else:
                return {"res": 'Not supported http_method'}