class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'down'
        self.TarMirrorCommand = 'tardown'
        self.CancelMirror = 'stop'
        self.CancelAllCommand = 'stopall'
        self.ListCommand = 'list'
        self.StatusCommand = 'status'
        self.AuthorizeCommand = 'authorize'
        self.UnAuthorizeCommand = 'unauthorize'
        self.PingCommand = 'ping'
        self.RestartCommand = 'restart'
        self.StatsCommand = 'stats'
        self.HelpCommand = 'help'
        self.LogCommand = 'log'
        self.CloneCommand = "move"
        self.WatchCommand = 'watch'
        self.TarWatchCommand = 'tarwatch'

BotCommands = _BotCommands()
