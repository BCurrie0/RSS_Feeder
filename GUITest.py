import PySimpleGUI as sg
import RssFeeder as rf
import webbrowser


# get data from RssFeeder and format so easy to use .
rssFeed = rf.getData("https://www.darkreading.com/rss.xml")
entry = rf.getLatest(rssFeed)

# loading a theme (possible make option later?)
sg.theme('DarkPurple7')
# All the stuff inside your window.
# tab1_layout = [[sg.Text(entry.title
#                         [sg.Text(text=entry.link, enable_events=True)],
#                         [sg.Button('HERE I WANT TO ADD RSS FEEDS.'), sg.Button('Cancel')]
#
# tab2_layout = [[sg.Text("test")],
#           [sg.Text(text=entry.link, enable_events=True)],
#           [sg.Button('HERE I WANT TO ADD RSS FEEDS.'), sg.Button('Cancel')]]
tab1_layout = [[sg.Text(entry.title)],
               [sg.Text(text=entry.link, enable_events=True)],
               [sg.Button('HERE I WANT TO ADD RSS FEEDS.')]]

tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, tooltip='tip'),
                        sg.Tab('Tab 2', tab2_layout)]], tooltip='TIP2')]]
# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        # if user closes window or clicks cancel
        break
    webbrowser.open(entry.link)

window.close()
