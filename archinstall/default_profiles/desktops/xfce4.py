from typing import Any, TYPE_CHECKING

from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

if TYPE_CHECKING:
	_: Any


class Xfce4Profile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Xfce4', ProfileType.DesktopEnv, description='')

	@property
	def packages(self) -> list[str]:
		return [
			"xfce4",
			"xfce4-goodies",
			"pavucontrol",
			"gvfs",
			"xarchiver"
		]

	@property
	def default_greeter_type(self) -> GreeterType | None:
		return GreeterType.Lightdm
