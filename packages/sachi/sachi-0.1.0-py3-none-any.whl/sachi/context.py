from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class FileBotContext:
    n: str | None = None
    """movie / series name (`Dark Angel`)"""
    
    y: int | None = None
    """movie / series year (`2009`)"""
    
    s: int | None = None
    """season number (`3`)"""
    
    e: int | None = None
    """episode number (`1`)"""
    
    sxe: str | None = None
    """season / episode number (`1x01`)"""
    
    s00e00: str | None = None
    """season / episode number (`S01E01`)"""
    
    t: str | None = None
    """episode title (`Labyrinth`)"""
    
    d: datetime | None = None
    """airdate (`2009-06-01`)"""
    
    startdate: datetime | None = None
    """series start date (`2002-09-20`)"""
    
    absolute: int | None = None
    """absolute episode number (`42`)"""
    
    ny: str | None = None
    """name (year) (`Avatar (2009)`)"""
    
    es: list[int] | None = None
    """episode numbers (`[1, 2, 3]`)"""
    
    sy: list[int] | None = None
    """season years (`[2002, 2003]`)"""
    
    sc: int | None = None
    """season count (`5`)"""
    
    di: int | None = None
    """duplicate index (`1`)"""
    
    dc: int | None = None
    """duplicate count (`2`)"""
    
    age: int | None = None
    """age in days (`7`)"""
    
    special: int | None = None
    """special number (`1`)"""
    
    episode: str | None = None
    """episode object (`Firefly - 1x01 - Serenity`)"""
    
    series: dict[str, Any] | None = None
    """series object (`<series properties>`)"""
    
    primaryTitle: str | None = None
    """primary name (`Juuni Kokuki`)"""
    
    alias: str | None = None
    """alias names (`[Juuni Kokuki, ...]`)"""
    
    movie: dict[str, Any] | None = None
    """movie object (`Avatar (2009)`)"""
    
    id: int | None = None
    """movie / series ID (`1437`)"""
    
    tmdbid: int | None = None
    """TheMovieDB ID (`1437`)"""
    
    tvdbid: int | None = None
    """TheTVDB ID (`78874`)"""
    
    imdbid: str | None = None
    """IMDb ID (`tt0756683`)"""
    
    pi: int | None = None
    """part index (`1`)"""
    
    pc: int | None = None
    """part count (`2`)"""
    
    lang: str | None = None
    """subtitle language (`eng`)"""
    
    subt: str | None = None
    """subtitle tag (`.eng.forced`)"""
    
    plex: Path | None = None
    """Plex Naming Standard (`<relative path>`)"""
    
    kodi: Path | None = None
    """Kodi Naming Standard (`<relative path>`)"""
    
    emby: Path | None = None
    """Emby Naming Standard (`<relative path>`)"""
    
    jellyfin: Path | None = None
    """Jellyfin Naming Standard (`<relative path>`)"""
    
    az: str | None = None
    """sort collection letter (`A`)"""
    
    object: Any | None = None
    """match object (`Firefly - 1x01 - Serenity`)"""
    
    type: str | None = None
    """object type (`Episode`)"""
    
    anime: bool | None = None
    """is anime episode (`false`)"""
    
    regular: bool | None = None
    """is regular episode (`true`)"""
    
    music: str | None = None
    """music object (`Leona Lewis - I See You`)"""
    
    medium: int | None = None
    """medium index (`1`)"""
    
    album: str | None = None
    """album (`Avatar`)"""
    
    artist: str | None = None
    """track artist (`Leona Lewis`)"""
    
    albumArtist: str | None = None
    """album artist (`James Horner`)"""
    
    actors: list[str] | None = None
    """list of actors (`[Zoe Saldana, ...]`)"""
    
    director: str | None = None
    """movie director (`James Cameron`)"""
    
    collection: str | None = None
    """movie collection (`Avatar Collection`)"""
    
    ci: int | None = None
    """movie collection index (`1`)"""
    
    cy: list[int] | None = None
    """movie collection years (`[1977, 2019]`)"""
    
    decade: int | None = None
    """movie decade (`1970`)"""
    
    genre: str | None = None
    """primary genre (`Science Fiction`)"""
    
    genres: list[str] | None = None
    """all genres (`[Science Fiction, ...]`)"""
    
    language: str | None = None
    """original language (`eng`)"""
    
    languages: list[str] | None = None
    """spoken languages (`[eng]`)"""
    
    country: str | None = None
    """origin country (`KR`)"""
    
    runtime: int | None = None
    """movie / episode runtime (`162`)"""
    
    certification: str | None = None
    """content rating (`PG-13`)"""
    
    rating: float | None = None
    """movie rating (`7.4`)"""
    
    votes: int | None = None
    """movie votes (`17720`)"""
    
    vcf: str | None = None
    """video compression format (`HEVC`)"""
    
    vc: str | None = None
    """video codec library (`x264`)"""
    
    ac: str | None = None
    """audio codec (`ac3`)"""
    
    cf: str | None = None
    """container format (`mkv`)"""
    
    vf: str | None = None
    """standard video format (`1080p`)"""
    
    hpi: str | None = None
    """exact video format (`384i`)"""
    
    aco: str | None = None
    """audio codec profile (`TrueHD+Atmos`)"""
    
    acf: str | None = None
    """audio channel format (`DD5.1`)"""
    
    af: str | None = None
    """audio channel count (`6ch`)"""
    
    channels: str | None = None
    """audio channel layout (`5.1`)"""
    
    resolution: str | None = None
    """video resolution (`3840x2160`)"""
    
    width: int | None = None
    """video width (`3840`)"""
    
    height: int | None = None
    """video height (`2160`)"""
    
    bitdepth: int | None = None
    """video bitdepth (`10`)"""
    
    hdr: str | None = None
    """high dynamic range (`HDR`)"""
    
    dovi: str | None = None
    """Dolby Vision (`Dolby Vision`)"""
    
    bitrate: str | None = None
    """overall bitrate (`2.0 Mbps`)"""
    
    vbr: str | None = None
    """video bitrate (`1.6 Mbps`)"""
    
    abr: str | None = None
    """audio bitrate (`192 kbps`)"""
    
    fps: str | None = None
    """frame rate (`23.976 fps`)"""
    
    khz: str | None = None
    """sampling rate (`44.1 kHz`)"""
    
    ar: str | None = None
    """aspect ratio (`16∶9`)"""
    
    ws: str | None = None
    """widescreen tag (`WS`)"""
    
    hd: str | None = None
    """video definition class (`UHD`)"""
    
    dt: datetime | None = None
    """media creation date (`<date and time>`)"""
    
    vs: str | None = None
    """source class (`BluRay`)"""
    
    source: str | None = None
    """source match (`BD25`)"""
    
    edition: str | None = None
    """movie edition (`Extended Edition`)"""
    
    tags: list[str] | None = None
    """movie tags (`[Extended Edition]`)"""
    
    s3d: str | None = None
    """stereoscopic 3D tag (`3D SBS`)"""
    
    group: str | None = None
    """release group (`ALLiANCE`)"""
    
    original: str | None = None
    """original file name (`Serenity`)"""
    
    historic: dict[str, Any] | None = None
    """original path (`<bindings>`)"""
    
    info: dict[str, Any] | None = None
    """extended metadata (`<all properties>`)"""
    
    omdb: dict[str, Any] | None = None
    """OMDb info (`<all properties>`)"""
    
    localize: dict[str, Any] | None = None
    """dynamic localization (`<languages>`)"""
    
    order: dict[str, Any] | None = None
    """dynamic episode order (`<episode orders>`)"""
    
    db: dict[str, Any] | None = None
    """dynamic cross-reference (`<mapper>`)"""
    
    fn: str | None = None
    """current file name (`Serenity`)"""
    
    ext: str | None = None
    """file extension (`mkv`)"""
    
    f: Path | None = None
    """file object (`<file path>`)"""
    
    folder: Path | None = None
    """folder object (`<folder path>`)"""
    
    drive: Path | None = None
    """file system root (`<folder path>`)"""
    
    files: list[Path] | None = None
    """file group (`<file paths>`)"""
    
    relativeFile: Path | None = None
    """relative library path (`<relative path>`)"""
    
    mediaFile: Path | None = None
    """primary media file (`<file path>`)"""
    
    mediaFileName: str | None = None
    """primary media file name (`Serenity`)"""
    
    mediaTitle: str | None = None
    """embedded media title (`Serenity`)"""
    
    audioLanguages: list[str] | None = None
    """audio streams (`<audio languages>`)"""
    
    textLanguages: list[str] | None = None
    """subtitle streams (`<subtitle languages>`)"""
    
    duration: str | None = None
    """media duration (`PT23M9.974S`)"""
    
    seconds: int | None = None
    """duration in seconds (`1389`)"""
    
    minutes: int | None = None
    """duration in minutes (`23`)"""
    
    hours: str | None = None
    """duration in HH:mm (`0:23`)"""
    
    bytes: str | None = None
    """file size (`356 MB`)"""
    
    megabytes: str | None = None
    """file size in MB (`356 MB`)"""
    
    gigabytes: str | None = None
    """file size in GB (`0.4 GB`)"""
    
    ct: datetime | None = None
    """file creation date (`<date and time>`)"""
    
    crc32: str | None = None
    """CRC32 checksum (`3E16AF40`)"""
    
    media: dict[str, str] | None = None
    """media properties (`<media properties>`)"""
    
    video: list[dict[str, str]] | None = None
    """video streams (`<video streams>`)"""
    
    audio: list[dict[str, str]] | None = None
    """audio streams (`<audio streams>`)"""
    
    text: list[dict[str, str]] | None = None
    """subtitle streams (`<subtitle streams>`)"""
    
    image: dict[str, str] | None = None
    """image properties (`<image properties>`)"""
    
    exif: dict[str, str] | None = None
    """EXIF image metadata (`<image properties>`)"""
    
    camera: dict[str, str] | None = None
    """photo camera (`<camera properties>`)"""
    
    location: dict[str, str] | None = None
    """photo location (`<location properties>`)"""
    
    today: datetime | None = None
    """current date (`2022-08-08`)"""
    
    home: Path | None = None
    """user home folder (`<folder path>`)"""
    
    output: Path | None = None
    """--output folder (`<folder path>`)"""
    
    defines: dict[str, str] | None = None
    """--def parameters (`<script parameters>`)"""
    
    label: str | None = None
    """--def label value (`<label parameter>`)"""
    
    self: dict[str, Any] | None = None
    """match bindings (`<bindings>`)"""
    
    model: list[dict[str, Any]] | None = None
    """match context (`<list of bindings>`)"""
    
    episodelist: list[dict[str, Any]] | None = None
    """series context (`<list of bindings>`)"""
    
    AnimeList: str | None = None
    """Anime Lists mapper (`<mapping>`)"""
    
    XEM: str | None = None
    """XEM mapper (`<mapping>`)"""
    
