from .sdp_aio_api_core import SDP


class Solutions(SDP):
    async def get_all_solutions_data(self, input_data=None):
        '''
        Эта операция поможет вам просмотреть все существующие решения в приложении.
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_field": "topic"}}
        return await self.get_data(f'solutions', input_data)
    
    async def get_solution_data(self, solution_id):
        '''
        Просмотреть информацию о контракте
        ''' 
        return await self.get_data(f'solutions/{solution_id}')
    
    async def add_solution(self, input_data):
        '''
        Эта операция поможет вам добавить новое решение.
        см. input_data в доках к api
        '''
        return await self.post_data(f'solutions', input_data)
    
    async def update_solution(self, solution_id, input_data):
        '''
        Эта операция поможет вам обновить существующее решение.
        см. input_data в доках к api
        '''
        return await self.put_data(f'solutions/{solution_id}', input_data)
    
    async def delete_solution(self, solution_id):
        '''
        Эта операция поможет вам удалить существующее решение по solution_id.
        '''
        return await self.delete_data(f'solutions/{solution_id}')
    
    async def solution_approve(self, solution_id, operation_comment):
        '''
        Эта операция поможет вам утвердить существующее решение.
        '''
        input_data = {"solution": {"operation_comment": operation_comment}}
        return await self.put_data(f'solutions/{solution_id}/approve', input_data)
    
    async def solution_reject(self, solution_id, operation_comment):
        '''
        Эта операция поможет вам отклонить утверждение существующего решения.
        '''
        input_data = {"solution": {"operation_comment": operation_comment}}
        return await self.put_data(f'solutions/{solution_id}/reject', input_data)
    
    async def solution_like(self, solution_id):
        '''
        Эта операция поможет лакнуть решение.
        '''
        return await self.put_data(f'solutions/{solution_id}/like')
    
    async def solution_removelike(self, solution_id):
        '''
        Чтобы удалить лайк (или) неприязнь к решению
        '''
        return await self.put_data(f'solutions/{solution_id}/removelike')
    
    async def solution_reacted_users(self, solution_id):
        '''
        Эта операция поможет вам просмотреть понравившихся и не понравившихся пользователей решения.
        '''
        return await self.get_data(f'solutions/{solution_id}/reacted_users')
    
    # topic
    async def get_all_topics_data(self, input_data=None):
        '''
        Эта операция поможет вам просмотреть все существующие темы в приложении.
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": "3", "start_index": "1"}}
        return await self.get_data(f'topics', input_data)
    
    async def get_topic_data(self, topic_id):
        '''
        Эта операция поможет вам просмотреть существующую тему по topic_id.
        ''' 
        return await self.get_data(f'topics/{topic_id}')
    
    async def add_topic(self, input_data):
        '''
        Эта операция поможет вам добавить новую тему
        см. input_data в доках к api
        '''
        return await self.post_data(f'topics', input_data)
    
    async def update_topic(self, topic_id, input_data):
        '''
        Эта операция поможет вам переименовать тему.
        см. input_data в доках к api
        '''
        return await self.put_data(f'topics/{topic_id}', input_data)
    
    async def delete_topic(self, topic_id):
        '''
        Эта операция поможет вам удалить существующую тему по topic_id
        '''
        return await self.delete_data(f'topics/{topic_id}')
    
    async def topic_change_parent(self, topic_id, parent_topic_id):
        '''
        Эта операция поможет вам изменить родительскую тему.
        '''
        input_data = { "topic": {"parent": {"id": str(parent_topic_id)}}}
        return await self.put_data(f'topics/{topic_id}', input_data)

    async def topic_change_parent(self, topic_id):
        '''
        Эта операция поможет вам удалить родительский элемент и переместить 
        дочерний элемент в качестве родительского элемента темы.
        '''
        input_data = { "topic": {"parent": None}}
        return await self.put_data(f'topics/{topic_id}', input_data)