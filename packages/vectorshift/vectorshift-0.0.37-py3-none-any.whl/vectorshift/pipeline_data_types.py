# This is meant to be more or less identical to the implementation of datatypes in 
# the API repo for consistency. If we collapse into a monorepo then we can get rid
# of the duplication here.

class PipelineDataType:
    def __init__(self, name: str, subtypes: set['PipelineDataType'] = None) -> None:
        if name == 'Any':
            assert subtypes == set()
            assert isinstance(self, AnyType)
        self.name = name
        self.subtypes = subtypes or set()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'PipelineDataType({self.name})'

    def __eq__(self, other: 'PipelineDataType') -> bool:
        return self.name == other.name and self.subtypes == other.subtypes

    def __hash__(self) -> int:
        return hash((self.name, tuple(self.subtypes)))

    def contains(self, other: 'PipelineDataType') -> bool:
        if self == other:
            return True
        elif (
            isinstance(other, ListType)
            and self.name == 'text'
            and other.element_type.is_subset(self)
        ):
            return True
        return any(subtype.contains(other) for subtype in self.subtypes)

    def is_subset(self, other: 'PipelineDataType') -> bool:
        return other.contains(self)

    def intersects(self, other: 'PipelineDataType') -> bool:
        return self.contains(other) or other.contains(self)


class ListType(PipelineDataType):
    def __init__(self, element_type: 'PipelineDataType') -> None:
        super().__init__(
            name=f'List[{element_type.name}]',
            subtypes={ListType(subtype) for subtype in element_type.subtypes},
        )
        self.element_type = element_type


class UnionType(PipelineDataType):
    def __init__(self, *args: 'PipelineDataType') -> None:
        if len(args) == 1:
            super().__init__(name=args[0].name, subtypes=args[0].subtypes)
        else:
            super().__init__(
                name=f'Union[{", ".join(type.name for type in args)}]', subtypes=args
            )


class AnyType(PipelineDataType):
    def __init__(self) -> None:
        super().__init__(name='Any', subtypes=set())

    def __eq__(self, other: 'PipelineDataType') -> bool:
        return isinstance(other, AnyType)

    def contains(self, other: 'PipelineDataType') -> bool:
        return True

    def is_subset(self, other: 'PipelineDataType') -> bool:
        return self == other


INT_TYPE = PipelineDataType('int')
FLOAT_TYPE = PipelineDataType('float', {INT_TYPE})

DOCUMENT_TYPE = PipelineDataType('document')
DICT_TYPE = PipelineDataType('dict', {DOCUMENT_TYPE})
URL_TYPE = PipelineDataType('url')
TEXT_TYPE = PipelineDataType('text', {FLOAT_TYPE, DICT_TYPE, URL_TYPE})

VECTOR_DB_TYPE = PipelineDataType('vector_db')

CSV_FILE_TYPE = PipelineDataType('csv_file')
TEXT_FILE_TYPE = PipelineDataType('text_file', {CSV_FILE_TYPE})
IMAGE_FILE_TYPE = PipelineDataType('image_file')
AUDIO_FILE_TYPE = PipelineDataType('audio_file')
FILE_TYPE = PipelineDataType('file', {TEXT_FILE_TYPE, IMAGE_FILE_TYPE, AUDIO_FILE_TYPE})
