# Packages
import metro_integrase as metro
import os
from uuid import uuid4
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from sqlalchemy import Table, MetaData, create_engine, Column, String, JSON, Boolean, DateTime, update, select, insert
from dotenv import load_dotenv
load_dotenv()

# Configure Fast API
app = FastAPI()

# Configure Metro Reviews
metro_reviews = metro.Metro(domain="https://metro.select-list.xyz", list_id=os.getenv("LIST_ID"), secret_key=os.getenv("SECRET_KEY"), app=app)

# Database
engine = create_engine(os.getenv("DATABASE_URI"))
metadata = MetaData()
connection = engine.connect()

# Bots schema
bots = Table(
    "bots",
    metadata,
    Column("bot_id", String),
    Column("avatar", String),
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
    Column("audit_logs", JSON),
    Column("createdAt", DateTime),
    Column("updatedAt", DateTime)
)

# Claim
@metro_reviews.claim()
async def claim(request: Request, bot: metro.Bot):
    data = select([bots]).where(
        (bots.columns.bot_id == bot.bot_id)
    )
    
    date = datetime.now()

    botExists = False
    
    for row in connection.execute(data):
        botExists = True

    if botExists == True:
        logs = row.audit_logs
        
        logs.append({
            "uuid": str(uuid4()),
            "action": "CLAIMED",
            "user": "0"
        })

        connection.execute(update(bots).where(bots.columns.bot_id == bot.bot_id).values(state="CLAIMED", audit_logs=logs))
        res = {
            "content": "Bot Claimed",
            "done": True
        }
    else:
        uuid = uuid4()
        state = "CLAIMED"
        connection.execute(insert(bots).values(bot_id=bot.bot_id, avatar="/defaultavatar.png", uuid=uuid, username=bot.username, description=bot.description, long_description=bot.long_description, state=state, flags=["METRO"], owner=bot.owner, extra_owners=bot.extra_owners, library=bot.library, nsfw=bot.nsfw, tags=bot.tags, invite=bot.invite, audit_logs=[{"uuid": str(uuid4()), "action": "CLAIMED", "user": "0"}], createdAt=date, updatedAt=date))
        res = {
            "content": "Bot Added and Claimed",
            "done": True
        }

    return ORJSONResponse(content=jsonable_encoder(res))

# Unclaim
@metro_reviews.unclaim()
async def unclaim(request: Request, bot: metro.Bot):
    data = select([bots]).where(
        (bots.columns.bot_id == bot.bot_id)
    )
    
    date = datetime.now()

    botExists = False
    
    for row in connection.execute(data):
        botExists = True

    if botExists == True:
        logs = row.audit_logs
        
        logs.append({
            "uuid": str(uuid4()),
            "action": "UNCLAIMED",
            "user": "0"
        })

        connection.execute(update(bots).where(bots.columns.bot_id == bot.bot_id).values(state="AWAITING_REVIEW", audit_logs=logs))
        res = {
            "content": "Bot Unclaimed",
            "done": True
        }
    else:
        uuid = uuid4()
        state = "AWAITING_REVIEW"
        connection.execute(insert(bots).values(bot_id=bot.bot_id, avatar="/defaultavatar.png", uuid=uuid, username=bot.username, description=bot.description, long_description=bot.long_description, state=state, flags=["METRO"], owner=bot.owner, extra_owners=bot.extra_owners, library=bot.library, nsfw=bot.nsfw, tags=bot.tags, invite=bot.invite, audit_logs=[{"uuid": str(uuid4()), "action": "UNCLAIMED", "user": "0"}], createdAt=date, updatedAt=date))
        res = {
            "content": "Bot Added and Unclaimed",
            "done": True
        }

    return ORJSONResponse(content=jsonable_encoder(res))

# Approve
@metro_reviews.approve()
async def approve(request: Request, bot: metro.Bot):
    data = select([bots]).where(
        (bots.columns.bot_id == bot.bot_id)
    )
    
    date = datetime.now()

    botExists = False
    
    for row in connection.execute(data):
        botExists = True

    if botExists == True:
        logs = row.audit_logs
        
        logs.append({
            "uuid": str(uuid4()),
            "action": "APPROVED",
            "user": "0"
        })

        connection.execute(update(bots).where(bots.columns.bot_id == bot.bot_id).values(state="APPROVED", audit_logs=logs))
        res = {
            "content": "Bot Approved",
            "done": True
        }
    else:
        uuid = uuid4()
        state = "APPROVED"
        connection.execute(insert(bots).values(bot_id=bot.bot_id, avatar="/defaultavatar.png", uuid=uuid, username=bot.username, description=bot.description, long_description=bot.long_description, state=state, flags=["METRO"], owner=bot.owner, extra_owners=bot.extra_owners, library=bot.library, nsfw=bot.nsfw, tags=bot.tags, invite=bot.invite, audit_logs=[{"uuid": str(uuid4()), "action": "APPROVED", "user": "0"}], createdAt=date, updatedAt=date))
        res = {
            "content": "Bot Added and Approved",
            "done": True
        }

    return ORJSONResponse(content=jsonable_encoder(res))


# Deny
@metro_reviews.deny()
async def deny(request: Request, bot: metro.Bot):
    data = select([bots]).where(
        (bots.columns.bot_id == bot.bot_id)
    )
    
    date = datetime.now()

    botExists = False
    
    for row in connection.execute(data):
        botExists = True

    if botExists == True:
        logs = row.audit_logs
        
        logs.append({
            "uuid": str(uuid4()),
            "action": "DENIED",
            "user": "0"
        })

        connection.execute(update(bots).where(bots.columns.bot_id == bot.bot_id).values(state="DENIED", audit_logs=logs))
        res = {
            "content": "Bot Denied",
            "done": True
        }
    else:
        uuid = uuid4()
        state = "DENIED"
        connection.execute(insert(bots).values(bot_id=bot.bot_id, avatar="/defaultavatar.png", uuid=uuid, username=bot.username, description=bot.description, long_description=bot.long_description, state=state, flags=["METRO"], owner=bot.owner, extra_owners=bot.extra_owners, library=bot.library, nsfw=bot.nsfw, tags=bot.tags, invite=bot.invite, audit_logs=[{"uuid": str(uuid4()), "action": "DENIED", "user": "0"}], createdAt=date, updatedAt=date))
        res = {
            "content": "Bot Added and Denied",
            "done": True
        }

    return ORJSONResponse(content=jsonable_encoder(res))

# Startup Event
@app.on_event("startup")
async def startup():
    print("Started!")
    await metro_reviews.register_api_urls()
