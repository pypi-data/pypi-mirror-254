import jsonobject
from datetime import datetime
from typing import TypedDict, Literal, Optional

from .shared import valid_per_page, positive_num, valid_hash, instruments, difficulties


__all__ = [
    "SearchFilter",
    "BasicSearch",
    "BasicSearchOpts",
    "AdvancedSearch",
    "AdvancedSearchOpts",
]


class BasicSearch(jsonobject.JsonObject):
    """
    A class representing a basic search query, using `jsonobject.JsonObject`.
    This class is used to define and validate the structure of a search request.

    Attributes:
        search (str): A string property to specify the search query term.
        per_page (int): An optional integer property specifying the number of results
                        to return per page. It must be between 1 and 250 inclusively.
                        If not specified it will default to 2.
        page (int): An integer property specifying the current page number of the search
                    results, with a default value of 1.
        instrument (str): A string property specifying the instrument for the search.
                          It must be one of the predefined choices in `instruments`.
        difficulty (str): A string property specifying the difficulty level of the music
                          pieces to search for. It must be easy, medium, hard, export, or None.
                          None represents any difficulty
    """

    search = jsonobject.StringProperty(name="search", required=True)
    per_page = jsonobject.IntegerProperty(
        name="per_page", validators=valid_per_page, required=False, exclude_if_none=True, default=20
    )
    page = jsonobject.IntegerProperty(name="page", validators=positive_num, default=1, required=True)
    instrument = jsonobject.StringProperty(
        name="instrument", choices=instruments, exclude_if_none=False, default=None
    )
    difficulty = jsonobject.StringProperty(
        name="difficulty", choices=difficulties, exclude_if_none=False, default=None
    )


class SearchFilter(jsonobject.JsonObject):
    """
    Represents a search filter for artist, album, year, genre, charter, etc, allowing
    for more nuanced search queries.

    Attributes:
        value (str): The string value to search for. Defaults to an empty string if not provided.
        exact (bool): Specifies whether the search should match the value exactly. Defaults to False,
                      indicating that partial matches are acceptable.
        exclude (bool): Indicates whether the search results should exclude items matching the value.
                        Defaults to False, meaning items matching the value are included in the results.
    """

    value = jsonobject.StringProperty(name="value", default="")
    exact = jsonobject.BooleanProperty(name="exact", default=False)
    exclude = jsonobject.BooleanProperty(name="exclude", default=False)

    def __repr__(self) -> str:
        return f'{self.value} <exact: {self.exact}, exclude: {self.exclude}>'


