__all__ = ["Feather"]
__version__ = "4.28.0"
from pathlib import Path
from enum import Enum


class Feather4(Enum):
    @classmethod
    def _font_file(self) -> str:
        fonts = Path(__file__).parent / "fonts"
        return str(fonts / "Feather.ttf")

    activity = "\uf100"
    airplay = "\uf101"
    alert_circle = "\uf102"
    alert_octagon = "\uf103"
    alert_triangle = "\uf104"
    align_center = "\uf105"
    align_justify = "\uf106"
    align_left = "\uf107"
    align_right = "\uf108"
    anchor = "\uf109"
    aperture = "\uf10a"
    archive = "\uf10b"
    arrow_down = "\uf10c"
    arrow_down_circle = "\uf10d"
    arrow_down_left = "\uf10e"
    arrow_down_right = "\uf10f"
    arrow_left = "\uf110"
    arrow_left_circle = "\uf111"
    arrow_right = "\uf112"
    arrow_right_circle = "\uf113"
    arrow_up = "\uf114"
    arrow_up_circle = "\uf115"
    arrow_up_left = "\uf116"
    arrow_up_right = "\uf117"
    at_sign = "\uf118"
    award = "\uf119"
    bar_chart = "\uf11a"
    bar_chart_2 = "\uf11b"
    battery = "\uf11c"
    battery_charging = "\uf11d"
    bell = "\uf11e"
    bell_off = "\uf11f"
    bluetooth = "\uf120"
    bold = "\uf121"
    book = "\uf122"
    book_open = "\uf123"
    bookmark = "\uf124"
    box = "\uf125"
    briefcase = "\uf126"
    calendar = "\uf127"
    camera = "\uf128"
    camera_off = "\uf129"
    cast = "\uf12a"
    check = "\uf12b"
    check_circle = "\uf12c"
    check_square = "\uf12d"
    chevron_down = "\uf12e"
    chevron_left = "\uf12f"
    chevron_right = "\uf130"
    chevron_up = "\uf131"
    chevrons_down = "\uf132"
    chevrons_left = "\uf133"
    chevrons_right = "\uf134"
    chevrons_up = "\uf135"
    chrome = "\uf136"
    circle = "\uf137"
    clipboard = "\uf138"
    clock = "\uf139"
    cloud = "\uf13a"
    cloud_drizzle = "\uf13b"
    cloud_lightning = "\uf13c"
    cloud_off = "\uf13d"
    cloud_rain = "\uf13e"
    cloud_snow = "\uf13f"
    code = "\uf140"
    codepen = "\uf141"
    codesandbox = "\uf142"
    coffee = "\uf143"
    columns = "\uf144"
    command = "\uf145"
    compass = "\uf146"
    copy = "\uf147"
    corner_down_left = "\uf148"
    corner_down_right = "\uf149"
    corner_left_down = "\uf14a"
    corner_left_up = "\uf14b"
    corner_right_down = "\uf14c"
    corner_right_up = "\uf14d"
    corner_up_left = "\uf14e"
    corner_up_right = "\uf14f"
    cpu = "\uf150"
    credit_card = "\uf151"
    crop = "\uf152"
    crosshair = "\uf153"
    database = "\uf154"
    delete = "\uf155"
    disc = "\uf156"
    divide = "\uf157"
    divide_circle = "\uf158"
    divide_square = "\uf159"
    dollar_sign = "\uf15a"
    download = "\uf15b"
    download_cloud = "\uf15c"
    dribbble = "\uf15d"
    droplet = "\uf15e"
    edit = "\uf15f"
    edit_2 = "\uf160"
    edit_3 = "\uf161"
    external_link = "\uf162"
    eye = "\uf163"
    eye_off = "\uf164"
    facebook = "\uf165"
    fast_forward = "\uf166"
    feather = "\uf167"
    figma = "\uf168"
    file = "\uf169"
    file_minus = "\uf16a"
    file_plus = "\uf16b"
    file_text = "\uf16c"
    film = "\uf16d"
    filter = "\uf16e"
    flag = "\uf16f"
    folder = "\uf170"
    folder_minus = "\uf171"
    folder_plus = "\uf172"
    framer = "\uf173"
    frown = "\uf174"
    gift = "\uf175"
    git_branch = "\uf176"
    git_commit = "\uf177"
    git_merge = "\uf178"
    git_pull_request = "\uf179"
    github = "\uf17a"
    gitlab = "\uf17b"
    globe = "\uf17c"
    grid = "\uf17d"
    hard_drive = "\uf17e"
    hash = "\uf17f"
    headphones = "\uf180"
    heart = "\uf181"
    help_circle = "\uf182"
    hexagon = "\uf183"
    home = "\uf184"
    image = "\uf185"
    inbox = "\uf186"
    info = "\uf187"
    instagram = "\uf188"
    italic = "\uf189"
    key = "\uf18a"
    layers = "\uf18b"
    layout = "\uf18c"
    life_buoy = "\uf18d"
    link = "\uf18e"
    link_2 = "\uf18f"
    linkedin = "\uf190"
    list = "\uf191"
    loader = "\uf192"
    lock = "\uf193"
    log_in = "\uf194"
    log_out = "\uf195"
    mail = "\uf196"
    map = "\uf197"
    map_pin = "\uf198"
    maximize = "\uf199"
    maximize_2 = "\uf19a"
    meh = "\uf19b"
    menu = "\uf19c"
    message_circle = "\uf19d"
    message_square = "\uf19e"
    mic = "\uf19f"
    mic_off = "\uf1a0"
    minimize = "\uf1a1"
    minimize_2 = "\uf1a2"
    minus = "\uf1a3"
    minus_circle = "\uf1a4"
    minus_square = "\uf1a5"
    monitor = "\uf1a6"
    moon = "\uf1a7"
    more_horizontal = "\uf1a8"
    more_vertical = "\uf1a9"
    mouse_pointer = "\uf1aa"
    move = "\uf1ab"
    music = "\uf1ac"
    navigation = "\uf1ad"
    navigation_2 = "\uf1ae"
    octagon = "\uf1af"
    package = "\uf1b0"
    paperclip = "\uf1b1"
    pause = "\uf1b2"
    pause_circle = "\uf1b3"
    pen_tool = "\uf1b4"
    percent = "\uf1b5"
    phone = "\uf1b6"
    phone_call = "\uf1b7"
    phone_forwarded = "\uf1b8"
    phone_incoming = "\uf1b9"
    phone_missed = "\uf1ba"
    phone_off = "\uf1bb"
    phone_outgoing = "\uf1bc"
    pie_chart = "\uf1bd"
    play = "\uf1be"
    play_circle = "\uf1bf"
    plus = "\uf1c0"
    plus_circle = "\uf1c1"
    plus_square = "\uf1c2"
    pocket = "\uf1c3"
    power = "\uf1c4"
    printer = "\uf1c5"
    radio = "\uf1c6"
    refresh_ccw = "\uf1c7"
    refresh_cw = "\uf1c8"
    repeat = "\uf1c9"
    rewind = "\uf1ca"
    rotate_ccw = "\uf1cb"
    rotate_cw = "\uf1cc"
    rss = "\uf1cd"
    save = "\uf1ce"
    scissors = "\uf1cf"
    search = "\uf1d0"
    send = "\uf1d1"
    server = "\uf1d2"
    settings = "\uf1d3"
    share = "\uf1d4"
    share_2 = "\uf1d5"
    shield = "\uf1d6"
    shield_off = "\uf1d7"
    shopping_bag = "\uf1d8"
    shopping_cart = "\uf1d9"
    shuffle = "\uf1da"
    sidebar = "\uf1db"
    skip_back = "\uf1dc"
    skip_forward = "\uf1dd"
    slack = "\uf1de"
    slash = "\uf1df"
    sliders = "\uf1e0"
    smartphone = "\uf1e1"
    smile = "\uf1e2"
    speaker = "\uf1e3"
    square = "\uf1e4"
    star = "\uf1e5"
    stop_circle = "\uf1e6"
    sun = "\uf1e7"
    sunrise = "\uf1e8"
    sunset = "\uf1e9"
    tablet = "\uf1ea"
    tag = "\uf1eb"
    target = "\uf1ec"
    terminal = "\uf1ed"
    thermometer = "\uf1ee"
    thumbs_down = "\uf1ef"
    thumbs_up = "\uf1f0"
    toggle_left = "\uf1f1"
    toggle_right = "\uf1f2"
    tool = "\uf1f3"
    trash = "\uf1f4"
    trash_2 = "\uf1f5"
    trello = "\uf1f6"
    trending_down = "\uf1f7"
    trending_up = "\uf1f8"
    triangle = "\uf1f9"
    truck = "\uf1fa"
    tv = "\uf1fb"
    twitch = "\uf1fc"
    twitter = "\uf1fd"
    type = "\uf1fe"
    umbrella = "\uf1ff"
    underline = "\uf200"
    unlock = "\uf201"
    upload = "\uf202"
    upload_cloud = "\uf203"
    user = "\uf204"
    user_check = "\uf205"
    user_minus = "\uf206"
    user_plus = "\uf207"
    user_x = "\uf208"
    users = "\uf209"
    video = "\uf20a"
    video_off = "\uf20b"
    voicemail = "\uf20c"
    volume = "\uf20d"
    volume_1 = "\uf20e"
    volume_2 = "\uf20f"
    volume_x = "\uf210"
    watch = "\uf211"
    wifi = "\uf212"
    wifi_off = "\uf213"
    wind = "\uf214"
    x = "\uf215"
    x_circle = "\uf216"
    x_octagon = "\uf217"
    x_square = "\uf218"
    youtube = "\uf219"
    zap = "\uf21a"
    zap_off = "\uf21b"
    zoom_in = "\uf21c"
    zoom_out = "\uf21d"
