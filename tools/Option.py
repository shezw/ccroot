from enum import Enum

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

class CCOption:
    # Name, Type, Default, Description, Value, Depends
    def __init__(self, name: str, opt_type: CCOptionType, default: str = None, description: str = None, value: str = None, depends: str = None):
        self.name = name
        self.type = opt_type
        self.default = default
        self.description = description
        self.value = value if value is not None else None
        self.depends = depends

    def __str__(self):
        return f"CCOption(name={self.name}, type={self.type}, default={self.default}, description={self.description}, value={self.value}, depends={self.depends})"

    def __repr__(self):
        return f"CCOption(name={self.name}, type={self.type}, default={self.default}, description={self.description}, value={self.value}, depends={self.depends})"

    def to_json(self):
        return {
            "name": self.name,
            "type": self.type.value,
            "default": self.default,
            "description": self.description,
            "value": self.value,
            "depends": self.depends.to_json() if isinstance(self.depends, CCOptionDepends) else None
        }