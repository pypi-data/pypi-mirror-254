from abc import ABC, abstractmethod
from typing import Iterator, Mapping, MutableMapping, Sequence, Union, overload

from pywikibot import (
    Claim,
    ItemPage,
    LexemePage,
    PropertyPage,
    WbTime,
    WbMonolingualText,
    WbGeoShape,
    WbQuantity,
    WbTabularData,
    WbUnknown,
    Coordinate,
)
import pywikibot.page._collections

from .dict_definition import PageDict

Page = Union[ItemPage, PropertyPage, LexemePage]
ClaimTargetValue = Union[
    ItemPage,
    PropertyPage,
    LexemePage,
    str,
    WbMonolingualText,
    WbGeoShape,
    WbQuantity,
    WbTabularData,
    WbUnknown,
    Coordinate,
    WbTime,
]


class AbstractItemContainer(ABC):
    """An abstract class representing the data in an item."""

    @overload
    def labels(self, language: None = None) -> MutableMapping[str, str]:
        ...

    @overload
    def labels(self, language: str) -> Union[str, None]:
        ...

    @abstractmethod
    def labels(self, language: Union[str, None] = None):
        """Get all labels for the item.

        :param language: The language to get the labels for. If None, all labels are returned.
        """

    def label_languages(self) -> list[str]:
        """Get all the languages that the item has labels in."""
        return list(self.labels().keys())

    @overload
    def descriptions(self, language: None = None) -> MutableMapping[str, str]:
        ...

    @overload
    def descriptions(self, language: str) -> Union[str, None]:
        ...

    @abstractmethod
    def descriptions(self, language: Union[str, None] = None):
        """Get all descriptions for the item.

        :param language: The language to get the descriptions for. If None, all descriptions are returned.
        """

    def description_languages(self) -> list[str]:
        """Get all the languages that the item has descriptions in."""
        return list(self.descriptions().keys())

    @overload
    def aliases(self, language: None = None) -> MutableMapping[str, list[str]]:
        ...

    @overload
    def aliases(self, language: str) -> list[str]:
        ...

    @abstractmethod
    def aliases(self, language: Union[str, None] = None):
        """Get all aliases for the item.

        :param language: The language to get the aliases for. If None, all aliases are returned.
        """

    def alias_languages(self) -> list[str]:
        """Get all the languages that the item has aliases in."""
        return list(self.aliases().keys())

    def alias_counts_by_language(self) -> dict[str, int]:
        """Get the number of aliases in each language."""
        return {k: len(v) for k, v in self.aliases().items()}

    @overload
    def all_titles(self, language: None = None) -> MutableMapping[str, list[str]]:
        ...

    @overload
    def all_titles(self, language: str) -> list[str]:
        ...

    def all_titles(self, language: Union[str, None] = None):
        """Get all titles for the item, with the label first.

        .. note:: An item can have no label and more than zero aliases, so there is no garuntee that the first item
            in the list is the label.
        """
        if language is not None:
            return (
                [self.labels(language)]
                if self.labels(language)
                else [] + self.aliases(language)
            )
        return {
            k: [self.labels(k)] if self.labels(k) else [] + v
            for k, v in self.aliases().items()
        }

    @overload
    def claims(self, property: None = None) -> Mapping[str, "MultiClaimContainer"]:
        ...

    @overload
    def claims(self, property: str) -> "MultiClaimContainer":
        ...

    @abstractmethod
    def claims(self, property: Union[str, None] = None):
        """Get all the claims for the item.

        :param property: The property to get the claims for. If None, all claims are returned.
        """


