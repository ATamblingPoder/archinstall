from typing import Any, TYPE_CHECKING

from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

if TYPE_CHECKING:
	_: Any


class I3wmProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('i3-wm', ProfileType.WindowMgr, description='')

	@property
	def packages(self) -> list[str]:
		return [
			'i3-wm',
			'i3lock',
			'i3status',
			'i3blocks',
			'xss-lock',
			'xterm',
			'lightdm-gtk-greeter',
			'lightdm',
			'dmenu'
		]

	@property
	def default_greeter_type(self) -> GreeterType | None:
		return GreeterType.Lightdm
