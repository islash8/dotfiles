# ~/.config/qutebrowser/config.py

# load existing settings made via :set
config.load_autoconfig()

# the page to open when opening a new tab or window
c.url.default_page = "https://www.duckduckgo.com"

# the page to open when starting qutebrowser
c.url.start_pages = "https://www.duckduckgo.com"

# search engines to set
# type 'o keyword search term' to search
#
c.url.searchengines = {
    "DEFAULT": "https://www.duckduckgo.com/?q={}",
    "aw": "https://wiki.archlinux.org/index.php?search={}",
    "g": "https://www.google.com/search?q={}",
    "r": "https://www.reddit.com/search/?q={}",
    "w": "https://en.wikipedia.org/w/index.php?search={}",
    "yt": "https://www.youtube.com/results?search_query={}",
}

# enable dark made
c.colors.webpage.darkmode.enabled = True

# set default fonts
c.fonts.default_family = "shure tech mono"
c.fonts.default_size = "12pt"

# ad blocking
c.content.blocking.enabled = True
c.content.blocking.hosts.lists = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
]

# tap management
c.tabs.position = "top"
c.tabs.show = "always"
c.tabs.favicons.show = "always"

# change tabs size
c.tabs.width = "10%"
