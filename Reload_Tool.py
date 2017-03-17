from robotide.publish import RideOpenSuite, RideFileNameChanged
from robotide.publish.messages import RideNewProject, RideSaved
from robotide.pluginapi import Plugin# ActionInfo, SeparatorInfo


# import wx.lib.inspection
# wx.lib.inspection.InspectionTool().Show()


class Reload_Files(Plugin):
    """Used to reload files edited in external editor via shortcut."""

    def __init__(self, application):
        Plugin.__init__(self, application, metadata={'Shortcut': 'CTRL + R'})
        self.path = "None"
        self.reg_shortcut()

    def reg_shortcut(self):
        self.register_shortcut('CtrlCmd-r', self.reload_files)
        self.subscribe(self.set_path, RideOpenSuite)
        self.subscribe(self.set_path, RideFileNameChanged)
        self.subscribe(self.set_path, RideNewProject)
        self.subscribe(self.set_path, RideSaved)

    def enable(self):
        print("Reload Enabled")
        self.reg_shortcut()

    def disable(self):
        self.unsubscribe_all()
        self.unregister_actions()

    def reopen_suite(self):
        self.open_suite(self.path)

    def reload_files(self,event):
        self.reopen_suite()

    def set_path(self,event):
        self.path = event.path

