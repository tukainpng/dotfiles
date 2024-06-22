config.load_autoconfig()
config.source('gruvbox.py')

# Teclas de atalho
config.bind('<space>p', 'tab-next')
config.bind('<space>a', 'tab-prev')
config.bind('<space>c', 'tab-close')
config.bind('<space>m', 'spawn mpv {url}')
config.bind('<space>u', 'adblock-update')
config.bind('<space>r', 'config-source')
config.bind('<space>b', 'bookmark-list')
config.bind('<space>d', 'download')
config.bind('<space>s', 'print')
config.bind('<space>i', 'devtools')

# Adblock list
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/legacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt"
]
