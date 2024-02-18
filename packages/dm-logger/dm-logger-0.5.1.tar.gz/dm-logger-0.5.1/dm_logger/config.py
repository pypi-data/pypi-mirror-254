from typing import Literal, Union


class Config:
    logs_dir_path: str = "logs"
    file_name: str = "main.log"
    write_mode: Literal["a", "w"] = "w"
    max_MB: int = 5
    max_count: int = 10
    show_name_label: bool = True
    show_location_label: Union[bool, Literal["auto"]] = "auto"
    format_string: str = None
