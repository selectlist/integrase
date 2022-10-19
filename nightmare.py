# Packages
import metro_integrase as metro
import os
from uuid import uuid4
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from sqlalchemy import Table, MetaData, create_engine, Column, String, JSON, Boolean, update, select, insert

# Configure Fast API
app = FastAPI()

# Configure Metro Reviews
MetroReviews = metro.Metro(domain="https://metro.select-list.xyz", list_id=os.environ["LIST_ID"], secret_key=os.environ["SECRET_KEY"], app=app)

# Database
engine = create_engine(os.environ["DATABASE_URI"])
metadata = MetaData()
connection = engine.connect()

# Bots schema
bots = Table(
    "bots",
    metadata,
    Column("bot_id", String),
    Column("uuid", String),
    Column("username", String),
    Column("description", String),
    Column("long_description", String),
    Column("state", String),
    Column("flags", JSON),
    Column("owner", String),
    Column("extra_owners", JSON),
    Column("library", String),
    Column("nsfw", Boolean),
    Column("tags", JSON),
    Column("invite", String),
)

# Claim
@MetroReviews.claim()
async def claim(request: Request, bot: metro.Bot):
    data = select([bots]).where(
        (bots.columns.bot_id == bot.bot_id)
    )
    
    botExists = False
    
    for row in connection.execute(data):
        botExists = True

    if botExists == True:
        update(bots).where(bots.bot_id == bot.bot_id).values(state="CLAIMED")
        res = {
            "content": "Bot Claimed",
            "done": True
        }
    else:
        uuid = uuid4()
        state = "CLAIMED"
        insert(bots).values(bot_id=bot.bot_id, uuid=uuid, username=bot.username, description=bot.description, long_description=bot.long_description, state=state, flags=["METRO"], owner=bot.owner, extra_owners=bot.extra_owners, library=bot.library, nsfw=bot.nsfw, tags=bot.tags, invite=bot.invite)
        res = {
            "content": "Bot Added and Claimed",
            "done": True
        }

    return ORJSONResponse(content=jsonable_encoder(res))

# Unclaim
@MetroReviews.unclaim()
async def unclaim(request: Request, bot: metro.Bot):
    data = select([bots]).where(
        (bots.columns.bot_id == bot.bot_id)
    )
    
    botExists = False
    
    for row in connection.execute(data):
        botExists = True

    if botExists == True:
        update(bots).where(bots.bot_id == bot.bot_id).values(state="AWAITING_REVIEW")
        res = {
            "content": "Bot Unclaimed",
            "done": True
        }
    else:
        uuid = uuid4()
        state = "AWAITING_REVIEW"
        insert(bots).values(bot_id=bot.bot_id, uuid=uuid, username=bot.username, description=bot.description, long_description=bot.long_description, state=state, flags=["METRO"], owner=bot.owner, extra_owners=bot.extra_owners, library=bot.library, nsfw=bot.nsfw, tags=bot.tags, invite=bot.invite)
        res = {
            "content": "Bot Added and Unclaimed",
            "done": True
        }

    return ORJSONResponse(content=jsonable_encoder(res))

# Approve
@MetroReviews.approve()
async def approve(request: Request, bot: metro.Bot):
    data = select([bots]).where(
        (bots.columns.bot_id == bot.bot_id)
    )
    
    botExists = False
    
    for row in connection.execute(data):
        botExists = True

    if botExists == True:
        update(bots).where(bots.bot_id == bot.bot_id).values(state="APPROVED")
        res = {
            "content": "Bot Approved",
            "done": True
        }
    else:
        uuid = uuid4()
        state = "APPROVED"
        insert(bots).values(bot_id=bot.bot_id, uuid=uuid, username=bot.username, description=bot.description, long_description=bot.long_description, state=state, flags=["METRO"], owner=bot.owner, extra_owners=bot.extra_owners, library=bot.library, nsfw=bot.nsfw, tags=bot.tags, invite=bot.invite)
        res = {
            "content": "Bot Added and Approved",
            "done": True
        }

    return ORJSONResponse(content=jsonable_encoder(res))


# Deny
@MetroReviews.deny()
async def deny(request: Request, bot: metro.Bot):
    data = select([bots]).where(
        (bots.columns.bot_id == bot.bot_id)
    )
    
    botExists = False
    
    for row in connection.execute(data):
        botExists = True

    if botExists == True:
        update(bots).where(bots.bot_id == bot.bot_id).values(state="DENIED")
        res = {
            "content": "Bot Denied",
            "done": True
        }
    else:
        uuid = uuid4()
        state = "DENIED"
        insert(bots).values(bot_id=bot.bot_id, uuid=uuid, username=bot.username, description=bot.description, long_description=bot.long_description, state=state, flags=["METRO"], owner=bot.owner, extra_owners=bot.extra_owners, library=bot.library, nsfw=bot.nsfw, tags=bot.tags, invite=bot.invite)
        res = {
            "content": "Bot Added and Denied",
            "done": True
        }

    return ORJSONResponse(content=jsonable_encoder(res))

# Startup Event
@app.on_event("startup")
async def startup():
    print("Started!")
    await MetroReviews.register_api_urls()
