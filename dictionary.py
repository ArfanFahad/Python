config = {
    "db": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "pass": "secret",
    },
    "app": {
        "debug": True,
        "secret_key": "xyz123"
    },
    "machine": {
        "hardware": True,
        "software": {
            "linux": "Yes",
            "mac": {
                "mini_mac": True,
                "age": 40,
                "ok": "fine"
            }
        }
    }
}

db_mini_mac = config["machine"]["software"]["mac"]["age"]
print(db_mini_mac)


