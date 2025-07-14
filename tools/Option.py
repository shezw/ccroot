from enum import Enum
import json

class CCOptionType(Enum):
    BOOLEAN = "boolean"
    NUMBER = "number"
    STRING = "string"
    CHOICE = "choice"
    LIBRARY = "library"

class CCOptionDependsRelation(Enum):
    # AND = "&&"
    # OR = "||"
    NOT = "!"
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_THAN = "<"
    LESS_THAN_OR_EQUAL = "<="
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="
    def __str__(self):
        return self.value
    def __repr__(self):
        return f"CCOptionDependsRelation({self.value})"

class CCOptionDepends:
    def __init__(self, option: str, value = None, relation: CCOptionDependsRelation = None):
        self.option = option
        self.value = value
        self.relation = relation

    def __str__(self):
        if self.relation:
            return f"{self.option} {self.relation.value} {self.value}"
        else:
            return f"{self.option} {self.value}"

    def __repr__(self):
        return f"CCOptionDepends(option={self.option}, value={self.value}, relation={self.relation})"

    def to_json(self):
        if self.relation and self.value is not None:
            if self.relation == CCOptionDependsRelation.NOT:
                return f'{self.option}{CCOptionDependsRelation.NOT.__str__()+self.value}'
            else:
                return f'{self.option}{self.relation.__str__()+self.value}'
        else:
            return f'{self.option}{CCOptionDependsRelation.EQUAL.__str__()+self.value if self.value is not None else ""}'

    @classmethod
    def from_string(cls,depends_str: str):
        if not depends_str:
            return None
        dep = CCOptionDepends(option="", value=None, relation=None)
        for relation in CCOptionDependsRelation:
            if relation.value in depends_str:
                parts = depends_str.split(relation.value)
                if len(parts) == 2:
                    dep.option = parts[0].strip()
                    dep.value = parts[1].strip()
                    dep.relation = relation
                    return dep
        if dep.relation is None:
            # If no relation is found, assume it's a simple option without value
            dep.option = depends_str.strip()
            dep.value = None
            dep.relation = None
        return dep

class CCOption:
    # Name, Type, Default, Description, Value, Depends
    def __init__(self, name: str, opt_type: CCOptionType, default: str = None, description: str = None, value: str = None, choices:[]=None, depends: CCOptionDepends = None):
        self.name = name
        self.type = opt_type
        self.default = default
        self.description = description
        self.value = value if value is not None else None
        self.choices = choices  # Choices for choice type options
        self.depends = depends

    def __str__(self):
        return f"CCOption(name={self.name}, type={self.type}, default={self.default}, description={self.description}, value={self.value}, choices={self.choices}, depends={self.depends})"

    def __repr__(self):
        return f"CCOption(name={self.name}, type={self.type}, default={self.default}, description={self.description}, value={self.value}, choices={self.choices},, depends={self.depends})"

    def to_json(self):
        return {
            "name": self.name,
            "type": self.type.value,
            "default": self.default,
            "description": self.description,
            "value": self.value,
            "choices": self.choices if self.choices is not None else [],
            "depends": self.depends.to_json() if isinstance(self.depends, CCOptionDepends) else None
        }

    @classmethod
    def from_json(cls, json_data):
        if not json_data:
            return None
        if isinstance(json_data, str):
            import json
            json_data = json.loads(json_data)
        if not isinstance(json_data, dict):
            raise ValueError("Invalid JSON data for CCOption")
        # Create a new CCOption instance with the provided JSON data
        option = cls(
            name=json_data.get("name", ""),
            opt_type=CCOptionType(json_data.get("type", CCOptionType.STRING.value)),
            default=json_data.get("default"),
            description=json_data.get("description"),
            value=json_data.get("value")
        )

        if "choices" in json_data:
            if isinstance(json_data["choices"], list):
                option.choices = json_data["choices"]
            else:
                raise ValueError("Invalid choices format, expected a list")

        # Handle the depends field
        if "depends" in json_data:
            if isinstance(json_data["depends"], str):
                option.depends = CCOptionDepends.from_string(json_data["depends"])
            else:
                option.depends = CCOptionDepends(
                    option=json_data["depends"].get("option"),
                    value=json_data["depends"].get("value"),
                    relation=CCOptionDependsRelation(json_data["depends"].get("relation"))
                )
        else:
            option.depends = None

        return option

    @classmethod
    def options_from_json(cls, json_data):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        if not isinstance(json_data, list):
            raise ValueError("Invalid JSON data for CCOption list")
        options = []
        for item in json_data:
            options.append(cls.from_json(item))
        return options

    @classmethod
    def options_from_json_file(cls, file_path):
        with open(file_path, 'r') as f:
            json_data = json.load(f)
        if isinstance(json_data, list):
            return cls.options_from_json(json_data)
        else:
            try_get_single_option = cls.from_json(json_data)
            if try_get_single_option:
                return [try_get_single_option]
            else:
                return None