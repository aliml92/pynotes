from tortoise import Tortoise, fields, run_async
from tortoise.models import Model


class Event(Model):
    id = fields.IntField(pk=True)  
    name = fields.TextField()
    datetime = fields.DatetimeField(null=True)

    class Meta:
        table = "event"                        # table name 

    def __str__(self):
        return self.name

class Player(Model):
    id = fields.IntField(pk=True)  
    username = fields.TextField()
    hometown = fields.TextField()
    age = fields.IntField()
    registered = fields.BooleanField()

    class Meta:
        table = "player"                       # table name 

    def __str__(self):
        return self.name

async def run():
    await Tortoise.init(
        db_url="asyncpg://postgres:postgres@localhost:5442/postgres",
        modules={"models": ["__main__"]}
    )
    await Tortoise.generate_schemas(safe=True)

    

    # event = await Event.create(name="Test")
    # await Event.filter(id=event.id).update(name="Updated name")

    # print(await Event.filter(name="Updated name").first())

    # await Event(name="Test 2").save()
    # print(await Event.all().values_list("id", flat=True))

    # print(await Event.all().values("id", "name"))
    
    # conn = Tortoise.get_connection("default")

    # val = await conn.execute_query_dict("SELECT * FROM event")
    # print(val)
    # print(type(val))

    player = await Player.create(
        username="jondoe",
        hometown="Berlin",
        age=23,
        registered=True
    )

    username_in_search = "jondoe"

    print(Player.filter(id=player.id).sql())
    print(Player.filter(username=username_in_search).sql())

    conn = Tortoise.get_connection("default")
    await conn.execute_query("drop schema public cascade")
    await conn.execute_query("create schema public")

if __name__ == "__main__":
    run_async(run())