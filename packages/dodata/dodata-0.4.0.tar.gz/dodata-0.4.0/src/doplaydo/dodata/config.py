"""SDK Configuration."""
import pathlib
from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from sqlalchemy.engine import URL
import os
import multiprocessing


class Path:
    """Paths."""

    module = pathlib.Path(__file__).parent.resolve()
    analysis_functions = module / "analysis_functions"

    analysis_functions_device = analysis_functions / "device_data"
    analysis_functions_die = analysis_functions / "die"
    analysis_functions_wafer = analysis_functions / "wafer"

    # Device
    analysis_functions_device_iv_resistance = (
        analysis_functions_device / "iv_resistance.py"
    )
    analysis_functions_device_fsr = analysis_functions_device / "fsr.py"
    analysis_functions_device_power_envelope = (
        analysis_functions_device / "power_envelope.py"
    )

    # Die
    analysis_functions_die_sheet_resistance = (
        analysis_functions_die / "iv_sheet_resistance.py"
    )
    analysis_functions_die_loss_cutback = analysis_functions_die / "loss_cutback.py"
    analysis_functions_die_cutback = analysis_functions_die / "cutback.py"
    analysis_functions_die_aggregate = analysis_functions_die / "aggregate.py"

    # Wafer
    analysis_functions_wafer_loss_cutback = (
        analysis_functions_wafer / "aggregate_loss_cutback.py"
    )
    analysis_functions_wafer_device_data_id = (
        analysis_functions_wafer / "aggregate_device_data_id.py"
    )
    analysis_functions_wafer_device_data = (
        analysis_functions_wafer / "aggregate_device_data.py"
    )


def get_affinity() -> int:
    """Get number of cores/threads available.

    On (most) linux we can get it through the scheduling affinity. Otherwise,
    fall back to the multiprocessing cpu count.
    """
    try:
        threads = len(os.sched_getaffinity(0))
    except AttributeError:
        threads = multiprocessing.cpu_count()
    return threads


dotenv_path = find_dotenv(usecwd=True)


class Config(BaseSettings):  # noqa: D101
    model_config = SettingsConfigDict(env_file=dotenv_path, extra="ignore")

    dodata_url: str
    dodata_user: str
    dodata_password: str
    dodata_db: str
    dodata_db_user: str
    dodata_db_password: str
    dodata_db_name: str = "dodata"
    dodata_db_port: int = 5432
    debug: bool = False
    n_threads: int = get_affinity() // 3 or 1
    n_cores: int = get_affinity() // 2 or 1
    ssl_verify: bool = True

    @property
    def dodata_db_connection_url(self) -> URL:
        """Calculates the connection URI."""
        if "sqlite" in self.dodata_db:
            # For SQLite, the URL should be directly returned if correctly formatted
            # 'sqlite:///' for file-based and 'sqlite:///:memory:' for in-memory
            if self.dodata_db.startswith("sqlite:///"):
                return URL.create(
                    drivername="sqlite",
                    database=self.dodata_db.removeprefix("sqlite:///"),
                )
            elif self.dodata_db == ":memory:":
                return URL.create(drivername="sqlite", database=self.dodata_db)
            else:
                # Handle cases where the SQLite URL might not be in the standard format
                return URL.create(drivername="sqlite", database=self.dodata_db)

        else:
            # For other databases like PostgreSQL
            return URL.create(
                drivername="postgresql+psycopg2",
                username=self.dodata_db_user,
                password=self.dodata_db_password,
                host=self.dodata_db,
                port=self.dodata_db_port,
                database=self.dodata_db_name,
            )


@lru_cache
def get_settings() -> Config:
    """The one and only settings."""
    return Config()
