from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

from atoti_core import keyword_only_dataclass

from ._config import Config, convert_path_to_absolute_string


@keyword_only_dataclass
@dataclass(frozen=True)
class I18nConfig(Config):
    """The internationalization configuration.

    Note:
        This feature is not part of the community edition: it needs to be `unlocked <../../how_tos/unlock_all_features.html>`__.

    Example:
        >>> config = tt.I18nConfig(
        ...     default_locale="fr-FR", translations="../translations"
        ... )

    """

    default_locale: Optional[str] = None
    """The default locale to use for internationalizing the session."""

    translations: Optional[Union[Path, str]] = None
    """The directory from which translation files will be loaded.

    This directory should contain a list of files named after their corresponding locale (e.g. ``en-US.json`` for US translations).
    The application will behave differently depending on how :func:`atoti.Session`'s *user_content_storage*  parameter is configured:

    * If *user_content_storage* is a path to a file:

      * If a value is specified for *translations*, those files will be uploaded to the local content storage, overriding any previously defined translations.
      * If no value is specified for *translations*, the default translations for Atoti will be uploaded to the local user content storage.

    * If a remote user content storage has been configured:

      * If a value is specified for *translations*, this data will be pushed to the remote user content storage, overriding any previously existing values.
      * If no value has been specified for *translations* and translations exist in the remote user content storage, those values will be loaded into the session.
      * If no value has been specified for *translations* and no translations exist in the remote user content storage, the default translations for Atoti will be uploaded to the remote user content storage.

    """

    def __post_init__(self) -> None:
        convert_path_to_absolute_string(self, "translations")
