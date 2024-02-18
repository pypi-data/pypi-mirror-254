from passninja import passninja

account_id = 'aid_0x4'
api_key = 'b46c4b93c1f1ff831f754e04e43a55f6'

pass_ninja_client = passninja.PassNinjaClient(
    account_id,
    api_key
)

simple_pass_object = pass_ninja_client.passes.create(
    'ptk_0x4', # passType
    {
        "altitude": "0",
        "latitude": "25.7940827",
        "longitude": "-80.2209766",
        "location-text": "home",
        "max-distance": "50",
    }
)

print(simple_pass_object.id)
