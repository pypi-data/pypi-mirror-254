from pydantic import BaseModel


class DataSettings(BaseModel):
    """
        Dataclass of settings for STEAM analyses
        This will be populated either form a local settings file (if flag_permanent_settings=False)
        or from the keys in the input analysis file (if flag_permanent_settings=True)
    """
    comsolexe_path:        str = None  # full path to comsol.exe, only COMSOL53a is supported
    JAVA_jdk_path:         str = None  # full path to folder with java jdk
    CFunLibPath:           str = None  # full path to dll files with material properties