class AdvancedSearch(jsonobject.JsonObject):
    """
    Represents an advanced search query, using `jsonobject.JsonObject` for JSON serialization.
    This class allows for detailed search criteria across various music-related attributes.

    Attributes:
        instrument (str): Filter by musical instrument type. Must be one of the predefined choices.
        page (int): The page number for pagination, starting from 1.
        difficulty (str): Filter by difficulty level. Must be one of the predefined choices.
        name (SearchFilter): A filter object for searching by name.
        artist (SearchFilter): A filter object for searching by artist.
        album (SearchFilter): A filter object for searching by album.
        genre (SearchFilter): A filter object for searching by genre.
        year (SearchFilter): A filter object for searching by year.
        charter (SearchFilter): A filter object for searching by charter.
        min_length (int): Minimum length of the song in seconds.
        max_length (int): Maximum length of the song in seconds.
        min_intensity (int): Minimum intensity of the song.
        max_intensity (int): Maximum intensity of the song.
        min_average_nps (int): Minimum average notes per second.
        max_average_nps (int): Maximum average notes per second.
        min_max_nps (int): Minimum peak notes per second.
        max_max_nps (int): Maximum peak notes per second.
        hash (str): Filter by MD5 hash of the song file.
        chart_hash (str): Filter by MD5 hash of the chart file.
        modified_after (date): Filter for charts modified after the specified date.
        has_solo_sections (bool): Filter for charts with solo sections.
        has_forced_notes (bool): Filter for charts with forced notes.
        has_open_notes (bool): Filter for charts with open notes.
        has_tap_notes (bool): Filter for charts with tap notes.
        has_lyrics (bool): Filter for charts with lyrics.
        has_vocals (bool): Filter for charts with vocals.
        has_roll_lanes (bool): Filter for charts with roll lanes.
        has_2x_kick (bool): Filter for charts with double kick pedals.
        has_issues (bool): Filter for charts flagged with issues.
        has_video_background (bool): Filter for charts with video backgrounds.
        modchart (bool): Filter for charts with modcharts (custom game mechanics).
        chart_id_after (int): Filter for charts with IDs greater than the specified value.
    """

    instrument = jsonobject.StringProperty(
        name="instrument", choices=instruments, exclude_if_none=False
    )
    page = jsonobject.IntegerProperty(name="page", validators=positive_num, default=1)
    difficulty = jsonobject.StringProperty(
        name="difficulty", choices=difficulties, exclude_if_none=False
    )
    name = jsonobject.ObjectProperty(lambda: SearchFilter, name="name")
    artist = jsonobject.ObjectProperty(lambda: SearchFilter, name="artist")
    album = jsonobject.ObjectProperty(lambda: SearchFilter, name="album")
    genre = jsonobject.ObjectProperty(lambda: SearchFilter, name="genre")
    year = jsonobject.ObjectProperty(lambda: SearchFilter, name="year")
    charter = jsonobject.ObjectProperty(lambda: SearchFilter, name="charter")
    min_length = jsonobject.IntegerProperty(name="minLength", validators=positive_num)
    max_length = jsonobject.IntegerProperty(name="maxLength", validators=positive_num)
    min_intensity = jsonobject.IntegerProperty(
        name="minIntensity", validators=positive_num
    )
    max_intensity = jsonobject.IntegerProperty(
        name="maxIntensity", validators=positive_num
    )
    min_average_nps = jsonobject.IntegerProperty(
        name="minAverageNPS", validators=positive_num
    )
    max_average_nps = jsonobject.IntegerProperty(
        name="maxAverageNPS", validators=positive_num
    )
    min_max_nps = jsonobject.IntegerProperty(name="minMaxNPS", validators=positive_num)
    max_max_nps = jsonobject.IntegerProperty(name="maxMaxNPS", validators=positive_num)
    hash = jsonobject.StringProperty(name="hash", validators=valid_hash)
    chart_hash = jsonobject.StringProperty(name="chartHash", validators=valid_hash)
    modified_after = jsonobject.DateProperty(name="modifiedAfter")
    has_solo_sections = jsonobject.BooleanProperty(name="hasSoloSections")
    has_forced_notes = jsonobject.BooleanProperty(name="hasForcedNotes")
    has_open_notes = jsonobject.BooleanProperty(name="hasOpenNotes")
    has_tap_notes = jsonobject.BooleanProperty(name="hasTapNotes")
    has_lyrics = jsonobject.BooleanProperty(name="hasLyrics")
    has_vocals = jsonobject.BooleanProperty(name="hasVocals")
    has_roll_lanes = jsonobject.BooleanProperty(name="hasRollLanes")
    has_2x_kick = jsonobject.BooleanProperty(name="has2xKick")
    has_issues = jsonobject.BooleanProperty(name="hasIssues")
    has_video_background = jsonobject.BooleanProperty(name="hasVideoBackground")
    modchart = jsonobject.BooleanProperty(name="modchart")
    chart_id_after = jsonobject.IntegerProperty(
        name="chartIdAfter", validators=positive_num, exclude_if_none=True
    )

    def __repr__(self) -> str:
        tmp = []
        for k, v in self.items():
            if v is None:
                   tmp.append(f'{k}=any') 
            elif isinstance(v, SearchFilter):
                if v.value:
                    tmp.append(f'{k}={repr(v)}')
            else:
                tmp.append(f'{k}={v}')
        return f'AdvancedSearch({", ".join(tmp)})'


class BasicSearchOpts(TypedDict):
    search: str
    per_page: Optional[int]
    page: Optional[int]
    instrument: Optional[
        Literal[
            "guitar",
            "guitarcoop",
            "rhythm",
            "bass",
            "drums",
            "keys",
            "guitarghl",
            "guitarcoopghl",
            "rhythmghl",
            "bassghl",
            None,
        ]
    ]
    difficulty: Optional[Literal["expert", "hard", "medium", "easy", None]]


class AdvancedSearchOpts(TypedDict):
    instrument: Optional[
        Literal[
            "guitar",
            "guitarcoop",
            "rhythm",
            "bass",
            "drums",
            "keys",
            "guitarghl",
            "guitarcoopghl",
            "rhythmghl",
            "bassghl",
            None,
        ]
    ]
    page: Optional[int]
    difficulty: Optional[Literal["expert", "hard", "medium", "easy", None]]
    name: Optional[SearchFilter]
    artist: Optional[SearchFilter]
    album: Optional[SearchFilter]
    genre: Optional[SearchFilter]
    year: Optional[SearchFilter]
    charter: Optional[SearchFilter]
    min_length: Optional[int]
    max_length: Optional[int]
    min_intensity: Optional[int]
    max_intensity: Optional[int]
    min_average_nps: Optional[int]
    max_average_nps: Optional[int]
    min_max_nps: Optional[int]
    max_max_nps: Optional[int]
    hash: Optional[str]
    chart_hash: Optional[str]
    modified_after: Optional[datetime]
    has_solo_sections: Optional[bool]
    has_forced_notes: Optional[bool]
    has_open_notes: Optional[bool]
    has_tap_notes: Optional[bool]
    has_lyrics: Optional[bool]
    has_vocals: Optional[bool]
    has_roll_lanes: Optional[bool]
    has_2x_kick: Optional[bool]
    has_issues: Optional[bool]
    has_video_background: Optional[bool]
    modchart: Optional[bool]
    chart_id_after: Optional[int]


class EncoreRequestHeaders(TypedDict):
    Accept: Literal["application/json"]
