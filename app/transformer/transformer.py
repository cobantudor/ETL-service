class Transformer:
    AVAILABLE_STRATEGIES = [
        'remove_undefined_user_orders',
        'keep_undefined_user_orders'
    ]

    def __init__(self):
        pass

    def merge_users_and_orders(self, users, orders, strategy='remove_undefined_user_orders'):
        user_orders = []
        users_dict = {}

        if strategy not in self.AVAILABLE_STRATEGIES:
            raise Exception('Undefined merging strategy')

        for user in users:
            user_id = user['user_id']
            del user['user_id']
            users_dict[user_id] = {f'user_{k}': v for k, v in user.items()}

        for order in orders:
            user_id = order['user_id']
            user_order = order

            if user_id in users_dict.keys():
                user_data = users_dict[user_id]
                user_order.update(user_data)
                user_orders.append(user_order)
            elif strategy == 'keep_undefined_user_orders':
                user_orders.append(user_order)

        return user_orders