class ItemContainer(AbstractItemContainer):
    """A class representing the data in a :attr:`.Page` object."""

    def __init__(self, page: Page):
        self.page = page

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.page!r})"

    @overload
    def labels(self, language: None = None) -> MutableMapping[str, str]:
        ...

    @overload
    def labels(self, language: str) -> Union[str, None]:
        ...

    def labels(self, language: Union[str, None] = None):
        if language is not None:
            return self.page.labels.get(language, None)
        return self.page.labels

    @overload
    def descriptions(self, language: None = None) -> MutableMapping[str, str]:
        ...

    @overload
    def descriptions(self, language: str) -> Union[str, None]:
        ...

    def descriptions(self, language: Union[str, None] = None):
        if language is not None:
            return self.page.descriptions.get(language, None)
        return self.page.descriptions

    @overload
    def aliases(self, language: None = None) -> MutableMapping[str, list[str]]:
        ...

    @overload
    def aliases(self, language: str) -> list[str]:
        ...

    def aliases(self, language: Union[str, None] = None):
        if language is not None:
            return self.page.aliases.get(language, [])
        return self.page.aliases

    @overload
    def claims(self, property: None = None) -> Mapping[str, "MultiClaimContainer"]:
        ...

    @overload
    def claims(self, property: str) -> "MultiClaimContainer":
        ...

    def claims(self, property: Union[str, None] = None):
        if property is not None:
            val = self.page.claims.get(property, None)
            if val:
                return MultiClaimContainer(val)
            return MultiClaimContainer([])
        return {k: MultiClaimContainer(v) for k, v in self.page.claims.items()}


class DictItemContainer(AbstractItemContainer):
    def __init__(self, page_dict: PageDict, site=None):
        self.page_dict = page_dict
        site = site or pywikibot.Site("wikidata", "wikidata")
        self._claim_container = pywikibot.page._collections.ClaimCollection.fromJSON(
            page_dict["claims"], site
        )
        self.sitelinks = pywikibot.page._collections.SiteLinkCollection.fromJSON(
            page_dict["sitelinks"], site
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.page_dict!r})"

    @overload
    def labels(self, language: None = None) -> MutableMapping[str, str]:
        ...

    @overload
    def labels(self, language: str) -> Union[str, None]:
        ...

    def labels(self, language: Union[str, None] = None):
        if language is not None:
            return self.page_dict["labels"].get(language, None)
        return self.page_dict["labels"]

    @overload
    def descriptions(self, language: None = None) -> MutableMapping[str, str]:
        ...

    @overload
    def descriptions(self, language: str) -> Union[str, None]:
        ...

    def descriptions(self, language: Union[str, None] = None):
        if language is not None:
            return self.page_dict["descriptions"].get(language, None)
        return self.page_dict["descriptions"]

    @overload
    def aliases(self, language: None = None) -> MutableMapping[str, list[str]]:
        ...

    @overload
    def aliases(self, language: str) -> list[str]:
        ...

    def aliases(self, language: Union[str, None] = None):
        if language is not None:
            return self.page_dict["aliases"].get(language, [])
        return self.page_dict["aliases"]

    @overload
    def claims(self, property: None = None) -> Mapping[str, "MultiClaimContainer"]:
        ...

    @overload
    def claims(self, property: str) -> "MultiClaimContainer":
        ...

    def claims(self, property: Union[str, None] = None):
        if property is not None:
            val = self._claim_container.get(property, None)
            if val:
                return MultiClaimContainer(val)
            return MultiClaimContainer([])
        return {k: MultiClaimContainer(v) for k, v in self._claim_container.items()}


class ClaimMixin(ABC):
    @property
    @abstractmethod
    def claims(self) -> list[Claim]:
        ...


class SingleClaimContainer(ClaimMixin):
    def __init__(self, claim: Claim):
        self.claim = claim

    @property
    def value(self):
        return self.claim.getTarget()

    @property
    def claims(self) -> list[Claim]:
        return [self.claim]

    @overload
    def qualifiers(self, property: None = None) -> Mapping[str, "MultiClaimContainer"]:
        ...

    @overload
    def qualifiers(self, property: str) -> "MultiClaimContainer":
        ...

    def qualifiers(self, property: Union[str, None] = None):
        if property is not None:
            val = self.claim.qualifiers.get(property, None)
            if val:
                return MultiClaimContainer(val)
            return MultiClaimContainer([])
        return {k: MultiClaimContainer(v) for k, v in self.claim.qualifiers.items()}

    def references(self) -> "MultiReferenceContainer":
        return MultiReferenceContainer(self.claim.sources)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.claim!r})"


