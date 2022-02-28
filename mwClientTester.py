import mwclient
import time
import datetime as dt
from datetime import date, timedelta
site = mwclient.Site('lol.fandom.com', path='/')


response = site.cargo_client.query('cargoquery',
                                   limit='max',
                                   tables="ScoreboardGames=SG",
                                   fields="SG.Tournament, SG.DateTime_UTC, SG.Team1, SG.Team2",
                                   where="SG.DateTime_UTC >= '2019-08-01 00:00:00'"  # Results after Aug 1, 2019
                                   )
for i in response:
    for x in i:
        print(x)
