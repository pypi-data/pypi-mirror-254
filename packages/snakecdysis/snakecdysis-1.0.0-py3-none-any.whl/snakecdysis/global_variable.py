from pathlib import Path

__dict_context_settings = dict(ignore_unknown_options=True, max_content_width=800, help_option_names=('-h', '--help'))

GIT_URL =  "https://forge.ird.fr/phim/sravel/snakecdysis"

pkg_templates_path = Path(__file__).resolve().parent.joinpath("templates")
