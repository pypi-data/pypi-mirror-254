from typing_extensions import TypedDict, TypeVar, Generic

LanguageCode = TypeVar("LanguageCode")


class LanguageDict(TypedDict, Generic[LanguageCode]):
    language: LanguageCode
    value: str


class PageDict(TypedDict):
    """Represents the dictionary that is stored as JSON in :attr:`pywikibot.ItemPage.text`."""

    type: str
    id: str
    labels: dict[str, LanguageDict[str]]  # Maybe autogenerate these in the future?
    descriptions: dict[
        str, LanguageDict[str]
    ]  # Maybe autogenerate these in the future?
    aliases: dict[
        str, list[LanguageDict[str]]
    ]  # Maybe autogenerate these in the future?
    claims: dict[str, list[dict[str, str]]]  # TODO: Expand upon these
    sitelinks: dict[str, dict[str, str]]  # TODO: Expand upon these
