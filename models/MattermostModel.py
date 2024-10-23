import json
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional, Any, Dict

@dataclass_json
@dataclass
class Post:
    id: str
    create_at: int
    update_at: int
    edit_at: int
    delete_at: int
    is_pinned: bool
    user_id: str
    channel_id: str
    root_id: str
    original_id: str
    message: str
    type: str
    props: Dict[str, Any]
    hashtags: str
    pending_post_id: str
    reply_count: int
    last_reply_at: int
    participants: Optional[Any]
    metadata: Dict[str, Any]

@dataclass_json
@dataclass
class Data:
    channel_display_name: str
    channel_name: str
    channel_type: str
    mentions: str
    post: Post
    sender_name: str
    set_online: bool
    team_id: str

@dataclass_json
@dataclass
class Broadcast:
    omit_users: Optional[Any]
    user_id: str
    channel_id: str
    team_id: str
    connection_id: str
    omit_connection_id: str

@dataclass_json
@dataclass
class Event:
    event: str
    data: Data
    broadcast: Broadcast
    seq: int

json_data = '''{
    "event": "posted",
    "data": {
        "channel_display_name": "@albrecht",
        "channel_name": "qwrrotfuniyut8djj6e7wppypo__sb6jiewp4tybie9r8e87wuwpnr",
        "channel_type": "D",
        "mentions": "[\\"qwrrotfuniyut8djj6e7wppypo\\"]",
        "post": "{\\"id\\":\\"idrzuwcxifropkhqayiactshry\\",\\"create_at\\":1729605947517,\\"update_at\\":1729605947517,\\"edit_at\\":0,\\"delete_at\\":0,\\"is_pinned\\":false,\\"user_id\\":\\"sb6jiewp4tybie9r8e87wuwpnr\\",\\"channel_id\\":\\"rexp6n3xbffxxnefu5smooci9a\\",\\"root_id\\":\\"\\",\\"original_id\\":\\"\\",\\"message\\":\\"hello\\",\\"type\\":\\"\\",\\"props\\":{\\"disable_group_highlight\\":true},\\"hashtags\\":\\"\\",\\"pending_post_id\\":\\"sb6jiewp4tybie9r8e87wuwpnr:1729605947384\\",\\"reply_count\\":0,\\"last_reply_at\\":0,\\"participants\\":null,\\"metadata\\":{}}",
        "sender_name": "@albrecht",
        "set_online": true,
        "team_id": ""
    },
    "broadcast": {
        "omit_users": null,
        "user_id": "",
        "channel_id": "rexp6n3xbffxxnefu5smooci9a",
        "team_id": "",
        "connection_id": "",
        "omit_connection_id": ""
    },
    "seq": 2
}'''

if __name__ == '__main__':
# Convert dictionary to Event object
    event = Event.from_json(json_data)
    Event().to_json()
    print(event)
