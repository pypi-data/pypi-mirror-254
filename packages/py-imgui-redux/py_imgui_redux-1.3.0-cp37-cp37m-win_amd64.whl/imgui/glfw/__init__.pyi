"""GLFW Backend Wrapper"""
from __future__ import annotations
import imgui.glfw
import typing
import imgui

__all__ = [
    "Init",
    "InitContextForGLFW",
    "NewFrame",
    "Render",
    "ShouldClose",
    "Shutdown"
]


def Init(title: str, window_width: int = 0, window_height: int = 0, swap_interval: int = 1) -> capsule:
    pass
def InitContextForGLFW(window: capsule) -> None:
    pass
def NewFrame() -> None:
    pass
def Render(window: capsule, clear_color: imgui.Vec4) -> None:
    pass
def ShouldClose(window: capsule) -> bool:
    pass
def Shutdown(window: capsule) -> None:
    pass