class SingleReferenceContainer:
    def __init__(self, reference_group: MutableMapping[str, list[Claim]]):
        self.reference_group = reference_group

    @overload
    def claims(self, property: None = None) -> Mapping[str, "MultiClaimContainer"]:
        ...

    @overload
    def claims(self, property: str) -> "MultiClaimContainer":
        ...

    def claims(self, property: Union[str, None] = None):
        if property is not None:
            val = self.reference_group.get(property, None)
            if val:
                return MultiClaimContainer(val)
            return MultiClaimContainer([])
        return {k: MultiClaimContainer(v) for k, v in self.reference_group.items()}

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.reference_group!r})"


class MultiReferenceContainer(Sequence[SingleReferenceContainer]):
    def __init__(self, reference_groups: list[MutableMapping[str, list[Claim]]]):
        self.reference_groups = reference_groups

    @overload
    def __getitem__(self, index: int) -> SingleReferenceContainer:
        ...

    @overload
    def __getitem__(self, index: slice) -> "MultiReferenceContainer":
        ...

    def __getitem__(self, index: Union[int, slice]):
        if isinstance(index, slice):
            return MultiReferenceContainer(self.reference_groups[index])
        return SingleReferenceContainer(self.reference_groups[index])

    def __len__(self) -> int:
        return len(self.reference_groups)

    def __iter__(self) -> Iterator[SingleReferenceContainer]:
        return map(SingleReferenceContainer, self.reference_groups)

    def first(self) -> Union[SingleReferenceContainer, None]:
        return (
            SingleReferenceContainer(self.reference_groups[0])
            if self.reference_groups
            else None
        )

    def last(self) -> Union[SingleReferenceContainer, None]:
        return (
            SingleReferenceContainer(self.reference_groups[-1])
            if self.reference_groups
            else None
        )

    @overload
    def claims(
        self, property: None = None
    ) -> list[Mapping[str, "MultiClaimContainer"]]:
        ...

    @overload
    def claims(self, property: str) -> "MultiReferenceClaimContainer":
        ...

    def claims(self, property: Union[str, None] = None):
        if property is not None:
            return MultiReferenceClaimContainer(
                [
                    SingleReferenceContainer(reference).claims(property)
                    for reference in self.reference_groups
                ]
            )
        return [
            SingleReferenceContainer(reference).claims()
            for reference in self.reference_groups
        ]

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.reference_groups!r})"


class MultiReferenceClaimContainer(list["MultiClaimContainer"]):
    def first_reference_claims(self) -> Union["MultiClaimContainer", None]:
        """Get all the claims of the first reference."""
        return self[0] if self else None

    def last_reference_claims(self) -> Union["MultiClaimContainer", None]:
        """Get all the claims of the last reference."""
        return self[-1] if self else None

    def first(self) -> list[Union[SingleClaimContainer, None]]:
        """Get the first claim of each claim in the list of claims."""
        return [claim.first() for claim in self]

    def last(self) -> list[Union[SingleClaimContainer, None]]:
        """Get the last claim of each claim in the list of claims."""
        return [claim.last() for claim in self]

    def to_claims(self) -> list[list[Claim]]:
        """Convert the MultiReferenceClaimContainer to a list of lists of claims."""
        return [reference.claims for reference in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({super().__repr__()})"


class MultiClaimContainer(ClaimMixin, Sequence[SingleClaimContainer]):
    def __init__(self, claim_list: list[Claim]):
        self.claim_list = claim_list

    @property
    def claims(self) -> list[Claim]:
        return self.claim_list

    @overload
    def __getitem__(self, index: int) -> SingleClaimContainer:
        ...

    @overload
    def __getitem__(self, index: slice) -> "MultiClaimContainer":
        ...

    def __getitem__(self, index: Union[int, slice]):
        if isinstance(index, slice):
            return MultiClaimContainer(self.claim_list[index])
        return SingleClaimContainer(self.claim_list[index])

    def __len__(self) -> int:
        return len(self.claims)

    def __iter__(self) -> Iterator[SingleClaimContainer]:
        return map(SingleClaimContainer, self.claims)

    @property
    def values(self) -> list[ClaimTargetValue]:
        return [claim.getTarget() for claim in self.claims]

    def first(self) -> Union[SingleClaimContainer, None]:
        return SingleClaimContainer(self.claims[0]) if self.claims else None

    def last(self) -> Union[SingleClaimContainer, None]:
        return SingleClaimContainer(self.claims[-1]) if self.claims else None

    @overload
    def qualifiers(
        self, property: None = None
    ) -> list[Mapping[str, "MultiClaimContainer"]]:
        ...

    @overload
    def qualifiers(self, property: str) -> "MultiClaimQualifierContainer":
        ...

    def qualifiers(self, property: Union[str, None] = None):
        if property is not None:
            return MultiClaimQualifierContainer(
                [
                    SingleClaimContainer(claim).qualifiers(property)
                    for claim in self.claims
                ]
            )
        return [SingleClaimContainer(claim).qualifiers() for claim in self.claims]

    def references(self) -> "MultiClaimMultiReferenceContainer":
        return MultiClaimMultiReferenceContainer(
            [SingleClaimContainer(claim).references() for claim in self.claims]
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.claims!r})"


