import streamlit as st
from chart_provider_definitions import chart_providers

def get_chart_embed(symbol: str, selected_provider: str = "TradingView") -> str:
    symbol = symbol.upper()

    for provider in chart_providers:
        if provider["name"] == selected_provider:
            if provider["type"] == "iframe":
                return provider["embed_template"](symbol)
            elif provider["type"] == "img":
                return provider["embed_template"](symbol)
            elif provider["type"] == "native":
                return None
    return None

def is_native_chart(provider_name: str) -> bool:
    for p in chart_providers:
        if p["name"] == provider_name:
            return p["type"] == "native"
    return False

def provider_supports_overlay(provider_name: str) -> bool:
    for p in chart_providers:
        if p["name"] == provider_name:
            return p.get("supports_overlay", False)
    return False

def provider_supported_assets(provider_name: str):
    for p in chart_providers:
        if p["name"] == provider_name:
            return p.get("asset_classes", [])
    return ["all"]
