from infra.database.connector_users import get_user_data, set_user_data

class UserData:
    def __init__(self, id: int, type: str, start_step: int) -> None:
        self.id = id
        self.type = type
        self.step = start_step

        user_data = get_user_data(id)
        if not user_data:
            self.sort_type = 'date'
            self.sort_reverse = False
        else:
            self.sort_type, self.sort_reverse = user_data

    def set_sort_type(self, new_sort_type: str) -> None:
        self.sort_type = new_sort_type
        set_user_data(self.id, self.sort_type, self.sort_reverse)

    def set_sort_reverse(self, new_sort_reverse: bool) -> None:
        self.sort_reverse = new_sort_reverse
        set_user_data(self.id, self.sort_type, self.sort_reverse)