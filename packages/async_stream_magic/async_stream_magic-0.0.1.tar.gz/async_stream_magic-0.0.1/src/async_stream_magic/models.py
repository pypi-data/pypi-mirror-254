"""Asynchronous Python client for StreamMagic Devices."""
from pydantic import BaseModel, Field

class Info(BaseModel):
    """Object holding the StreamMagic device information."""
    
    name: str = Field(..., alias="name")
    model: str = Field(..., alias="model")
    timezone: str = Field(..., alias="timezone")
    locale: str = Field(..., alias="locale")
    udn: str = Field(..., alias="udn")
    unit_id: str = Field(..., alias="unit_id")
    api_version: str = Field(..., alias="api")

class Source(BaseModel):
    """Object holding the aviable StreamMagic device sources."""

    id: str = Field(..., alias="id"),
    name: str = Field(..., alias="name"),
    default_name: str = Field(..., alias="default_name"),
    #class_name: str = Field(..., alias="class"),
    nameable: bool = Field(..., alias="nameable"),
    ui_selectable: bool = Field(..., alias="ui_selectable"),
    description: str = Field(..., alias="description"),
    description_locale: str = Field(..., alias="description_locale"),
    preferred_order: int = Field(..., alias="preferred_order"),

class State(BaseModel):
    """Object holding the State of StreamMagic device."""

    zone: str = Field(..., alias="zone"),
    source: str = Field(..., alias="id"),
    power: bool = Field(..., alias="power"),
    pre_amp_mode: bool = Field(..., alias="pre_amp_mode"),
    pre_amp_state: bool = Field(..., alias="pre_amp_state"),
    mute: bool = Field(..., alias="mute"),
    volume_step: int = Field(..., alias="volume_step"),
    volume_percent: int = Field(..., alias="volume_percent"),
    volume_db: int = Field(..., alias="volume_db"),