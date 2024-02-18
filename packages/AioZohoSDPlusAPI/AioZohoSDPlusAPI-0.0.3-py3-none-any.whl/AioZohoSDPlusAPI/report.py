from .sdp_aio_api_core import SDP


class Report(SDP):

    async def get_all_query_reports_data(self, input_data=None):
        '''
        Эта операция извлекает все отчеты.
        '''
        if not input_data:
            input_data = {"list_info": {"row_count": 100,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "filter_by": {"name": "Query_reports"}}}
        return await self.get_data('reports', input_data)

    async def get_report_data(self, report_id):
        '''
        Эта операция извлекает данные по отчету.
        '''
        return await self.get_data(f'reports/{report_id}/execute')
    
    async def execute_sql_query(self, sql_query):
        input_data = {"query": sql_query}
        return await self.post_data(f'reports/execute_query', input_data)


    # Тут закончились методы указанные в документациях