class MultiClaimQualifierContainer(list[MultiClaimContainer]):
    def first_claim_qualifiers(self) -> Union[MultiClaimContainer, None]:
        """Get the qualifiers of the first claim in the list of claims."""
        return self[0] if self else None

    def last_claim_qualifiers(self) -> Union[MultiClaimContainer, None]:
        """Get the qualifiers of the last claim in the list of claims."""
        return self[-1] if self else None

    def first(self) -> list[Union[SingleClaimContainer, None]]:
        """Get the first qualifier of each claim in the list of claims."""
        return [claim.first() for claim in self]

    def last(self) -> list[Union[SingleClaimContainer, None]]:
        """Get the last qualifier of each claim in the list of claims."""
        return [claim.last() for claim in self]

    def to_claims(self) -> list[list[Claim]]:
        """Convert the MultiClaimQualifierContainer to a list of lists of claims."""
        return [claim.claims for claim in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({super().__repr__()})"


class MultiClaimMultiReferenceContainer(list[MultiReferenceContainer]):
    def first_claim_references(self) -> Union[MultiReferenceContainer, None]:
        """Get the references of the first claim in the list of claims."""
        return self[0] if self else None

    def last_claim_references(self) -> Union[MultiReferenceContainer, None]:
        """Get the references of the last claim in the list of claims."""
        return self[-1] if self else None

    def first(self) -> list[Union[SingleReferenceContainer, None]]:
        """Get the first reference of each claim in the list of claims."""
        return [claim.first() for claim in self]

    def last(self) -> list[Union[SingleReferenceContainer, None]]:
        """Get the last reference of each claim in the list of claims."""
        return [claim.last() for claim in self]

    @overload
    def claims(
        self, property: None = None
    ) -> list[list[Mapping[str, "MultiClaimContainer"]]]:
        ...

    @overload
    def claims(self, property: str) -> "MultiClaimMultiReferenceClaimContainer":
        ...

    def claims(self, property: Union[str, None] = None):
        if property is not None:
            return MultiClaimMultiReferenceClaimContainer(
                [claim.claims(property) for claim in self]
            )
        return [reference.claims() for reference in self]

    def to_reference_groups(self) -> list[list[MutableMapping[str, list[Claim]]]]:
        """Convert the MultiClaimMultiReferenceContainer to a list of reference groups."""
        return [reference.reference_groups for reference in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({super().__repr__()})"


class MultiClaimMultiReferenceClaimContainer(list[MultiReferenceClaimContainer]):
    def first_claim_references_claims(
        self,
    ) -> Union[MultiReferenceClaimContainer, None]:
        """Get the claims of the first reference of the first claim in the list of claims."""
        return self[0] if self else None

    def last_claim_references_claims(self) -> Union[MultiReferenceClaimContainer, None]:
        """Get the claims of the last reference of the last claim in the list of claims."""
        return self[-1] if self else None

    def first(self) -> list[list[Union[SingleClaimContainer, None]]]:
        """Get the first claim of each reference of each claim in the list of claims."""
        return [claim.first() for claim in self]

    def last(self) -> list[list[Union[SingleClaimContainer, None]]]:
        """Get the last claim of each reference of each claim in the list of claims."""
        return [claim.last() for claim in self]

    def to_claims(self) -> list[list[list[Claim]]]:
        """Convert the MultiClaimMultiReferenceClaimContainer to a list of lists of lists of claims."""
        return [reference.to_claims() for reference in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"
