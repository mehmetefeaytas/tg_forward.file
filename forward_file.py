import os
import asyncio
from telethon import TelegramClient, events, errors
from telethon.tl.types import DocumentAttributeFilename, MessageMediaDocument
from tqdm.asyncio import tqdm
from config import api_id, api_hash

client = TelegramClient('session_name', api_id, api_hash)
client.start()

# Prompt the user to input the source and target group IDs
source_entity = int(input("Enter the source group ID: "))
target_entities = list(map(int, input("Enter the target group IDs, separated by commas: ").split(',')))

async def forward_file(message, target_entity):
    if isinstance(message.media, MessageMediaDocument):
        file_name = None
        for attr in message.media.document.attributes:
            if isinstance(attr, DocumentAttributeFilename):
                file_name = attr.file_name
                break
        if file_name is not None:
            try:
                # Attempt to send the file to the target group
                file_task = await client.send_file(target_entity, message.media, caption=message.text, allow_cache=True, file_name=file_name)
                await asyncio.sleep(1) # 1-second delay to avoid rate limiting
                return (file_name, file_task)
            except errors.FloodWaitError as e:
                await asyncio.sleep(e.seconds) # Handle flood wait errors by waiting
    return None

async def forward_all_files():
    for target_entity in target_entities:
        all_files = []
        async for message in tqdm(client.iter_messages(source_entity), desc=f"Source Group {source_entity}"):
            file_task = await forward_file(message, target_entity)
            if file_task is not None:
                all_files.append(file_task)
        file_names = set()
        for file_task in all_files:
            file_name, _ = file_task
            if file_name not in file_names:
                file_names.add(file_name)
            else:
                await client.delete_messages(target_entity, [m.id for fname, m in all_files if fname == file_name])
        for file_name in file_names:
            file_tasks = [ft for fname, ft in all_files if fname == file_name]
            for dest_entity in target_entities:
                if dest_entity != target_entity:
                    await client.forward_messages(dest_entity, file_tasks)
        await client.send_message(target_entity, f"All files successfully forwarded from {source_entity}.")

asyncio.get_event_loop().run_until_complete(forward_all_files())

client.disconnect()
