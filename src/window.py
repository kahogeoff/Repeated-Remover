#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Mon Sep 08 10:58:06 2014
#

import wx
import core

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.txt_path = wx.TextCtrl(self, wx.ID_ANY, "")
        self.btn_open = wx.Button(self, wx.ID_ANY, _("Open"))
        self.tree_file = wx.TreeCtrl(self, wx.ID_ANY, style=wx.TR_HAS_BUTTONS | wx.TR_LINES_AT_ROOT | wx.TR_DEFAULT_STYLE | wx.SUNKEN_BORDER)
        self.btn_check = wx.Button(self, wx.ID_ANY, _("Check"))
        self.btn_Remove = wx.Button(self, wx.ID_ANY, _("Remove"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.btn_open)
        self.Bind(wx.EVT_BUTTON, self.OnCheck, self.btn_check)
        self.Bind(wx.EVT_BUTTON, self.OnRemove, self.btn_Remove)

        self.root = None
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle(_("Repeated Remover"))
        self.SetSize((500, 400))
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        mainSizer = wx.FlexGridSizer(3, 3, 2, 2)
        lbl_path = wx.StaticText(self, wx.ID_ANY, _("File Path: "))
        lbl_path.SetMinSize((-1, 20))
        mainSizer.Add(lbl_path, 0, wx.ALL| wx.ALIGN_RIGHT, 5)
        mainSizer.Add(self.txt_path, 0, wx.ALL | wx.EXPAND, 5)
        mainSizer.Add(self.btn_open, 0, wx.ALL , 5)
        mainSizer.Add((20, 20), 0, 0, 0)
        mainSizer.Add(self.tree_file, 1, wx.ALL | wx.EXPAND, 5)
        mainSizer.Add((20, 20), 0, 0, 0)
        mainSizer.Add((20, 20), 0, 0, 0)
        mainSizer.Add(self.btn_check, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 5)
        mainSizer.Add(self.btn_Remove, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 5)
        self.SetSizer(mainSizer)
        mainSizer.AddGrowableRow(1)
        mainSizer.AddGrowableCol(1)
        self.Layout()
        self.btn_Remove.Disable()
        # end wxGlade

    def OnOpen(self, event):  # wxGlade: MainFrame.<event_handler>
        dirDia = wx.DirDialog(None, "Select directory to open", "~/", 0, (10, 10))
        ret = dirDia.ShowModal()
        if ret == wx.ID_OK:
            self.txt_path.SetValue(dirDia.GetPath())
            core.path = self.txt_path.GetValue()
        dirDia.Destroy()
        self.tree_file.DeleteAllItems()
        core.fileList = []
        core.sortedList = []
        self.root = self.tree_file.AddRoot(self.txt_path.GetValue())
        self.btn_Remove.Disable()
        event.Skip()

    def OnCheck(self, event):  # wxGlade: MainFrame.<event_handler>
        if self.tree_file.ItemHasChildren(self.root):
            self.tree_file.DeleteChildren(self.root)
        targetPath = self.txt_path.GetValue()
        if self.txt_path.GetValue() is not None:
            core.GetList(targetPath)
            self.tree_file.SetItemHasChildren(self.root)
            core.GetRepeated()
            self.ShowList()
            self.tree_file.Expand(self.root)
            self.btn_Remove.Enable()
        else:
            event.Skip()

    def OnRemove(self, event):  # wxGlade: MainFrame.<event_handler>
        dlg = wx.MessageDialog(self, "Are you sure want to remove the repeated files?", "Remove", wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal() == wx.ID_YES
        dlg.Destroy()
        if result:
            core.RemoveRepeated()
            self.tree_file.DeleteChildren(self.root)
            self.ShowList()
            self.tree_file.Expand(self.root)
            dlg_done = wx.MessageDialog(self, "Done", "Remove", wx.OK | wx.ICON_QUESTION)
            dlg_done.ShowModal()
            dlg_done.Destroy()
            self.btn_Remove.Disable()

    def ShowList(self):
        for fileItem in core.sortedList:
            child = self.tree_file.AppendItem(self.root, fileItem.getFileName())
            if fileItem.getRepeatedItems():
                self.tree_file.SetItemText(child, fileItem.getFileName() + " *<Repeated files found>*")
                for i in fileItem.getRepeatedItems():
                    self.tree_file.InsertItem(child, child, i.getFileName())
        pass

# end of class MainFrame

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    mainFrame = MainFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(mainFrame)
    mainFrame.Show()
    app.MainLoop()