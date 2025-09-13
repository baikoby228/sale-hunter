from infra.database.connector_users import get_user_data

class UserData:
    sort_type = 'price'
    sort_reverse = False

    def __init__(self, id: int, type: str, start_step: int) -> None:
        self.type = type
        self.step = start_step

        user_data = get_user_data(id)

        if not user_data:
            self.sort_type = 'date'
            self.sort_reverse = False
        else:
            self.sort_type, self.sort_reverse = user_data