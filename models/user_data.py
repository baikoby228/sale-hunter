from infra.database.connector_users  import get_user_data, set_user_data

class UserData:
    def __init__(self, id: int, chat_id: int, type: str, start_step: int) -> None:
        self.id = id
        self.chat_id = chat_id
        self.type = type
        self.step = start_step

    async def init(self):
        user_data = await get_user_data(self.id)
        if not user_data:
            self.sort_type = 'date'
            self.sort_reverse = False
        else:
            pox, self.sort_type, self.sort_reverse = user_data
        await set_user_data(self.id, self.chat_id, self.sort_type, self.sort_reverse)

    async def set_sort_type(self, new_sort_type: str) -> None:
        self.sort_type = new_sort_type
        await set_user_data(self.id, self.chat_id, self.sort_type, self.sort_reverse)

    async def set_sort_reverse(self, new_sort_reverse: bool) -> None:
        self.sort_reverse = new_sort_reverse
        await set_user_data(self.id, self.chat_id, self.sort_type, self.sort_reverse)