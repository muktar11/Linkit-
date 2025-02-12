import django
django.setup()

'''
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.utils.timezone import now
from .models import CustomUser, Coin, UsedCoin


class CoinConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        phone = data.get('phone')
        coin_code = data.get('code')

        try:
            # Wrap ORM operations with sync_to_async
            user = await sync_to_async(CustomUser.objects.get)(phone=phone)
            coin = await sync_to_async(Coin.objects.get)(code=coin_code, expiry_date__gte=now())

            # Check if the coin has already been used
            used_coin_exists = await sync_to_async(UsedCoin.objects.filter(user=user, coin=coin).exists)()
            if used_coin_exists:
                response = {
                    'status': 'error',
                    'message': 'Coin has already been used.'
                }
            else:
                # Update user's coins
                user.coins += coin.value
                await sync_to_async(user.save)()

                # Record the used coin
                await sync_to_async(UsedCoin.objects.create)(user=user, coin=coin)

                response = {
                    'status': 'success',
                    'message': f"{float(coin.value)} coins added to user {user.phone}.",
                    'total_coins': float(user.coins)
                }
        except CustomUser.DoesNotExist:
            response = {'status': 'error', 'message': 'User not found.'}
        except Coin.DoesNotExist:
            response = {'status': 'error', 'message': 'Invalid or expired coin code.'}

        await self.send(text_data=json.dumps(response))
'''


from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json
from .models import CustomUser, Coin, UsedCoin  # Replace `your_app` with your actual app name
from django.utils.timezone import now

'''
class CoinConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract user_id from the query parameters
        self.user_id = self.scope['query_string'].decode().split('=')[1]  # Extract user_id from the query string

        try:
            # Fetch the user from the database
            self.user = await sync_to_async(CustomUser.objects.get)(id=self.user_id)
            response = {
                'total_coins': float(self.user.coins)  # Return the user's coin count
            }
        except CustomUser.DoesNotExist:
            response = {'status': 'error', 'message': 'User not found.'}
            await self.send(text_data=json.dumps(response))
            await self.close()  # Close the WebSocket connection if the user is not found
            return

        # Accept the WebSocket connection
        await self.accept()

        # Send the user's coin count
        await self.send(text_data=json.dumps(response))

    async def disconnect(self, close_code):
        # Handle WebSocket disconnection
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data.get('user_id')
        coin_code = data.get('code')
        try:
            # Wrap ORM operations with sync_to_async
            user = await sync_to_async(CustomUser.objects.get)(id=user_id)
            coin = await sync_to_async(Coin.objects.get)(code=coin_code, expiry_date__gte=now())

            # Check if the coin has already been used
            used_coin_exists = await sync_to_async(UsedCoin.objects.filter(user=user, coin=coin).exists)()
            if used_coin_exists:
                response = {
                    'status': 'error',
                    'message': 'Coin has already been used.'
                }
            else:
                # Update user's coins
                user.coins += coin.value
                await sync_to_async(user.save)()

                # Record the used coin
                await sync_to_async(UsedCoin.objects.create)(user=user, coin=coin)

                response = {
                    'status': 'success',
                    'message': f"{float(coin.value)} coins added to user {user.phone}.",
                    'total_coins': float(user.coins)
                }
        except CustomUser.DoesNotExist:
            response = {'status': 'error', 'message': 'User not found.'}
        except Coin.DoesNotExist:
            response = {'status': 'error', 'message': 'Invalid or expired coin code.'}

        await self.send(text_data=json.dumps(response))
'''

'''
{
    "action": "redeem_coin",
    "user_id": "123",
    "code": "ABC123"
}

'''

'''
{
    "action": "add_single_coin",
    "user_id": "1"
}

'''
class CoinConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract user_id from the query parameters
        self.user_id = self.scope['query_string'].decode().split('=')[1]  # Extract user_id from the query string

        try:
            # Fetch the user from the database
            self.user = await sync_to_async(CustomUser.objects.get)(id=self.user_id)
            response = {
                'total_coins': float(self.user.coins)  # Return the user's coin count
            }
        except CustomUser.DoesNotExist:
            response = {'status': 'error', 'message': 'User not found.'}
            await self.send(text_data=json.dumps(response))
            await self.close()  # Close the WebSocket connection if the user is not found
            return

        # Accept the WebSocket connection
        await self.accept()

        # Send the user's coin count
        await self.send(text_data=json.dumps(response))

    async def disconnect(self, close_code):
        # Handle WebSocket disconnection
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')  # Determine the action type
        user_id = data.get('user_id')

        if action == "add_single_coin":
            await self.add_single_coin(user_id)
        else:
            coin_code = data.get('code')
            await self.redeem_coin(user_id, coin_code)

    async def redeem_coin(self, user_id, coin_code):
        try:
            # Wrap ORM operations with sync_to_async
            user = await sync_to_async(CustomUser.objects.get)(id=user_id)
            coin = await sync_to_async(Coin.objects.get)(code=coin_code, expiry_date__gte=now())

            # Check if the coin has already been used
            used_coin_exists = await sync_to_async(UsedCoin.objects.filter(user=user, coin=coin).exists)()
            if used_coin_exists:
                response = {
                    'status': 'error',
                    'message': 'Coin has already been used.'
                }
            else:
                # Update user's coins
                user.coins += coin.value
                await sync_to_async(user.save)()

                # Record the used coin
                await sync_to_async(UsedCoin.objects.create)(user=user, coin=coin)

                response = {
                    'status': 'success',
                    'message': f"{float(coin.value)} coins added to user {user.phone}.",
                    'total_coins': float(user.coins)
                }
        except CustomUser.DoesNotExist:
            response = {'status': 'error', 'message': 'User not found.'}
        except Coin.DoesNotExist:
            response = {'status': 'error', 'message': 'Invalid or expired coin code.'}

        await self.send(text_data=json.dumps(response))

    async def add_single_coin(self, user_id):
        try:
            # Fetch the user from the database
            user = await sync_to_async(CustomUser.objects.get)(id=user_id)
            print('user', user)
            # Add a single coin to the user's balance
            user.coins += 1
            await sync_to_async(user.save)()

            response = {
                'status': 'success',
                'message': '1 coin added successfully.',
                'total_coins': float(user.coins)
            }
        except CustomUser.DoesNotExist:
            response = {'status': 'error', 'message': 'User not found.'}

        await self.send(text_data=json.dumps(response))
