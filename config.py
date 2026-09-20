import os
import sys
from pathlib import Path

class Config:
    # Application Identity (Authentic Indian Army & Defence Platform)
    APP_NAME = "TRINETRA"
    APP_TAGLINE = "Indian Army AI Surveillance & Digital Evidence Platform"
    SYSTEM_TITLE = "TRINETRA — Indian Army Border Surveillance & Evidence Vault"
    CLASSIFICATION_LABEL = "RESTRICTED // FOR OFFICIAL INDIAN DEFENCE USE ONLY"
    PROBLEM_STATEMENT_ID = "SIH26187"
    THEME = "Blockchain & Cybersecurity"
    DEFENCE_MOTTO = "SEVA ASMAKAM DHARMA • SERVICE BEFORE SELF"
    DEFENCE_CORPS = "HQ 16 CORPS • WHITE KNIGHT CORPS"
    DEFENCE_FORMATION = "26 INFANTRY DIVISION / SAMBA BRIGADE"
    OPERATION_CODE = "OP SARD HAWA (PHASE IV SURVEILLANCE PROTOCOL)"
    
    # Deployment / Sector Metadata
    SECTOR_ID = "BOP-ALPHA-04"
    SECTOR_NAME = "HQ 16 Corps • BOP Samba Outpost (IB/LC Sector)"
    COORDINATES = "32.7266° N, 75.1157° E (MGRS: 43S XU 8219 4432)"
    ELEVATION = "384m AMSL"

    # Base Paths (Supports standalone executable packaging)
    if getattr(sys, "frozen", False):
        BASE_DIR = Path(sys.executable).resolve().parent
    else:
        BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "data"
    VIDEOS_DIR = DATA_DIR / "videos"
    EVIDENCE_DIR = DATA_DIR / "evidence"
    THUMBNAILS_DIR = DATA_DIR / "thumbnails"
    REPORTS_DIR = DATA_DIR / "reports"
    DATABASE_DIR = DATA_DIR / "database"
    LOGS_DIR = DATA_DIR / "logs"
    MODELS_DIR = BASE_DIR / "models"
    AUTHORIZED_FACES_DIR = DATA_DIR / "authorized_faces"
    
    # Database
    DB_PATH = DATABASE_DIR / "trinetra.db"
    
    # Blockchain / Ledger
    LEDGER_PATH = DATA_DIR / "blockchain" / "local_ledger.json"
    FABRIC_ENABLED = False  # Set True when connected to real Hyperledger Fabric peer
    
    # Cryptography
    KEYS_DIR = DATA_DIR / "keys"
    PRIVATE_KEY_PATH = KEYS_DIR / "ed25519_private.pem"
    PUBLIC_KEY_PATH = KEYS_DIR / "ed25519_public.pem"
    
    # AI & Neuromorphic Processing
    IMAGE_SIZE = 224
    NUM_FRAMES = 16          # 16-frame temporal buffer
    PATCH_SIZE = 16
    EMBED_DIM = 192
    LIF_TAU = 2.0            # Leaky Integrate-and-Fire membrane time constant
    CONFIDENCE_THRESHOLD = 0.65
    RISK_THRESHOLD = "MEDIUM"
    
    # Evidence Clipping Specification
    PRE_EVENT_SECONDS = 3.0  # Seconds before detection
    POST_EVENT_SECONDS = 3.0 # Seconds after detection
    DEFAULT_CLIP_FPS = 15.0
    
    # Indian Army Tactical Threat Taxonomy
    THREAT_CLASSES = [
        "NORMAL",
        "PERIMETER BREACH / INFILTRATION",
        "TERRAIN & NULLAH INGRESSION",
        "HOSTILE DRONE / UAV RECON",
        "LINE OF CONTROL (LC) CROSSING",
        "SUSPICIOUS GROUP CONVERGENCE",
        "HOSTILE RECON LOITERING",
        "UNAUTHORIZED VEHICLE MOVEMENT"
    ]
    
    # Threat Risk Level Map
    THREAT_RISK_MAP = {
        "NORMAL": "LOW",
        "HOSTILE RECON LOITERING": "MEDIUM",
        "TERRAIN & NULLAH INGRESSION": "HIGH",
        "SUSPICIOUS GROUP CONVERGENCE": "HIGH",
        "LINE OF CONTROL (LC) CROSSING": "CRITICAL",
        "UNAUTHORIZED VEHICLE MOVEMENT": "HIGH",
        "PERIMETER BREACH / INFILTRATION": "CRITICAL",
        "HOSTILE DRONE / UAV RECON": "CRITICAL"
    }

    # Incident Lifecycles
    INCIDENT_STATUSES = [
        "DETECTED",
        "VALIDATING",
        "CONFIRMED",
        "ALERTED",
        "ACKNOWLEDGED",
        "RESPONDING",
        "RESOLVED",
        "ARCHIVED"
    ]

    # Offline / Network Fail-safe
    OFFLINE_MODE = False
    
    # Dual Theme Modes: Tactical Night Ops (Dark) vs Command HQ Day Ops (Light)
    THEME_MODE = "dark"
    
    # Theme Palettes
    PALETTES = {
        "dark": {
            "COLOR_BG": "#0c100d",            # Deep Olive-Charcoal Canvas
            "COLOR_SURFACE": "#141a15",       # Olive-Slate Card / Panel Container
            "COLOR_SURFACE_LIGHT": "#1e261f", # Elevated Surface / Card Hover
            "COLOR_BORDER": "#2d3b2f",        # Mil-Spec Subdued Olive Border
            "COLOR_BORDER_LIGHT": "#405443",  # Highlighted Border
            "COLOR_PRIMARY": "#eab308",       # Indian Army Brass Gold
            "COLOR_PRIMARY_HOVER": "#ca8a04", # Darker Brass Gold
            "COLOR_PRIMARY_MUTED": "#713f12", # Subtle Gold/Bronze Fill
            "COLOR_TEXT_MAIN": "#f3f4f6",     # Stencil Off-White
            "COLOR_TEXT_MUTED": "#9aa89d",    # Sage / Muted Olive Gray
            "COLOR_TEXT_DIM": "#64746b",      # Dim Military Slate
            "COLOR_SUCCESS": "#22c55e",       # Tactical Green
            "COLOR_WARNING": "#f59e0b",       # Caution Amber
            "COLOR_CRITICAL": "#ef4444",      # Breach Red
            "COLOR_INFO": "#38bdf8",          # Telemetry Cyan
            "COLOR_ARMY_GREEN": "#38a169",    # Olive Green Accent
        },
        "light": {
            "COLOR_BG": "#f8fafc",            # Ultra-crisp bright clean canvas (Light Slate White)
            "COLOR_SURFACE": "#ffffff",       # Pure Crisp White Surface Card
            "COLOR_SURFACE_LIGHT": "#f1f5f9", # Subtle elevated card / button hover
            "COLOR_BORDER": "#e2e8f0",        # Crisp light border
            "COLOR_BORDER_LIGHT": "#cbd5e1",  # Active crisp border
            "COLOR_PRIMARY": "#15803d",       # Eye-Catchy Indian Army Forest Green
            "COLOR_PRIMARY_HOVER": "#166534", # Darker Emerald Hover
            "COLOR_PRIMARY_MUTED": "#dcfce7", # Vibrant Soft Mint/Sage Tint
            "COLOR_TEXT_MAIN": "#0f172a",     # High-Contrast Deep Slate Text (Never dull black)
            "COLOR_TEXT_MUTED": "#475569",    # Medium Slate Text
            "COLOR_TEXT_DIM": "#64748b",      # Dim Military Metadata Text
            "COLOR_SUCCESS": "#16a34a",       # Vibrant Field Green
            "COLOR_WARNING": "#d97706",       # Vibrant Warm Amber / Gold
            "COLOR_CRITICAL": "#dc2626",      # Tactical Breach Alert Red
            "COLOR_INFO": "#0284c7",          # Telemetry Blue
            "COLOR_ARMY_GREEN": "#15803d",    # Vibrant Indian Army Green
        }
    }
    
    # Active Color Tokens (Default to Dark / Tactical Night Ops)
    COLOR_BG = PALETTES["dark"]["COLOR_BG"]
    COLOR_SURFACE = PALETTES["dark"]["COLOR_SURFACE"]
    COLOR_SURFACE_LIGHT = PALETTES["dark"]["COLOR_SURFACE_LIGHT"]
    COLOR_BORDER = PALETTES["dark"]["COLOR_BORDER"]
    COLOR_BORDER_LIGHT = PALETTES["dark"]["COLOR_BORDER_LIGHT"]
    COLOR_PRIMARY = PALETTES["dark"]["COLOR_PRIMARY"]
    COLOR_PRIMARY_HOVER = PALETTES["dark"]["COLOR_PRIMARY_HOVER"]
    COLOR_PRIMARY_MUTED = PALETTES["dark"]["COLOR_PRIMARY_MUTED"]
    COLOR_TEXT_MAIN = PALETTES["dark"]["COLOR_TEXT_MAIN"]
    COLOR_TEXT_MUTED = PALETTES["dark"]["COLOR_TEXT_MUTED"]
    COLOR_TEXT_DIM = PALETTES["dark"]["COLOR_TEXT_DIM"]
    COLOR_SUCCESS = PALETTES["dark"]["COLOR_SUCCESS"]
    COLOR_WARNING = PALETTES["dark"]["COLOR_WARNING"]
    COLOR_CRITICAL = PALETTES["dark"]["COLOR_CRITICAL"]
    COLOR_INFO = PALETTES["dark"]["COLOR_INFO"]
    COLOR_ARMY_GREEN = PALETTES["dark"]["COLOR_ARMY_GREEN"]

    @classmethod
    def apply_theme(cls, mode: str):
        """Updates active class-level color properties according to selected mode ('dark' or 'light')."""
        if mode not in cls.PALETTES:
            mode = "dark"
        cls.THEME_MODE = mode
        palette = cls.PALETTES[mode]
        for key, val in palette.items():
            setattr(cls, key, val)
    
    # User Roles
    ROLE_ADMIN = "Administrator"
    ROLE_OFFICER = "Security Officer"
    ROLE_ANALYST = "Analyst"
    ROLE_VIEWER = "Viewer"
    
    @classmethod
    def initialize_directories(cls):
        """Ensures all operational data directories exist."""
        for p in [
            cls.DATA_DIR,
            cls.VIDEOS_DIR,
            cls.EVIDENCE_DIR,
            cls.THUMBNAILS_DIR,
            cls.REPORTS_DIR,
            cls.DATABASE_DIR,
            cls.LOGS_DIR,
            cls.MODELS_DIR,
            cls.KEYS_DIR,
            cls.AUTHORIZED_FACES_DIR,
            cls.DATA_DIR / "blockchain"
        ]:
            p.mkdir(parents=True, exist_ok=True)

# Run initialization on import
Config.initialize_directories()
