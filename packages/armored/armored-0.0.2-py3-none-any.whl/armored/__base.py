from typing import (
    AbstractSet,
    Any,
    Union,
)

from pydantic import BaseModel, ConfigDict

AbstractSetOrDict = Union[
    AbstractSet[Union[int, str]],
    dict[Union[int, str], Any],
]


class __BaseModel(BaseModel):
    # This config allow to validate before assign new data to any field
    model_config = ConfigDict(
        validate_assignment=True,
        use_enum_values=True,
        populate_by_name=True,
    )


class BaseUpdatableModel(__BaseModel):
    """Base Model that was implemented updatable method and properties."""

    @classmethod
    def get_field_names(cls, alias=False):
        return list(cls.model_json_schema(alias).get("properties").keys())

    @classmethod
    def get_properties(cls) -> list:
        """Return list of properties of this model"""
        return [
            prop
            for prop in cls.__dict__
            if isinstance(cls.__dict__[prop], property)
        ]

    def dict(
        self,
        *,
        include: AbstractSetOrDict = None,
        exclude: AbstractSetOrDict = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """Override the dict function to include our properties
        docs: https://github.com/pydantic/pydantic/issues/935
        """
        attribs = super().model_dump(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            **kwargs,
        )
        props: list = self.get_properties()

        # Include and exclude properties
        if include:
            props: list = [prop for prop in props if prop in include]
        if exclude:
            props: list = [prop for prop in props if prop not in exclude]

        # Update the attribute dict with the properties
        if props:
            attribs.update({prop: getattr(self, prop) for prop in props})
        return attribs

    def update(self, data: dict):
        """Updatable method for update data to existing model data.
        docs: https://github.com/pydantic/pydantic/discussions/3139
        """
        update = self.dict()
        update.update(data)
        for k, v in (
            self.model_validate(update).dict(exclude_defaults=True).items()
        ):
            setattr(self, k, v)
        return self
