from json import dumps, loads


obj = {"student": {"age": 28, "course": 1}}

s_obs = dumps(obj)
serialize_obs = loads(s_obs)
print(serialize_obs["student"])