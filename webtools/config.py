import dataclasses

import toml


@dataclasses.dataclass(frozen=True)
class Config:
    ENV: str
    SECRET_KEY: str
    ALLOWED_HOST: str
    DATABASE_URL: str
    EXPORT_AS_BOOKMARK_REDIS_URL: str
    USE_X_FORWARDED_HOST: bool = False

    @classmethod
    def from_dict(cls, args):
        # Check type explicitly
        for field in dataclasses.fields(cls):
            if field.name in args:
                assert isinstance(args[field.name], field.type)
        return cls(**args)

    @classmethod
    def from_toml(cls, filepath):
        with open(filepath) as f:
            obj = toml.load(f)
        return cls.from_dict(obj["webtools"])
