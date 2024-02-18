import sys
import aiohttp
import asyncio
sys.path.append('src')
from python_bring_api.bring import Bring
from python_bring_api.types import BringNotificationType

# Fix for asyncio on Windows (https://stackoverflow.com/questions/68123296/asyncio-throws-runtime-error-with-exception-ignored)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# SYNC

# Create Bring instance with email and password
bring = Bring("e.ball227@gmail.com", "SHSFJvKNOA*U4a5")
# Login
bring.login()

# Get information about all available shopping lists
lists = bring.loadLists()['lists']

# Save an item with specifications to a certain shopping list
bring.saveItem(lists[0]['listUuid'], 'Milk', 'low fat')
bring.saveItem(lists[0]['listUuid'], 'Bread')

# Get all the items of a list
items = bring.getItems(lists[0]['listUuid'])
print(items['purchase']) # [{'specification': 'low fat', 'name': 'Milk'}]

# Get all item details of a list
bring.getAllItemDetails(lists[0]['listUuid'])

# Update an item in a list
bring.updateItem(lists[0]['listUuid'], 'Milk', 'high fat')

# Remove an item from a list
bring.removeItem(lists[0]['listUuid'], 'Milk')

# Add an item to recents
bring.completeItem(lists[0]['listUuid'], 'Bread')

# Notify other users
bring.notify(lists[0]['listUuid'], BringNotificationType.CHANGED_LIST)

# ASYNC
async def main():
    async with aiohttp.ClientSession() as session:
        # Create Bring instance with email and password
        bring = Bring("e.ball227@gmail.com", "SHSFJvKNOA*U4a5", sessionAsync=session)
        # Login
        await bring.loginAsync()

        # Get information about all available shopping lists
        lists = (await bring.loadListsAsync())["lists"]

        # Save an item with specifications to a certain shopping list
        await bring.saveItemAsync(lists[0]['listUuid'], 'Milk', 'low fat')
        await bring.saveItemAsync(lists[0]['listUuid'], 'Bread')

        # Get all the items of a list
        items = await bring.getItemsAsync(lists[0]['listUuid'])
        print(items['purchase'])

        # Check of an item
        await bring.completeItemAsync(lists[0]['listUuid'], 'Bread')

        # Remove an item from a list
        await bring.removeItemAsync(lists[0]['listUuid'], 'Milk')

asyncio.run(main())

print('TEST COMPLETED!')