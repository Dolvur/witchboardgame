from typing import Dict, List

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, ws: WebSocket, game_id: str):
        await ws.accept()
        if game_id not in self.active_connections:
            self.active_connections[game_id] = []
        self.active_connections[game_id].append(ws)
        print(f"Client ({ws.client}) connected to game: {game_id}")

    def disconnect(self, ws: WebSocket, game_id: str):
        self.active_connections[game_id].remove(ws)
        if not self.active_connections[game_id]:
            del self.active_connections[game_id]  # If no players left, remove game

    async def broadcast(self, message: dict, game_id: str):
        if game_id in self.active_connections:
            for connection in self.active_connections[game_id]:
                try:
                    await connection.send_json(message)
                except Exception as e:
                    self.disconnect(connection, game_id)
                    print(f"Error sending message to client: {e}")
