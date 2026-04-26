"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .amcor import AmcorFetcher
from .ball import BallFetcher
from .berry import BerryFetcher
from .central_pet import CentralPetFetcher
from .cheng_loong import ChengLoongFetcher
from .chewy import ChewyFetcher
from .crown import CrownFetcher
from .elanco import ElancoFetcher
from .freshpet import FreshpetFetcher
from .graphic_pkg import GraphicPkgFetcher
from .idexx import IdexxFetcher
from .intl_paper import IntlPaperFetcher
from .petco import PetcoFetcher
from .pkg import PkgFetcher
from .rong_cheng import RongChengFetcher
from .sealed_air import SealedAirFetcher
from .smurfit import SmurfitFetcher
from .sonoco import SonocoFetcher
from .trupanion import TrupanionFetcher
from .zoetis import ZoetisFetcher

FETCHERS = {
    "amcor": AmcorFetcher,
    "ball": BallFetcher,
    "berry": BerryFetcher,
    "central_pet": CentralPetFetcher,
    "cheng_loong": ChengLoongFetcher,
    "chewy": ChewyFetcher,
    "crown": CrownFetcher,
    "elanco": ElancoFetcher,
    "freshpet": FreshpetFetcher,
    "graphic_pkg": GraphicPkgFetcher,
    "idexx": IdexxFetcher,
    "intl_paper": IntlPaperFetcher,
    "petco": PetcoFetcher,
    "pkg": PkgFetcher,
    "rong_cheng": RongChengFetcher,
    "sealed_air": SealedAirFetcher,
    "smurfit": SmurfitFetcher,
    "sonoco": SonocoFetcher,
    "trupanion": TrupanionFetcher,
    "zoetis": ZoetisFetcher,
}
