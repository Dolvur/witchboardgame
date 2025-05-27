from typing import Dict
from pydantic import BaseModel
from enum import Enum

import uvicorn
from ConnectionManager import ConnectionManager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()
manager = ConnectionManager()

# Starting with one single game for simplicity
game_state: Dict = {
    "game_id": "1",
    "status": "active",
    "round": 1,
    "phase": "brewing",
    "players": [],
    "fortune_teller": [],
    "market": {
        "available_ingredients": [
            {"type": "pumpkin", "cost": 2, "quanitity": 3},
            {"type": "crow_skull", "cost": 3, "quanitity": 2},
        ],
    },
}


class move(BaseModel):
    player_id: str
    action: str
    details: dict


class Player(BaseModel):
    player_id: str


class Ingredient(Enum):
    CHERRY_BOMB = "cherry_bomb"
    PUMPKIN = "pumpkin"
    GARDEN_SPIDER = "garden_spider"
    CROW_SKULL = "crow_skull"
    TOADSTOOL = "toadstool"
    MANDRAKE = "mandrake"
    GHOST_BREATH = "ghost_breath"
    AFRICAN_DEATH = "african_death"


# @app.post("/game/join/")  # TODO: Add game_id later
# async def join_game(player: Player):
#     if not any(p["player_id"] == player.player_id for p in game_state["players"]):
#         game_state["players].append({
#             "player_id": player.player_id,
#             "pot": [],
#             "bag": [Ingredient.PUMPKIN, Ingredient.GARDEN_SPIDER] +
#         })


@app.websocket("/ws/game/{game_id}")
async def websocket_endpoint(ws: WebSocket, game_id: str):
    await manager.connect(ws, game_id)
    try:
        while True:
            data = await ws.receive_json()
            # Handle received data (e.g., log it, process it)
            print(f"Received message: {data}")
            # Echo the message back to the client
            await manager.broadcast({"event": "player_message", "data": data}, game_id)
    except WebSocketDisconnect:
        # Handle client disconnect
        manager.disconnect(ws, game_id)
        print("Client disconnected.")
    except Exception as e:
        print(f"WebSocket error: {e}")
        manager.disconnect(ws, game_id)


@app.get("/")
async def root():
    return {"message:": "Hello, FastAPI!"}


@app.get("/test")
async def test():
    return {"message:": "test"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
