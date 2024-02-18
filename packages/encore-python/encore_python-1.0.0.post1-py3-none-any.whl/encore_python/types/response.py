import jsonobject

from .shared import valid_hash, instruments, difficulties


class NotesPerSecond(jsonobject.JsonObject):
    time = jsonobject.FloatProperty(name="time")
    length = jsonobject.FloatProperty(name="length")
    type = jsonobject.StringProperty(name="type")


class NotesPerSecondMetaData(jsonobject.JsonObject):
    instrument = jsonobject.StringProperty(name="instrument")
    difficulty = jsonobject.StringProperty(name="difficulty")
    time = jsonobject.FloatProperty(name="time")
    nps = jsonobject.IntegerProperty(name="nps")
    notes = jsonobject.ListProperty(lambda: NotesPerSecond, name="notes")


class NoteIssue(jsonobject.JsonObject):
    issue_type = jsonobject.StringProperty(name="issueType")
    time = jsonobject.FloatProperty(name="time")

    def __repr__(self) -> str:
        return f"{self.issue_type} at {self.time:.2f}"


class TrackIssue(jsonobject.JsonObject):
    instrument = instrument = jsonobject.StringProperty(
        name="instrument", choices=instruments, exclude_if_none=False
    )
    difficulty = jsonobject.StringProperty(
        name="difficulty", choices=difficulties, exclude_if_none=False
    )
    track_issues = jsonobject.ListProperty(str, name="trackIssues")


class NoteIssueMetadata(jsonobject.JsonObject):
    instrument = jsonobject.StringProperty(name="instrument")
    difficulty = jsonobject.StringProperty(name="difficulty")
    note_issues = jsonobject.ListProperty(lambda: NoteIssue, name="noteIssues")


class NoteCount(jsonobject.JsonObject):
    instrument = jsonobject.StringProperty(name="instrument")
    difficulty = jsonobject.StringProperty(name="difficulty")
    count = jsonobject.IntegerProperty(name="count")


class Hash(jsonobject.JsonObject):
    instrument = jsonobject.StringProperty(name="instrument")
    difficulty = jsonobject.StringProperty(name="difficulty")
    hash = jsonobject.StringProperty(name="hash")


class NotesData(jsonobject.JsonObject):
    instruments = jsonobject.ListProperty(name="instruments")
    drum_type = jsonobject.StringProperty(name="drumType")
    has_solo_sections = jsonobject.BooleanProperty(name="hasSoloSections")
    has_lyrics = jsonobject.BooleanProperty(name="hasLyrics")
    has_vocals = jsonobject.BooleanProperty(name="hasVocals")
    has_forced_notes = jsonobject.BooleanProperty(
        name="hasForcedNotes", exclude_if_none=True
    )
    has_tap_notes = jsonobject.BooleanProperty(name="hasTapNotes", exclude_if_none=True)
    has_open_notes = jsonobject.BooleanProperty(
        name="hasOpenNotes", exclude_if_none=True
    )
    has_2x_kick = jsonobject.BooleanProperty(name="has2xKick", exclude_if_none=True)
    has_roll_lanes = jsonobject.BooleanProperty(
        name="hasRollLanes", exclude_if_none=True
    )
    note_issues = jsonobject.ListProperty(lambda: NoteIssueMetadata, name="noteIssues")
    track_issues = jsonobject.ListProperty(lambda: TrackIssue, name="trackIssues")
    chart_issues = jsonobject.ListProperty(dict, name="chartIssues")
    note_counts = jsonobject.ListProperty(lambda: NoteCount, name="note_counts")
    max_nps = jsonobject.ListProperty(lambda: NotesPerSecondMetaData, name="maxNps")
    hashes = jsonobject.ListProperty(lambda: Hash, name="hashes")
    tempo_map_hash = jsonobject.StringProperty(name="tempoMapHash")
    tempo_marker_count = jsonobject.IntegerProperty(name="tempoMarkerCount")
    length = jsonobject.IntegerProperty(name="length")
    effective_length = jsonobject.IntegerProperty(name="effectiveLength")


class FolderIssue(jsonobject.JsonObject):
    folder_issue = jsonobject.StringProperty(name="folderIssue")
    description = jsonobject.StringProperty(name="description")


class Song(jsonobject.JsonObject):
    ordering = jsonobject.IntegerProperty(name="ordering")
    name = jsonobject.StringProperty(name="name")
    artist = jsonobject.StringProperty(name="artist")
    album = jsonobject.StringProperty(name="album")
    genre = jsonobject.StringProperty(name="genre")
    year = jsonobject.StringProperty(name="year")
    chart_name = jsonobject.StringProperty(name="chartName")
    chart_album = jsonobject.StringProperty(name="chartAlbum")
    chart_genre = jsonobject.StringProperty(name="chartGenre")
    chart_year = jsonobject.StringProperty(name="chartYear")
    chart_id = jsonobject.IntegerProperty(name="chartId")
    song_id = jsonobject.IntegerProperty(name="songId")
    group_id = jsonobject.IntegerProperty(name="groupId")
    chart_drive_chart_id = jsonobject.IntegerProperty(name="chartDriveChartId")
    album_art_md5 = jsonobject.StringProperty(name="albumArtMd5", validators=valid_hash)
    md5 = jsonobject.StringProperty(name="md5", validators=valid_hash)
    chart_md5 = jsonobject.StringProperty(name="chartMd5", validators=valid_hash)
    version_group_id = jsonobject.IntegerProperty(name="versionGroupId")
    charter = jsonobject.StringProperty(name="charter")
    song_length = jsonobject.IntegerProperty(name="song_length")
    diff_band = jsonobject.IntegerProperty(name="diff_band", default=-1)
    diff_guitar = jsonobject.IntegerProperty(name="diff_guitar", default=-1)
    diff_guitar_coop = jsonobject.IntegerProperty(name="diff_guitar_coop", default=-1)
    diff_rhythm = jsonobject.IntegerProperty(name="diff_rhythm", default=-1)
    diff_bass = jsonobject.IntegerProperty(name="diff_bass", default=-1)
    diff_drums = jsonobject.IntegerProperty(name="diff_drums", default=-1)
    diff_drums_real = jsonobject.IntegerProperty(name="diff_drums_real", default=-1)
    diff_drums_real22 = jsonobject.IntegerProperty(name="diff_drums_real22", default=-1)
    diff_keys = jsonobject.IntegerProperty(name="diff_keys", default=-1)
    diff_keys_real = jsonobject.IntegerProperty(name="diff_keys_real", default=-1)
    diff_guitarghl = jsonobject.IntegerProperty(name="diff_guitarghl", default=-1)
    diff_guitar_coop_ghl = jsonobject.IntegerProperty(
        name="diff_guitar_coop_ghl", default=-1
    )
    diff_rhythm_ghl = jsonobject.IntegerProperty(name="diff_rhythm_ghl", default=-1)
    diff_bassghl = jsonobject.IntegerProperty(name="diff_bassghl", default=-1)
    diff_vocals = jsonobject.IntegerProperty(name="diff_vocals", default=-1)
    diff_dance = jsonobject.IntegerProperty(name="diff_dance", default=-1)
    preview_start_time = jsonobject.IntegerProperty(name="preview_start_time")
    icon = jsonobject.StringProperty(name="icon")
    loading_phrase = jsonobject.StringProperty(name="loading_phrase")
    album_track = jsonobject.IntegerProperty(name="album_track")
    playlist_track = jsonobject.IntegerProperty(name="playlist_track")
    modchart = jsonobject.BooleanProperty(name="modchart")
    delay = jsonobject.IntegerProperty(name="delay")
    chart_offset = jsonobject.IntegerProperty(name="chart_offset")
    hopo_frequency = jsonobject.IntegerProperty(name="hopo_frequency")
    eighthnote_hopo = jsonobject.BooleanProperty(name="eighthnote_hopo")
    multiplier_note = jsonobject.IntegerProperty(name="multiplier_note")
    video_start_time = jsonobject.IntegerProperty(name="video_start_time")
    five_lane_drums = jsonobject.BooleanProperty(name="five_lane_drums")
    pro_drums = jsonobject.BooleanProperty(name="pro_drums")
    end_events = jsonobject.BooleanProperty(name="end_events")
    notes_data = jsonobject.ObjectProperty(NotesData, name="notesData")
    folder_issues = jsonobject.ListProperty(FolderIssue, name="folderIssues")
    metadata_issues = jsonobject.ListProperty(str, name="metadataIssues")
    has_video_background = jsonobject.BooleanProperty(name="hasVideoBackground")
    modified_time = jsonobject.DateTimeProperty(name="modifiedTime")
    application_drive_id = jsonobject.StringProperty(name="applicationDriveId")
    application_username = jsonobject.StringProperty(name="applicationUsername")
    pack_name = jsonobject.StringProperty(name="packName")
    parent_folder_id = jsonobject.StringProperty(name="parentFolderId")
    drive_path = jsonobject.StringProperty(name="drivePath")
    drive_file_id = jsonobject.StringProperty(name="driveFileId")
    drive_file_name = jsonobject.StringProperty(name="driveFileName")
    drive_chart_is_pack = jsonobject.BooleanProperty(name="driveChartIsPack")
    archive_path = jsonobject.StringProperty(name="archivePath")
    chart_file_name = jsonobject.StringProperty(name="chartFileName")

    def __repr__(self) -> str:
        return f"Song(name={self.name}, artist={self.artist}, charter={self.charter})"


class SearchResponse(jsonobject.JsonObject):
    found = jsonobject.IntegerProperty(name="found")
    out_of = jsonobject.IntegerProperty(name="out_of")
    page = jsonobject.IntegerProperty(name="page")
    search_time_ms = jsonobject.IntegerProperty(name="search_time_ms")
    data = jsonobject.ListProperty(lambda: Song, name="data")


class ErrorMessage(jsonobject.JsonObject):
    code = jsonobject.StringProperty(name="code")
    expected = jsonobject.StringProperty(name="expected")
    received = jsonobject.StringProperty(name="received")
    path = jsonobject.ListProperty(str, name="path")
    message = jsonobject.StringProperty(name="message")


class ErrorResponse(jsonobject.JsonObject):
    error = jsonobject.StringProperty(name="error")
    message = jsonobject.ListProperty(lambda: ErrorMessage, name="message")
